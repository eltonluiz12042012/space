# Generated by Django 4.1 on 2023-06-24 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
