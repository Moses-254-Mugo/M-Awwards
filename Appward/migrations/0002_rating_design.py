# Generated by Django 3.2.8 on 2021-10-23 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appward', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='design',
            field=models.IntegerField(default=1),
        ),
    ]
