# Generated by Django 4.1.3 on 2023-03-15 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historia', '0005_rename_participantes_participante'),
    ]

    operations = [
        migrations.AddField(
            model_name='participante',
            name='participa',
            field=models.CharField(max_length=100, null=True, verbose_name='Participa'),
        ),
    ]
