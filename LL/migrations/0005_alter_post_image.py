# Generated by Django 3.2 on 2021-04-23 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LL', '0004_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]