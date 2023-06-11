from django.db import models

from wagtail.models import Page
from wagtail.fields import StreamField, RichTextField
from wagtail import blocks
from wagtail.images import get_image_model_string
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.panels import FieldPanel
from wagtailmetadata.models import MetadataPageMixin
from home.blocks import DynamicContentSection, GridContainer



class ContactPage(MetadataPageMixin, Page):
    body = StreamField([
        ('grid_container', GridContainer()),
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    subpage_types = ['shops.OfficePage']

    class Meta:
        verbose_name = 'Contact Page'
        verbose_name_plural = 'Contact Page'


class OfficePage(MetadataPageMixin, Page):
    header = models.CharField(max_length=255, blank=True)
    address = models.TextField()
    footer_more_details = models.TextField(blank=True)
    show_in_footer = models.BooleanField(default=False)
    email = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    working_hours = models.TextField(blank=True)
    location_coordinates = models.CharField(max_length=255, blank=True)
    image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Office image'
    )
    body = RichTextField()
    additional_body = StreamField([
        ('dynamic_section', DynamicContentSection()),
    ], blank=True, null=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('header'),
        FieldPanel('address'),
        FieldPanel('footer_more_details'),
        FieldPanel('show_in_footer'),
        FieldPanel('email'),
        FieldPanel('phone'),
        FieldPanel('working_hours'),
        FieldPanel('image'),
        FieldPanel('body'),
        FieldPanel('location_coordinates'),
        FieldPanel('additional_body'),
    ]

    subpage_types = []
    parent_page_types = ['shops.ContactPage']

    class Meta:
        verbose_name = 'Office Page'
        verbose_name_plural = 'Office Pages'

