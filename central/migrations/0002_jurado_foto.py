# Generated by Django 4.2.3 on 2024-02-26 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jurado',
            name='foto',
            field=models.ImageField(null=True, upload_to='jurados/'),
        ),
    ]
