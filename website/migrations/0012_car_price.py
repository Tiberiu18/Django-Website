# Generated by Django 3.2.6 on 2021-08-27 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_auto_20210820_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]