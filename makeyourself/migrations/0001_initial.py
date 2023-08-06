# Generated by Django 4.2.3 on 2023-08-05 23:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jurado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=50)),
                ('personagem', models.CharField(max_length=200)),
                ('imagem', models.ImageField(upload_to='makeyourself/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Julgamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota_estetica', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('nota_criatividade', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('nota_performance', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('nota_sustentabilidade', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('nota_final', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(4)])),
                ('observacao', models.CharField(blank=True, max_length=300, null=True)),
                ('jurado', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='makeyourself.jurado')),
                ('participante', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='makeyourself.participante')),
            ],
        ),
    ]
