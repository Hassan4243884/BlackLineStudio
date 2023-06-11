# Generated by Django 2.1.3 on 2018-11-09 14:48

from django.db import migrations
import home.models
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(classname='full title')), ('paragraph', home.models.CustomRichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())]),
        ),
    ]
