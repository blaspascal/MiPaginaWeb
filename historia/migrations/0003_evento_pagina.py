# Generated by Django 4.1.3 on 2023-03-14 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historia', '0002_evento'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='pagina',
            field=models.CharField(max_length=100, null=True, verbose_name='Pagina'),
        ),
    ]
