# Generated by Django 2.1.5 on 2019-11-25 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0017_auto_20191003_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='onay',
            field=models.BooleanField(default=False, verbose_name='Onay'),
        ),
    ]
