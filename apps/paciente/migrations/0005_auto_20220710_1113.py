# Generated by Django 2.2.10 on 2022-07-10 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0004_auto_20220710_1112'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paciente',
            old_name='user',
            new_name='criado_por',
        ),
    ]
