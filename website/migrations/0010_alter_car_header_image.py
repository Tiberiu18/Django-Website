# Generated by Django 3.2.6 on 2021-08-17 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_alter_car_header_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='header_image',
            field=models.ImageField(default='images/default-img.jpg', upload_to='images/'),
        ),
    ]
