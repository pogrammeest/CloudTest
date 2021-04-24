# Generated by Django 3.2 on 2021-04-23 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150)),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('body', models.TextField(blank=True, db_index=True)),
                ('image', models.ImageField(upload_to='images/', verbose_name='Изображение')),
            ],
        ),
    ]
