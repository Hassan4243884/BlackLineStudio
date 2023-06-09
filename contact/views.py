from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from contact import handle_form
from contact.forms import StoryForm, ContactForm, NotRegisteredForm
from contact.models import Subscriber, RegistrationCompleteEvent
from quiz.models import Question


@csrf_exempt
def ajax_submit_story(request):
    form, success = handle_form('story-form', request, StoryForm, 'photo')
    result = {
        'success': success,
        'errors': [field for field, errors in form.errors.items()] if not success else [],
    }
    return JsonResponse(result, safe=False)


@csrf_exempt
def ajax_submit_contact(request):
    form, success = handle_form('contact-form', request, ContactForm)
    result = {
        'success': success,
        'errors': [field for field, errors in form.errors.items()] if not success else [],
    }
    return JsonResponse(result, safe=False)


@csrf_exempt
def ajax_submit_subscribe(request):
    result = {
        'status': False
    }

    if request.POST.get('email'):
        result = {
            'success': True
        }
        subscriber = Subscriber(email=request.POST.get('email'))
        subscriber.save()
    return JsonResponse(result, safe=False)


@csrf_exempt
def ajax_submit_not_registered(request):
    form, success = handle_form('not-registered-form', request, NotRegisteredForm)
    result = {
        'success': success,
        'errors': [field for field, errors in form.errors.items()] if not success else [],
    }
    return JsonResponse(result, safe=False)


@csrf_exempt
def ajax_submit_registration(request):
    result = {
        'status': True
    }
    if request.is_ajax():
        print('hello')
        event = RegistrationCompleteEvent()
        event.save()
    return JsonResponse(result, safe=False)
