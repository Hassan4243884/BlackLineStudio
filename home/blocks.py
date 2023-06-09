from wagtail.core import blocks
from wagtail.core.blocks import PageChooserBlock
from wagtail.images.blocks import ImageChooserBlock


class SpoilerMobileText(blocks.RichTextBlock):

    class Meta:
        template = 'blocks/rich_text_block.html'


class AdditionalSpolerText(blocks.StructBlock):
    header = blocks.CharBlock(required=False)
    content = blocks.RichTextBlock(required=False)

    class Meta:
        template = 'blocks/additional_text_spoiler.html'

class AdditionalSpolerTextWithButton(blocks.StructBlock):
    content = blocks.RichTextBlock(required=False)

    class Meta:
        template = 'blocks/additional_text_spoiler_with_button.html'


class DoubleImageBlock(blocks.StructBlock):
    first_image = ImageChooserBlock(required=True)
    second_image = ImageChooserBlock(required=True)

    class Meta:
        icon = 'image'
        template = 'blocks/rich_text_block.html'


class ContentImageSliderBlock(blocks.StructBlock):
    images = blocks.ListBlock(ImageChooserBlock(required=True))

    class Meta:
        icon = 'image'
        template = 'blocks/content_image_slider.html'


class SquareContentImageSliderBlock(blocks.StructBlock):
    images = blocks.ListBlock(ImageChooserBlock(required=True))

    class Meta:
        icon = 'image'
        template = 'blocks/square_content_image_slider.html'


class TextBlock(blocks.StructBlock):
    header = blocks.CharBlock(required=False)
    content = blocks.StreamBlock([
            ('rich_text', blocks.RichTextBlock()),
            ('mobile_hidden_text', SpoilerMobileText()),
            ('additional_spoiler_text', AdditionalSpolerText()),
            ('additional_spoiler_text_with_button', AdditionalSpolerTextWithButton())
        ]
    )
    spoiler = blocks.BooleanBlock(required=False)
    anchor = blocks.CharBlock(required=False)

    def is_spoiler_present(self):
        for i in self.child_blocks.get('content').child_blocks:
            if i == 'mobile_hidden_text':
                return True
        return False

    class Meta:
        template = 'blocks/text_block.html'


class SpoilerTextBlock(blocks.StructBlock):
    header = blocks.CharBlock(required=False)
    content = blocks.RichTextBlock()

    class Meta:
        template = 'blocks/spoiler_block.html'

SECTION_BGCOLOR_CHOICES = (
    ('_dark', 'Dark'),
    ('_dark-800', 'Dark-800'),
)


SECTION_BGPOSITION_CHOICES = (
    ('default', 'Default'),
    ('center', 'Center'),
    ('top-left', 'Top Left'),
)


class ContentSection(blocks.StructBlock):
    background = ImageChooserBlock(required=False)
    bg_color = blocks.ChoiceBlock(choices=SECTION_BGCOLOR_CHOICES, default='_dark')
    bg_position = blocks.ChoiceBlock(choices=SECTION_BGPOSITION_CHOICES, default='default')
    left_part = blocks.StreamBlock([
        ('text_block', TextBlock()),
        ('double_image_block', DoubleImageBlock()),
        ('content_image_slider', ContentImageSliderBlock()),
        ('square_content_image_slider', SquareContentImageSliderBlock()),
    ])
    right_part = blocks.StreamBlock([
        ('text_block', TextBlock()),
        ('double_image_block', DoubleImageBlock()),
        ('content_image_slider', ContentImageSliderBlock()),
        ('square_content_image_slider', SquareContentImageSliderBlock()),
    ])

    class Meta:
        template = 'blocks/section.html'


class GalleryBlock(blocks.StructBlock):
    images = blocks.ListBlock(ImageChooserBlock(required=True))

    class Meta:
        icon = 'image'
        template = 'blocks/simple_gallery.html'


