# Generated by Django 4.1 on 2023-06-28 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0006_fotografia_data_fotografia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='foto',
            field=models.ImageField(blank=True, upload_to='foto/%Y/%m/%d/'),
        ),
    ]
