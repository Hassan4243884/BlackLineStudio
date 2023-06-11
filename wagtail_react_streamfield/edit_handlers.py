from wagtail.admin.panels import FieldPanel


class NewFieldPanel(FieldPanel):
    def html_declarations(self):
        return ''
