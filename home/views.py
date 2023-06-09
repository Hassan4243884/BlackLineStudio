from django.http import HttpResponse
from django.views import View

from home.models import SiteElement


class RobotsView(View):
    def get(self, request, *args, **kwargs):
        try:
            data = SiteElement.objects.get(key='robots').value
        except SiteElement.DoesNotExist:
            data = ''
        return HttpResponse(data, content_type='text/plain')
