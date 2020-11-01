# Generated by Django 3.1.2 on 2020-10-21 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20201015_1508'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Almacenamiento',
        ),
        migrations.DeleteModel(
            name='FuentesPoder',
        ),
        migrations.DeleteModel(
            name='Gabinete',
        ),
        migrations.DeleteModel(
            name='Gpu',
        ),
        migrations.DeleteModel(
            name='Monitore',
        ),
        migrations.DeleteModel(
            name='Procesadore',
        ),
        migrations.DeleteModel(
            name='Ram',
        ),
        migrations.AddField(
            model_name='placasmadre',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='fotos/'),
        ),
        migrations.AddField(
            model_name='placasmadre',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]