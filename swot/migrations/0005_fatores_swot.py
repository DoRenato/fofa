# Generated by Django 3.2.3 on 2021-07-07 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('swot', '0004_elementos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Swot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Fatores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swot.elementos')),
            ],
        ),
    ]
