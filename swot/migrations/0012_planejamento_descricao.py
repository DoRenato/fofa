# Generated by Django 3.2.3 on 2021-07-13 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swot', '0011_rename_tipo_fatores_elemento'),
    ]

    operations = [
        migrations.AddField(
            model_name='planejamento',
            name='descricao',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