class LargeGalleryBlock(blocks.StructBlock):
    header = blocks.CharBlock(required=False)
    items = blocks.ListBlock(blocks.StructBlock([
        ('image', ImageChooserBlock(required=True)),
        ('video_link', blocks.CharBlock(required=False)),
    ]))

    class Meta:
        icon = 'image'
        template = 'blocks/large_gallery.html'


class SimplePageHeader(blocks.StructBlock):
    header = blocks.CharBlock(required=True)
    background = ImageChooserBlock(required=True)
    cta_text = blocks.CharBlock(required=True, default='Book an appointment')

    class Meta:
        template = 'blocks/simple_page_header.html'


class ServicesBlockFullSize(blocks.StructBlock):

    class Meta:
        template = 'blocks/services_block_full_size.html'
        icon = 'list-ul'


class ServicesBlock(blocks.StructBlock):
    header = blocks.CharBlock(required=True)
    background = ImageChooserBlock(required=False)

    class Meta:
        template = 'blocks/services_block.html'
        icon = 'list-ul'


class ServicesPageBlock(blocks.StructBlock):
    background = ImageChooserBlock(required=False)

    class Meta:
        template = 'blocks/services_page_block.html'
        icon = 'list-ul'


class CountersBlock(blocks.StructBlock):
    happy_clients = blocks.IntegerBlock(required=True, min_value=1)
    years_in_business = blocks.IntegerBlock(required=True, min_value=1)
    body_piercings = blocks.IntegerBlock(required=True, min_value=1)
    tattoos = blocks.IntegerBlock(required=True, min_value=1)

    class Meta:
        template = 'blocks/counters_block.html'
        icon = 'list-ul'


class ArtistBlock(blocks.StructBlock):
    name = blocks.CharBlock(required=True)
    title = blocks.CharBlock(required=True)
    photo = ImageChooserBlock(required=True)
    page = PageChooserBlock(required=True)


class ArtistGalleryBlock(blocks.StructBlock):
    header = blocks.CharBlock(required=True)
    artists = blocks.ListBlock(ArtistBlock())
    cta_text = blocks.CharBlock(required=False)
    cta_page = blocks.PageChooserBlock(required=False)

    class Meta:
        icon = 'user'
        template = 'blocks/artists_block.html'


class CTABlock(blocks.StructBlock):
    header = blocks.CharBlock(required=True, default='Let Us Bring Your Vision to Life!')
    form_cta_text = blocks.CharBlock(required=True, default='Book a free consultation')
    phone_cta_text = blocks.CharBlock(required=True, default='Speak with an artist:')
    phone_cta_number = blocks.CharBlock(required=True)

    class Meta:
        template = 'blocks/cta_block.html'


class InstagramBlock(blocks.CharBlock):

    class Meta:
        icon = 'image'
        template = 'blocks/instagram_block.html'


class TestimonialBlock(blocks.StructBlock):
    name = blocks.CharBlock(required=True)
    rating = blocks.IntegerBlock(min_value=1, max_value=5)
    text = blocks.TextBlock(required=True)


class TestimonialsBlock(blocks.StructBlock):
    header = blocks.CharBlock(required=True)
    testimonials = blocks.ListBlock(TestimonialBlock)

    class Meta:
        icon = 'user'
        template = 'blocks/testimonials_block.html'


class ChildPage(blocks.StructBlock):
    name = blocks.CharBlock(required=True)
    image = ImageChooserBlock()
    page = blocks.PageChooserBlock()


class ChildPagesMenu(blocks.StructBlock):
    header = blocks.CharBlock(required=True)
    short_description = blocks.RichTextBlock(required=False)
    pages = blocks.ListBlock(ChildPage())

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        if 'pages' in value:
            context['get_visible'] = value['pages'][:8]
            context['get_hidden'] = value['pages'][8:]
        return context

    class Meta:
        template = 'blocks/child_pages_block.html'


