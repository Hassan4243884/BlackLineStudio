import json

import requests
from django.core.exceptions import ValidationError
from django.db import models
from django.template import engines
from django import forms
from django.conf import settings
from django.template import Context
from django.core.validators import validate_email
from django.core.mail import EmailMessage, mail_admins
import os

from requests import Response
from wagtail.core.fields import RichTextField

from cleantalk.cleantalk import CleanTalk


def create_form_table(form):
    s = u'<table style="border-collapse: collapse;">'
    for field in form:
        if field.name != 'captcha':
            label = field.label
            if isinstance(form.cleaned_data.get(field.name, ''), bool):
                value = 'Yes' if form.cleaned_data.get(field.name, '') else 'No'
            else:
                value = form.cleaned_data.get(field.name, '')
            s += u'''
            <tr>
                <th style="border:1px solid #ccc; text-align: left; padding: 0.6em;">{field_label}</th>
                <td style="border:1px solid #ccc; text-align: left; padding: 0.6em;">{field_value}</td>
            </tr>
            '''.format(field_label=label, field_value=value)
    s += u'</table>'
    return s


DEFAULT_EMAIL_SUBJECT = 'New Web Submission'


DEFAULT_EMAIL_TEXT = '''
<p>Hello <strong>{{ user }}</strong>,</p>
<p>Someone has submitted the contact form at <strong>{{ host }}</strong>:<br />
The request was submitted on <strong>{{ created|date }}</strong> at <strong>{{ created|time }}</strong>
from the IP address of <strong>{{ ip }}</strong>.</p>
<p>Request details:</p>
<p>{{ data }}</p>
<p>Truly yours,<br />
Mailer daemon @ <strong>{{ host }}</strong></p>'''


SOURCE_CHOICES = (
    ('110090', '110090'),
    ('110091', '110091'),
    ('110092', '110092')
)

SOURCE_DICT = {
    'seo': '110091',
    'ppc': '110092',
}


