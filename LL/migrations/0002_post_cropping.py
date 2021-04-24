# Generated by Django 3.2 on 2021-04-23 13:08

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('LL', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '1280x720', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
    ]
