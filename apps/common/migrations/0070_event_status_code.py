# Generated by Django 4.2.8 on 2024-12-09 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0069_event_input_event_output"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="status_code",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
