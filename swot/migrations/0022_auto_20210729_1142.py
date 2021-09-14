# Generated by Django 3.2.3 on 2021-07-29 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_membro_lider_objetivo'),
        ('swot', '0021_auto_20210729_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planejamento',
            name='lider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plan_lider_rel', to='users.membro'),
        ),
        migrations.AlterField(
            model_name='planejamento',
            name='membros',
            field=models.ManyToManyField(blank=True, null=True, related_name='plan_membros_rel', to='users.Membro'),
        ),
    ]