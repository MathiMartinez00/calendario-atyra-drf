# Generated by Django 3.0.8 on 2020-10-19 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarios', '0009_auto_20201009_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservas',
            name='precio',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='reservas',
            name='estado',
            field=models.IntegerField(choices=[(0, 'Pendiente'), (1, 'Ocupado')], default=1),
        ),
    ]
