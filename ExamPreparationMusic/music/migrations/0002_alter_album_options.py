# Generated by Django 4.1.2 on 2022-10-28 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ('genre',)},
        ),
    ]
