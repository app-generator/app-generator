# Generated by Django 4.2.8 on 2024-11-02 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0054_products_url_video"),
    ]

    operations = [
        migrations.AddField(
            model_name="ticket",
            name="custom_development",
            field=models.BooleanField(default=False),
        ),
    ]
