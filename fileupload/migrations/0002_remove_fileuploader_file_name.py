# Generated by Django 4.1.2 on 2022-10-11 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("fileupload", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="fileuploader", name="file_name",),
    ]