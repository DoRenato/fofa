# Generated by Django 3.2.3 on 2021-09-14 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20210906_1823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='convite',
            name='resolvido',
        ),
        migrations.RemoveField(
            model_name='convite',
            name='convidado',
        ),
        migrations.AddField(
            model_name='convite',
            name='convidado',
            field=models.ManyToManyField(blank=True, related_name='convidado', to='users.Membro'),
        ),
    ]
