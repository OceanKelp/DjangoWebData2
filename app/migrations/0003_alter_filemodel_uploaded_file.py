# Generated by Django 4.2.4 on 2024-01-22 02:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_filemodel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="filemodel",
            name="uploaded_file",
            field=models.FileField(upload_to="app.uploads/"),
        ),
    ]