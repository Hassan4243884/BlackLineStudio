import csv

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.utils.safestring import mark_safe
from wagtail.contrib.modeladmin.helpers import PermissionHelper
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register, ModelAdminGroup)
from wagtail.contrib.modeladmin.views import IndexView

from .models import Form, History, Recipient

from django.urls import path
from wagtail.core import hooks
from django.shortcuts import get_object_or_404, redirect
from django.template import engines
from django.core.mail import EmailMessage


class FormModelAdmin(ModelAdmin):
    model = Form
    menu_label = 'Forms'
    menu_icon = 'form'
    list_display = ('name', 'email_subject', )
    search_fields = ('name',)


class HistoryPermissionHelper(PermissionHelper):

    def user_can_create(self, user):
        return False


class HistoryAdminView(IndexView):
    EXPORT_CSV_FLAG = 'export_csv'
    ORDER_VAR = 'o'
    ORDER_TYPE_VAR = 'ot'
    PAGE_VAR = 'p'
    SEARCH_VAR = 'q'
    ERROR_FLAG = 'e'
    IGNORED_PARAMS = (ORDER_VAR, ORDER_TYPE_VAR, SEARCH_VAR, EXPORT_CSV_FLAG)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        # Only continue if logged in user has list permission
        if not self.permission_helper.user_can_list(request.user):
            raise PermissionDenied

        self.list_display = self.model_admin.get_list_display(request)
        self.list_filter = self.model_admin.get_list_filter(request)
        self.search_fields = self.model_admin.get_search_fields(request)
        self.items_per_page = self.model_admin.list_per_page
        self.select_related = self.model_admin.list_select_related

        # Get search parameters from the query string.
        try:
            self.page_num = int(request.GET.get(self.PAGE_VAR, 0))
        except ValueError:
            self.page_num = 0

        self.params = dict(request.GET.items())
        if self.PAGE_VAR in self.params:
            del self.params[self.PAGE_VAR]
        if self.ERROR_FLAG in self.params:
            del self.params[self.ERROR_FLAG]
        if self.EXPORT_CSV_FLAG in self.params:
            del self.params[self.EXPORT_CSV_FLAG]

        self.query = request.GET.get(self.SEARCH_VAR, '')
        self.queryset = self.get_queryset(request)

        if request.GET.get(self.EXPORT_CSV_FLAG):
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="history-export.csv"'

            writer = csv.writer(response)
            for i in self.queryset:
                writer.writerow([i.created, i.ip, i.form.name, i.seed, mark_safe(i.data)])
            return response

        return super().dispatch(request, *args, **kwargs)


class HistoryAdmin(ModelAdmin):
    model = History
    index_view_class = HistoryAdminView
    menu_label = 'Form History'
    menu_icon = 'date'
    list_display = ('created', 'ip', 'form', 'sent')
    list_filter = ('form', 'seed')
    date_hierarchy = 'created'
    permission_helper_class = HistoryPermissionHelper


class RecipientAdmin(ModelAdmin):
    model = Recipient
    menu_icon = 'user'
    menu_label = 'Recipients'
    list_display = ('name', 'email')


class ContactGroupMenu(ModelAdminGroup):
    menu_label = 'Contacts'
    menu_icon = 'mail'
    items = (FormModelAdmin, HistoryAdmin, RecipientAdmin)


modeladmin_register(ContactGroupMenu)

DEFAULT_EMAIL_SUBJECT = 'New Web Submissio' \
                        ''

DEFAULT_EMAIL_TEXT = '''
<p>Hello <strong>{{ user }}</strong>,</p>
<p>Someone has submitted the contact form at <strong>{{ host }}</strong>:<br />
The request was submitted on <strong>{{ created|date }}</strong> at <strong>{{ created|time }}</strong>
from the IP address of <strong>{{ ip }}</strong>.</p>
<p>Request details:</p>
<p>{{ data }}</p>
<p>Truly yours,<br />
Mailer daemon @ <strong>{{ host }}</strong></p>'''

def create_form_data(data):
    s = u'<table style="border-collapse: collapse;">'
    for key, value in data:
        if key in ['captcha']:
            continue

        if type(value) == bool:
            value = 'Yes' if value else 'No'
        if isinstance(value, (list,)):
            value = ', '.join(map(str, value))

        s += u'''
        <tr>
            <th style="border:1px solid #ccc; text-align: left; padding: 0.6em;">{field_label}</th>
            <td style="border:1px solid #ccc; text-align: left; padding: 0.6em;">{field_value}</td>
        </tr>
        '''.format(field_label=key, field_value=value)

    s += u'</table>'
    return s
def resend_form(request, history_id):
    instance = get_object_or_404(History, id=history_id)
    form = instance.form

    data = {
        'data': create_form_data(instance.get_data()),
        'ip': instance.ip,
        'id': instance.id,
        'created': instance.created,
        'host': request.META.get('HTTP_HOST', 'your website'),
    }
    ctx = dict(data)

    for r in form.recipients.filter(active=True):
        ctx['user'] = r.name or 'Admin'
        subject = engines['django'].from_string(
            u'{%% autoescape off %%}%s{%% endautoescape %%}' % DEFAULT_EMAIL_SUBJECT).render(ctx)
        message = engines['django'].from_string(
            u'{%% autoescape off %%}%s{%% endautoescape %%}' % DEFAULT_EMAIL_TEXT).render(ctx)
        msg = EmailMessage(subject, message, 'info@clovermortgage.ca', [r.email])
        msg.content_subtype = "html"
        msg.send()

    instance.sent = True
    instance.save()
    return redirect('/admin/contact/history/')

@hooks.register('register_admin_urls')
def register_calendar_url():
    return [
        path('resend/<int:history_id>', resend_form, name='resend_form'),
    ]