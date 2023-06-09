from .models import SiteElement
import re


def site_elements(request):
    d = {}
    for s in SiteElement.objects.all():
        n = re.sub(r'\W+', '_', s.key).lower()
        d[n] = s

    return {
        'se': d,
    }
