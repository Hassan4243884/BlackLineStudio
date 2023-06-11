from django import forms
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget

class ContactForm(forms.Form):
    name = forms.CharField(label='Name')
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Phone')
    location = forms.CharField(label='Location', required=False)
    interest = forms.CharField(label='What are you interested in?', required=False)
    captcha = ReCaptchaField(widget=ReCaptchaWidget())

