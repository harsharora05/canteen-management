# Generated by Django 4.1.4 on 2023-04-07 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_no',
            field=models.IntegerField(),
        ),
    ]
