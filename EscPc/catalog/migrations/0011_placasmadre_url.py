# Generated by Django 3.1.2 on 2020-10-21 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20201021_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='placasmadre',
            name='url',
            field=models.URLField(default='', max_length=100),
        ),
    ]
