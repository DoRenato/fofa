# Generated by Django 3.2.3 on 2021-10-24 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swot', '0025_objetivo_elemento'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentariofator',
            name='horario',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
