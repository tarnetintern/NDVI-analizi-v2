# Generated by Django 3.1 on 2020-08-18 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0006_auto_20200818_1543'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='tarih',
            new_name='title',
        ),
    ]