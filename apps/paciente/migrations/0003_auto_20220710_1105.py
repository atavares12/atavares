# Generated by Django 2.2.10 on 2022-07-10 11:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0002_auto_20220710_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='user',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]