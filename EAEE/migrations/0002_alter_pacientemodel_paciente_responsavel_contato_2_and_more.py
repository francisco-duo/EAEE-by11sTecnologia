# Generated by Django 4.2.7 on 2023-12-12 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EAEE', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacientemodel',
            name='paciente_responsavel_contato_2',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='pacientemodel',
            name='paciente_responsavel_estado_civil',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='pacientemodel',
            name='paciente_responsavel_profissao',
            field=models.CharField(max_length=255),
        ),
    ]
