# Generated by Django 4.1.7 on 2023-04-01 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='image',
            field=models.ImageField(default='image', upload_to='images'),
            preserve_default=False,
        ),
    ]