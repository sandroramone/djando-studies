# Generated by Django 4.1.7 on 2023-02-21 15:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("galeria", "0004_fotografia_data_fotografia"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fotografia",
            name="foto",
            field=models.ImageField(blank=True, upload_to="fotos/%Y/%m/%d/"),
        ),
    ]
