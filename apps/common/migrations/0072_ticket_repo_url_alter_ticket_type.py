# Generated by Django 4.2.8 on 2024-12-14 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0071_generatedapp"),
    ]

    operations = [
        migrations.AddField(
            model_name="ticket",
            name="repo_url",
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="type",
            field=models.CharField(
                choices=[
                    ("PRODUCT_ASSISTANCE", "Product Assistance"),
                    ("PLATFORM", "Platform"),
                    ("SUGGESTED_FEATURE", "Suggested Feature"),
                    ("GENERATED_APP", "Generated App"),
                ],
                default="PRODUCT_ASSISTANCE",
                max_length=100,
            ),
        ),
    ]