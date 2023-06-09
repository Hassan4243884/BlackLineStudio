# Generated by Django 2.1.3 on 2018-11-12 18:31

from django.db import migrations
import home.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20181112_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teampage',
            name='body',
            field=wagtail.core.fields.StreamField([('team_member_block', wagtail.core.blocks.StructBlock([('background', wagtail.images.blocks.ImageChooserBlock()), ('header', wagtail.core.blocks.CharBlock(required=True)), ('name', wagtail.core.blocks.CharBlock(required=True)), ('photo', wagtail.images.blocks.ImageChooserBlock()), ('job_title', wagtail.core.blocks.CharBlock(required=True)), ('content', wagtail.core.blocks.RichTextBlock())])), ('cta_block', wagtail.core.blocks.StructBlock([('header', wagtail.core.blocks.CharBlock(default='Let Us Bring Your Vision to Life!', required=True)), ('form_cta_text', wagtail.core.blocks.CharBlock(default='Book a free consultation', required=True)), ('phone_cta_text', wagtail.core.blocks.CharBlock(default='Speak with an artist:', required=True)), ('phone_cta_number', wagtail.core.blocks.CharBlock(required=True))])), ('instagram_block', home.blocks.InstagramBlock()), ('testimonials_block', wagtail.core.blocks.StructBlock([('header', wagtail.core.blocks.CharBlock(required=True)), ('testimonials', wagtail.core.blocks.ListBlock(home.blocks.TestimonialBlock))])), ('large_gallery_block', wagtail.core.blocks.StructBlock([('header', wagtail.core.blocks.CharBlock(required=False)), ('images', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock(required=True)))]))]),
        ),
    ]