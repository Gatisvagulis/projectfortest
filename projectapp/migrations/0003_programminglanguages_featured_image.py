# Generated by Django 3.2.5 on 2022-09-27 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0002_auto_20220927_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='programminglanguages',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
