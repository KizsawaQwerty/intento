# Generated by Django 3.1.2 on 2020-10-21 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0021_auto_20201021_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placasmadre',
            name='imagen',
            field=models.ImageField(upload_to='placasmadres/'),
        ),
    ]