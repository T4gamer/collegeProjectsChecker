# Generated by Django 4.2.7 on 2024-01-08 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0007_project_teacher"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="project",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="api.project",
            ),
        ),
    ]