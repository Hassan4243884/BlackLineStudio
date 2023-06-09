from shops.models import OfficePage


def footer_shops(request):
    footer_shops_list = OfficePage.objects.live().filter(show_in_footer=True)
    return {
        'footer_shops_list': footer_shops_list
    }
