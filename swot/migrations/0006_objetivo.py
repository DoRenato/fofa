# Generated by Django 3.2.3 on 2021-07-07 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swot', '0005_fatores_swot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Objetivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('concluido', models.BooleanField(default=False)),
            ],
        ),
    ]
