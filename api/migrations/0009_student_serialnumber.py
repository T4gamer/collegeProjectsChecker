# Generated by Django 4.2.7 on 2024-04-02 20:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0008_alter_student_project"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="serialNumber",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
