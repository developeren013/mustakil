# Generated by Django 2.1.5 on 2019-08-07 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_article_kategori'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='view',
            field=models.IntegerField(default=0, verbose_name='Görüntülenme'),
        ),
    ]