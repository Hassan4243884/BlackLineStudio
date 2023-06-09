from django.apps import apps


def handle_form(form_name, request, form_class, pdf=None, pdf2=None, additional_context=None, error_data=None):
    Form = apps.get_model(app_label='contact', model_name='Form')
    return Form.objects.get(key=form_name).handle_form(request, form_class, pdf, pdf2, additional_context, error_data=error_data)


def is_blocked_ip(ip):
    BlacklistItem = apps.get_model(app_label='contact', model_name='Form')
    return not ip or BlacklistItem.objects.filter(ip=ip).count() == 0


def is_blocked(request):
    return is_blocked_ip(request.META.get('REMOTE_ADDR'))

