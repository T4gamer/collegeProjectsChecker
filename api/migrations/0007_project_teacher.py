# Generated by Django 4.2.7 on 2024-01-08 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0006_requirement_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="teacher",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="api.teacher",
            ),
        ),
    ]
