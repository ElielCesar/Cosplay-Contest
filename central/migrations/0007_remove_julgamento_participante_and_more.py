# Generated by Django 4.2.3 on 2024-03-03 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('central', '0006_rename_nota_criatidade_julgamento_nota_criatividade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='julgamento',
            name='participante',
        ),
        migrations.AddField(
            model_name='julgamento',
            name='participante_fantasy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='julgamentos_fantasy', to='central.fantasy'),
        ),
    ]