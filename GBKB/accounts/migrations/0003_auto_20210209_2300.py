# Generated by Django 2.2 on 2021-02-09 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210209_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postad',
            name='roadSize',
            field=models.IntegerField(default=1),
        ),
    ]