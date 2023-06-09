from django.http import JsonResponse
from django.shortcuts import redirect

from contact import handle_form
from .models import Form
from .forms import ContactForm


def contact_form_middleware(get_response):

    def middleware(request):
        if request.POST and 'contact_form' in request.POST:
            error_data = []
            if request.POST.get('location') == 'Uptown':
                form, success = handle_form('contact_form_uptown', request, ContactForm, error_data=error_data)
            else:
                form, success = handle_form('contact_form', request, ContactForm, error_data=error_data)
            data = {'success': False, 'errors': None, 'form_fields': None}
            redirect_to = None
            if error_data:
                redirect_to = ''.join(('/thank-you/?form-error=', error_data[0]))
            data.update(success=success, errors=form.errors, form_fields=list(form.fields.keys()), redirect_to=redirect_to)
            return JsonResponse(data)
        else:
            form = ContactForm()
        request.contact_form = form
        response = get_response(request)

        return response

    return middleware
