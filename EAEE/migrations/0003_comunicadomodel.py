# Generated by Django 4.2.7 on 2024-01-04 23:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('EAEE', '0002_permissoesmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComunicadoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comunicado_mensagem', models.TextField()),
                ('comunicado_dt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data')),
                ('comunicado_usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