class ProductImagesMenu(blocks.StructBlock):
    images = blocks.ListBlock(ImageChooserBlock())

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        if 'images' in value:
            context['get_visible'] = value['images'][:4]
            context['get_hidden'] = value['images'][4:]
        return context

    class Meta:
        template = 'blocks/product_images_block.html'


class TeamMemberPageBlock(blocks.StructBlock):
    background = ImageChooserBlock()
    header = blocks.CharBlock(required=True)
    name = blocks.CharBlock(required=True)
    photo = ImageChooserBlock()
    job_title = blocks.CharBlock(required=True)
    content = blocks.RichTextBlock()

    class Meta:
        icon = 'user'
        template = 'blocks/team_member_block.html'


class IndexSliderBlock(blocks.StructBlock):
    logo = ImageChooserBlock(required=True)
    first_line = blocks.CharBlock()
    second_line = blocks.CharBlock()
    third_line = blocks.CharBlock()
    images = blocks.ListBlock(ImageChooserBlock(required=True))
    cta_text = blocks.CharBlock()

    class Meta:
        icon = 'image'
        template = 'blocks/index-slider.html'


DYNAMIC_CONTENT_SECTION_BG_COLOR = (
    ('_dark', 'Dark'),
    ('_dark-800', 'Dark 800'),
)

DYNAMIC_CONTENT_SECTION_BG_PATTERN = (
    ('bg-pattern', 'Pattern'),
    ('', 'No Pattern'),
)

DYNAMIC_CONTENT_SECTION_BG_REPEAT = (
    ('', 'No repeat'),
    ('_bg-repeat-y', 'Repeat Y'),
)

DYNAMIC_CONTENT_SECTION_BG_POSITION = (
    ('', 'Default Position'),
    ('_bg-center-left-4', 'Center Left 4'),
    ('_bg-center-right-4', 'Center Right 4'),
    ('_bg-top-left', 'Top Left'),
    ('_bg-center-bottom', 'Center Bottom'),
    ('_bg-center-top', 'Center Top'),
    ('_bg-center', 'Center'),
    ('', 'No Pattern'),
)

GRID_PADDING_CHOICES = (
    ('', 'No padding'),
    ('grid-padding-x', 'Padding X'),
    ('grid-margin-x', 'Margin X'),
)

GRID_ALIGN_CHOICES = (
    ('', 'No align'),
    ('align-justify', 'Justify'),
    ('align-middle align-justify', 'Middle Justify'),
)


class BorderedImage(blocks.StructBlock):
    image = ImageChooserBlock()

    class Meta:
        template = 'blocks/bordered_image.html'


class GroupedImage(blocks.StructBlock):
    first_image = ImageChooserBlock()
    second_image = ImageChooserBlock()

    class Meta:
        template = 'blocks/grouped_image.html'


class BenefitsBlock(blocks.StructBlock):
    icon = ImageChooserBlock()
    title = blocks.CharBlock()
    body = blocks.RichTextBlock()

    class Meta:
        template = 'blocks/benefits_block.html'


class ButtonBlock(blocks.StructBlock):
    text = blocks.CharBlock()
    hard_link = blocks.CharBlock(required=False)
    inner_link = PageChooserBlock(required=False)

    class Meta:
        template = 'blocks/button_block.html'


class PartBlock(blocks.StructBlock):
    additional_classes = blocks.CharBlock(required=False)
    body = blocks.StreamBlock([
        ('text_block', TextBlock()),
        ('content_image_slider', ContentImageSliderBlock()),
        ('bordered_image', BorderedImage()),
        ('grouped_image', GroupedImage()),
        ('square_content_image_slider', SquareContentImageSliderBlock()),
        ('benefits_block', BenefitsBlock()),
        ('button_block', ButtonBlock()),
    ])


class GridContentSection(blocks.StructBlock):
    left_part = PartBlock()
    right_part = PartBlock()

    class Meta:
        template = 'blocks/grid_section.html'


