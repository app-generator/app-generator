# Generated by Django 4.2.8 on 2024-11-04 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0055_ticket_custom_development"),
    ]

    operations = [
        migrations.AlterField(
            model_name="props",
            name="category",
            field=models.CharField(
                choices=[("DOWNLOAD", "Downlaod"), ("FEATURE", "Feature")],
                max_length=250,
            ),
        ),
    ]
