# Generated by Django 3.2.9 on 2023-02-01 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0004_alter_uploadfile_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='file',
            field=models.FileField(null=True, upload_to='documents/'),
        ),
    ]
