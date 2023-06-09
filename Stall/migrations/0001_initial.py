# Generated by Django 4.1.4 on 2023-05-18 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('canteenStallName', models.CharField(max_length=50)),
                ('StallDesc', models.CharField(default='', max_length=20)),
                ('StallImg', models.ImageField(default='', upload_to='StallImage')),
                ('Url', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(default='', max_length=50)),
                ('productDesc', models.CharField(default='', max_length=300)),
                ('category', models.CharField(default='', max_length=50)),
                ('publishDate', models.DateField()),
                ('price', models.IntegerField(default='')),
                ('productImg', models.ImageField(default='', upload_to='ProductImage')),
                ('StallName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Stall.stall')),
            ],
        ),
    ]
