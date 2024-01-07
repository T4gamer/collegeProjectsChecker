# Generated by Django 4.2.7 on 2024-01-07 03:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0005_project_delivery_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="requirement",
            name="status",
            field=models.CharField(
                choices=[("c", "completed"), ("i", "incomplete")],
                default="i",
                max_length=2,
                null=True,
            ),
        ),
    ]