class FullWidthGridContentSection(blocks.StructBlock):
    body = PartBlock()

    class Meta:
        template = 'blocks/full_width_grid_section.html'


class FAQItemBlock(blocks.StructBlock):
    question = blocks.CharBlock()
    answer = blocks.RichTextBlock()


class FAQAccordionBlock(blocks.StructBlock):
    questions = blocks.ListBlock(FAQItemBlock())

    class Meta:
        template = 'blocks/faq_section.html'


class TabItem(blocks.StructBlock):
    name = blocks.CharBlock()
    content = blocks.RichTextBlock()


class TabbedContent(blocks.StructBlock):
    header = blocks.CharBlock(required=False)
    tabs = blocks.ListBlock(TabItem())
    id = blocks.CharBlock(required=False)

    class Meta:
        template = 'blocks/tabbed_block.html'


class GridContainer(blocks.StructBlock):
    grid_padding = blocks.ChoiceBlock(choices=GRID_PADDING_CHOICES, required=False)
    grid_align = blocks.ChoiceBlock(choices=GRID_ALIGN_CHOICES, required=False)
    additional_classes = blocks.CharBlock(required=False)
    inner_additional_classes = blocks.CharBlock(required=False)

    body = blocks.StreamBlock([
        ('full_width_content_section', FullWidthGridContentSection()),
        ('content_section', GridContentSection()),
        ('faq_section', FAQAccordionBlock()),
        ('product_images_block', ProductImagesMenu()),
    ])

    class Meta:
        template = 'blocks/grid.html'


class SectionTitle(blocks.CharBlock):
    additional_classes = blocks.CharBlock(required=False)

    class Meta:
        template = 'blocks/section_header.html'


class SectionIndent(blocks.StructBlock):
    indent = blocks.IntegerBlock(min_value=1, max_value=3, default=1)
    body = blocks.StreamBlock([
        ('grid', GridContainer()),
        ('section_title', SectionTitle()),
        ('artists_gallery_block', ArtistGalleryBlock()),
    ])

    class Meta:
        template = 'blocks/section_indent.html'


class DynamicContentSection(blocks.StructBlock):
    background = ImageChooserBlock(required=False)
    bg_color = blocks.ChoiceBlock(choices=DYNAMIC_CONTENT_SECTION_BG_COLOR, default='_dark', required=False)
    bg_position = blocks.ChoiceBlock(choices=DYNAMIC_CONTENT_SECTION_BG_POSITION, default='', required=False)
    bg_pattern = blocks.ChoiceBlock(choices=DYNAMIC_CONTENT_SECTION_BG_PATTERN, default='', required=False)
    bg_repeat = blocks.ChoiceBlock(choices=DYNAMIC_CONTENT_SECTION_BG_REPEAT, default='', required=False)
    additional_classes = blocks.CharBlock(required=False)

    body = blocks.StreamBlock([
        ('grid', GridContainer()),
        ('section_title', SectionTitle()),
        ('section_indent', SectionIndent()),
        ('artists_gallery_block', ArtistGalleryBlock()),
    ])

    class Meta:
        template = 'blocks/dynamic_content.html'


class MobileBlock(blocks.StructBlock):
    position = blocks.IntegerBlock(min_value=1)
    body = blocks.StreamBlock([
        ('content_section', GridContentSection()),
        ('simple_gallery', GalleryBlock()),
        ('services_block', ServicesBlock()),
        ('services_block_full_size', ServicesBlockFullSize()),
        ('counters_block', CountersBlock()),
        ('cta_block', CTABlock()),
        ('instagram_block', InstagramBlock()),
        ('testimonials_block', TestimonialsBlock()),
        ('large_gallery_block', LargeGalleryBlock()),
        ('dynamic_content_block', DynamicContentSection()),
    ])


class MobileContentSection(blocks.StructBlock):
    body = blocks.ListBlock(MobileBlock())

    class Meta:
        template = 'blocks/mobile_block.html'
