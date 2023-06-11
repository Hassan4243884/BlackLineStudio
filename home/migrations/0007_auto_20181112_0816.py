# Generated by Django 2.1.3 on 2018-11-12 13:16

from django.db import migrations
import home.blocks
import home.models
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20181112_0624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('index_slider', wagtail.blocks.StructBlock([('logo', wagtail.images.blocks.ImageChooserBlock(required=True)), ('first_line', wagtail.blocks.CharBlock()), ('second_line', wagtail.blocks.CharBlock()), ('third_line', wagtail.blocks.CharBlock()), ('images', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock(required=True))), ('cta_text', wagtail.blocks.CharBlock())])), ('heading', wagtail.blocks.CharBlock(classname='full title')), ('paragraph', home.models.CustomRichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('content_section', wagtail.blocks.StructBlock([('left_part', wagtail.blocks.StreamBlock([('text_block', wagtail.blocks.StructBlock([('header', wagtail.blocks.CharBlock(required=False)), ('content', wagtail.blocks.StreamBlock([('rich_text', wagtail.blocks.RichTextBlock()), ('mobile_hidden_text', home.blocks.SpoilerMobileText())]))])), ('double_image_block', wagtail.blocks.StructBlock([('first_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('second_image', wagtail.images.blocks.ImageChooserBlock(required=True))]))]))]))]),
        ),
    ]
