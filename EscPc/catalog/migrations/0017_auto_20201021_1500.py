# Generated by Django 3.1.2 on 2020-10-21 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0016_auto_20201021_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placasmadre',
            name='imagen',
            field=models.ImageField(upload_to='fotos'),
        ),
    ]