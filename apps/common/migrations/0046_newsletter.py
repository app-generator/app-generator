# Generated by Django 4.2.8 on 2024-10-29 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0045_alter_event_text"),
    ]

    operations = [
        migrations.CreateModel(
            name="Newsletter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("mailchimp", models.BooleanField(default=False)),
                ("subscribed_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