class Form(models.Model):
    key = models.CharField(max_length=255, unique=True, help_text='Don`t change!')
    name = models.CharField(max_length=255)

    sender = models.EmailField(max_length=255, null=True, blank=True)
    sender_field = models.CharField(max_length=128, null=True, blank=True)

    email_subject = models.CharField(max_length=255, default=DEFAULT_EMAIL_SUBJECT)
    email_text = RichTextField(editor='tinymce', verbose_name='body', blank=True, default=DEFAULT_EMAIL_TEXT)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name

    def get_sender(self, form):
        if self.sender_field and self.sender_field.strip():
            try:
                result = form.cleaned_data.get(self.sender_field.strip(), '')
                validate_email(result)
                return result
            except ValidationError:
                pass
        if self.sender:
            return self.sender
        return settings.FROM_EMAIL

    @staticmethod
    def handle_uploaded_file(f, date):
        filename, file_extension = os.path.splitext(f.name)
        dir_name = 'tmp'
        dest_dir = os.path.join(settings.MEDIA_ROOT, dir_name)
        filename = '%s_%s_%s' % (filename, date.strftime("%Y-%m-%d"), file_extension)
        filename_result = os.path.join(dest_dir, filename)
        fi = open(filename_result, 'wb+')
        for chunk in f.chunks():
            fi.write(chunk)
        return filename_result, filename

    def handle_form(self, request, form_class, file=None, file2=None, additional_context=None, error_data=None):
        if request.method == 'POST':
            f = form_class(request.POST, request.FILES)

            ip = request.META.get("REMOTE_ADDR", u"127.0.0.1")
            try:
                BlacklistItem.objects.get(ip=ip)
                return f, False
            except:
                pass
            if f.is_valid():
                history = History()
                history.form = self
                history.ip = request.META.get("REMOTE_ADDR", u"127.0.0.1")
                if request.POST.get('source'):
                    source = SOURCE_DICT.get(request.POST.get('source').lower(), '110090')
                    history.seed = source
                history.data = json.dumps([
                    (field.label, f.cleaned_data.get(k, '')) for k, field in f.fields.items()
                    if not isinstance(field, forms.FileField)
                ])
                history.save()
                success_id = history.id
                table = create_form_table(f)
                data = {
                    'data': table,
                    'ip': history.ip,
                    'id': history.id,
                    'created': history.created,
                    'host': request.META.get('HTTP_HOST', 'your website'),
                }

                ct = CleanTalk(auth_key='y3e6evy9a8uha4u')
                ct_result = ct.request(
                    message=f.cleaned_data.get('message', ''),  # Visitor comment
                    sender_ip=ip,  # Visitor IP address
                    sender_email=f.cleaned_data.get('email', ''),  # Visitor email
                    sender_nickname=f.cleaned_data.get('name', ''),  # Visitor nickname
                    js_on=1,  # Is visitor has JavaScript
                    submit_time=12  # Seconds from start form filling till the form POST
                )

                try:
                    spam_data = {
                        'key': '4de442104de230bd435f17ca373b367b18d0bb54b4f3f64054d4500487e609c7',
                        'ip': ip,
                        'cleantalk': ct_result,
                        'data': {key: value for key, value in history.get_data()}
                    }
                    spam_response = requests.post(url='http://spamassist.icmconsulting.com/spam/history/add/',
                                                  json=spam_data, timeout=3)

                except Exception as e:
                    spam_response = None
                if additional_context:
                    data.update(additional_context)
                try:
                    filename_result = None
                    filename_result2 = None
                    if file and request.FILES.get(file, None):
                        filename_result, filename = self.handle_uploaded_file(request.FILES.get(file), history.created)
                        history.file = os.path.join('tmp', filename)
                        history.save()
                    if file2:
                        filename_result2, filename2 = self.handle_uploaded_file(request.FILES[file2], history.created)
                        history.file2 = os.path.join('tmp', filename2)
                        history.save()
                    sender = self.get_sender(f)
                    if isinstance(spam_response,
                                  Response) and spam_response.status_code == 200 or spam_response == None:
                        for r in self.recipients.filter(active=True):
                            data['user'] = r.name or 'Admin'
                            subject = engines['django'].from_string('{{% autoescape off %}}{}{{% endautoescape %}}'.format(self.email_subject)).render(data)
                            message = engines['django'].from_string('{{% autoescape off %}}{}{{% endautoescape %}}'.format(self.email_text)).render(data)
                            msg = EmailMessage(subject, message, sender, [r.email])
                            if filename_result:
                                msg.attach_file(filename_result)
                            if filename_result2:
                                msg.attach_file(filename_result2)
                            msg.content_subtype = "html"
                            msg.send()
                    else:
                        error_message = ct_result.get('comment', '')
                        error_data.append(error_message)
                        history.sent = False
                        history.save()
                except Exception as e:
                    print(e)
                    import traceback
                    host = request.META.get('HTTP_HOST', 'Unknown host')
                    message = host + '\n\n' + str(e) + '\n\n'
                    mail_admins('Sending contact email failed.', message, fail_silently=True)

                return f, success_id
            else:
                print(f.errors)
        else:
            f = form_class()
        return f, False


class Recipient(models.Model):
    form = models.ForeignKey(Form, related_name='recipients', on_delete=models.CASCADE)
    name = models.CharField(max_length=128, null=True, blank=True)
    email = models.EmailField()
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.email


class History(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=128, null=True, blank=True)
    data = models.TextField(null=True, blank=True)
    seed = models.CharField(max_length=20, blank=False, default='110090', choices=SOURCE_CHOICES,
                              verbose_name='Spam Protection Seed')
    file = models.FileField(upload_to='tmp', max_length=255, blank=True, null=True)
    file2 = models.FileField(upload_to='tmp', max_length=255, blank=True, null=True)

    sent = models.BooleanField(default=True, blank=True)

    def __unicode__(self):
        return 'Contact %s / %s' % (self.created, self.ip)

    def get_data(self):
        return json.loads(self.data)

    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'Histories'


class BlacklistItem(models.Model):
    ip = models.CharField(max_length=15)
    comment = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.ip


class Subscriber(models.Model):
    email = models.EmailField()
    export = models.BooleanField(default=False)


class RegistrationCompleteEvent(models.Model):
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)
