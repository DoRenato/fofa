# Generated by Django 3.2.3 on 2021-11-09 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swot', '0026_comentariofator_horario'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentarioobjetivo',
            name='horario',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
