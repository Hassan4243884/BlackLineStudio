from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtailmetadata.models import MetadataPageMixin
from .blocks import IndexSliderBlock, ContentSection, GalleryBlock, SimplePageHeader, ServicesBlock, CountersBlock, \
    ArtistGalleryBlock, CTABlock, InstagramBlock, TestimonialsBlock, ServicesPageBlock, ChildPagesMenu, \
    LargeGalleryBlock, TeamMemberPageBlock, DynamicContentSection, MobileContentSection, ServicesBlockFullSize, \
    TabbedContent, SpoilerTextBlock


class CustomRichTextBlock(blocks.RichTextBlock):
    pass

    class Meta:
        template = 'blocks/rich_text_block.html'


class HomePage(MetadataPageMixin, Page):
    body = StreamField([
        ('index_slider', IndexSliderBlock()),
        ('content_section', ContentSection()),
        ('simple_gallery', GalleryBlock()),
        ('simple_page_header', SimplePageHeader()),
        ('services_block', ServicesBlock()),
        ('services_block_full_size', ServicesBlockFullSize()),
        ('counters_block', CountersBlock()),
        ('cta_block', CTABlock()),
        ('instagram_block', InstagramBlock()),
        ('testimonials_block', TestimonialsBlock()),
        ('child_pages_block', ChildPagesMenu()),
        ('large_gallery_block', LargeGalleryBlock()),
        ('dynamic_section', DynamicContentSection()),
        ('mobile_block', MobileContentSection()),
        ('tabbed_content', TabbedContent()),
        ('text', SpoilerTextBlock()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'


SERVICES_ICONS = (
    ('svg-icons/acne-removal.html', 'Acne Removal'),
    ('svg-icons/airbrush_icn.html', 'Airbrush'),
    ('svg-icons/bird_icn.html', 'Bird'),
    ('svg-icons/body_art_icn.html', 'Body Art'),
    ('svg-icons/ear_icn.html', 'Ear'),
    ('svg-icons/face_icn.html', 'Face'),
    ('svg-icons/gun_icn.html', 'Gun'),
    ('svg-icons/laser_icn.html', 'Laser'),
    ('svg-icons/reviv_icn.html', 'Reviv'),
)


class ServicePage(MetadataPageMixin, Page):
    menu_icon = models.CharField(max_length=100, choices=SERVICES_ICONS, help_text='Icon for service menus', default='svg-icons/bird_icn.html')
    short_description = models.TextField(help_text='Short descriptions for service menus', blank=True)

    body = StreamField([
        ('content_section', ContentSection()),
        ('simple_gallery', GalleryBlock()),
        ('simple_page_header', SimplePageHeader()),
        ('services_block', ServicesBlock()),
        ('services_block_full_size', ServicesBlockFullSize()),
        ('counters_block', CountersBlock()),
        ('cta_block', CTABlock()),
        ('instagram_block', InstagramBlock()),
        ('testimonials_block', TestimonialsBlock()),
        ('child_pages_block', ChildPagesMenu()),
        ('large_gallery_block', LargeGalleryBlock()),
        ('dynamic_section', DynamicContentSection()),
        ('mobile_block', MobileContentSection()),
        ('tabbed_content', TabbedContent()),
    ])

    content_panels = Page.content_panels + [
        FieldPanel('menu_icon'),
        FieldPanel('short_description'),
        StreamFieldPanel('body'),
    ]

    class Meta:
        verbose_name = 'Service Page'
        verbose_name_plural = 'Service Pages'


class TeamPage(MetadataPageMixin, Page):
    body = StreamField([
        ('team_member_block', TeamMemberPageBlock()),
        ('cta_block', CTABlock()),
        ('instagram_block', InstagramBlock()),
        ('testimonials_block', TestimonialsBlock()),
        ('large_gallery_block', LargeGalleryBlock()),
        ('tabbed_content', TabbedContent()),
    ])

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

    class Meta:
        verbose_name = 'Team Member Page'
        verbose_name_plural = 'Team Member Pages'


class SiteElement(models.Model):
    name = models.CharField(max_length=255, blank=True)
    key = models.CharField(max_length=255, unique=True, help_text='Do no change')
    value = models.TextField(blank=True)

    def __str__(self):
        return '{name} ({key})'.format(name=self.name, key=self.key)

    class Meta:
        verbose_name = 'Site Element'
        verbose_name_plural = 'Site Elements'


class ThankYouPage(MetadataPageMixin, Page):
    header = models.CharField(max_length=255)
    body = models.TextField(help_text='Short descriptions for service menus', blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('header'),
        FieldPanel('body'),
    ]

    parent_page_types = ['home.HomePage']
    subpage_types = []

    class Meta:
        verbose_name = 'Thank You Page'
        verbose_name_plural = 'Thank You Pages'
