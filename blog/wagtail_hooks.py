from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import BlogPage


class MyPageModelAdmin(ModelAdmin):
    model = BlogPage
    menu_label = 'Blog Pages'  # ditch this to use verbose_name_plural from model
    list_display = ('title', 'date', )
    list_filter = ('live', )
    search_fields = ('title',)

# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(MyPageModelAdmin)