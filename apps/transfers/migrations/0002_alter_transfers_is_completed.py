# Generated by Django 4.2.5 on 2023-09-11 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfers',
            name='is_completed',
            field=models.BooleanField(default=False, verbose_name='Подтверждение'),
        ),
    ]