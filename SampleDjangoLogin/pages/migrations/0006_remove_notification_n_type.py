# Generated by Django 5.0.2 on 2024-10-29 15:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0005_notification"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="notification",
            name="n_type",
        ),
    ]
