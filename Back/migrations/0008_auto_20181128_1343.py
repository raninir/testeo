# Generated by Django 2.1.3 on 2018-11-28 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Back', '0007_auto_20181109_2138'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Mascota',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='user',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
