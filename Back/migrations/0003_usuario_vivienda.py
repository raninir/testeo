# Generated by Django 2.1.2 on 2018-11-09 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Back', '0002_auto_20181108_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='vivienda',
            field=models.CharField(default='', max_length=20),
        ),
    ]
