# Generated by Django 3.2.6 on 2021-08-15 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_car_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='header_image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
