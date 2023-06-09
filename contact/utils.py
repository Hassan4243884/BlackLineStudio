from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template import engines, RequestContext
from django.template.loader import render_to_string

from contact.models import Form
from enjoy.settings import DEFAULT_SENDER, DEFAULT_SITE_URL


def send_form_email(sender, receivers, subject, data, template, request=None):
    subject = engines['django'].from_string(
        '{{% autoescape off %}}{}{{% endautoescape %}}'.format(subject)).render(data)
    data['site'] = DEFAULT_SITE_URL
    if request:
        data['site'] = get_current_site(request)
    message = engines['django'].from_string(
        '{{% autoescape off %}}{}{{% endautoescape %}}'.format(template)).render(data)
    msg = EmailMessage(subject, message, sender, receivers)
    msg.content_subtype = "html"
    msg.send()


def send_template_email(sender, receivers, subject, data, template, request=None):
    subject = engines['django'].from_string(
        '{{% autoescape off %}}{}{{% endautoescape %}}'.format(subject)).render(data)
    data['site'] = DEFAULT_SITE_URL
    if request:
        data['site'] = get_current_site(request)
        message = render_to_string(template, data, request=request)
    else:
        message = render_to_string(template, data)
    msg = EmailMessage(subject, message, sender, receivers)
    msg.content_subtype = "html"
    msg.send()


def send_register_email(email, username, password, first_name, request):
    form = Form.objects.get(key='register')
    data = {
        'email': email,
        'first_name': first_name,
        'username': username,
        'password': password,
    }
    sender = form.sender if form.sender else DEFAULT_SENDER
    send_template_email(sender, [email,], form.email_subject, data, 'emails/register.html', request)


def send_user_card_update_email(user_id, request):
    form = Form.objects.get(key='user_card_update')
    data = {
        'user_id': user_id,
    }
    sender = form.sender if form.sender else DEFAULT_SENDER
    send_form_email(
        sender, [r.email for r in form.recipients.filter(active=True)],
        form.email_subject, data, form.email_text, request
    )


def send_user_card_status_email(user):
    form = Form.objects.get(key='user_card_status_change')
    data = {
        'first_name': user.user.first_name,
        'email': user.user.email,
        'card_status': user.get_card_status_display(),
    }
    sender = form.sender if form.sender else DEFAULT_SENDER
    send_template_email(
        sender, [user.user.email, ],
        form.email_subject, data, 'emails/card_status.html'
    )


def send_new_review_or_comment_email(url, request):
    form = Form.objects.get(key='new_review_or_comment')
    data = {
        'url': url
    }
    sender = form.sender if form.sender else DEFAULT_SENDER
    send_form_email(
        sender, [r.email for r in form.recipients.filter(active=True)],
        form.email_subject, data, form.email_text, request
    )


def send_new_comment_to_user_email(url, user):
    form = Form.objects.get(key='new_comment_to_user')
    data = {
        'email': user.email,
        'first_name': user.first_name,
        'link_to_product': url,
    }
    sender = form.sender if form.sender else DEFAULT_SENDER
    send_template_email(
        sender, [user.email, ],
        form.email_subject, data, 'emails/new_user_comment.html'
    )


def send_order_email(order, request):
    form = Form.objects.get(key='order_confirm')
    data = {
        'email': order.email,
        'first_name': order.name,
        'order': order,
    }
    sender = form.sender if form.sender else DEFAULT_SENDER
    send_template_email(sender, [order.email, ], form.email_subject, data, 'emails/order_confirm.html', request)


def send_order_admin_email(order, request):
    form = Form.objects.get(key='order_admin_confirm')
    data = {
        'url': '/admin/cart/order/{}/change/'.format(order.id)
    }
    sender = form.sender if form.sender else DEFAULT_SENDER
    send_form_email(
        sender, [r.email for r in form.recipients.filter(active=True)],
        form.email_subject, data, form.email_text, request
    )
