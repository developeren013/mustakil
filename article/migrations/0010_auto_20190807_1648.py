# Generated by Django 2.1.5 on 2019-08-07 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_auto_20190807_1645'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='view',
            new_name='viewNumber',
        ),
    ]