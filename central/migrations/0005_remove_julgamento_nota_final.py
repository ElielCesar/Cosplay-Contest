# Generated by Django 4.2.3 on 2024-03-02 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('central', '0004_remove_jurado_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='julgamento',
            name='nota_final',
        ),
    ]