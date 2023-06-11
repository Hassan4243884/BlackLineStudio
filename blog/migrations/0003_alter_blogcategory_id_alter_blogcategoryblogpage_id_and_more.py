# Generated by Django 4.2.2 on 2023-06-10 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
        ("blog", "0002_auto_20181119_0918"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogcategory",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="blogcategoryblogpage",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="blogpagetag",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="blogpagetag",
            name="tag",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(app_label)s_%(class)s_items",
                to="taggit.tag",
            ),
        ),
    ]
