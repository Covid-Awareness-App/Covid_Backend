# Generated by Django 3.1.7 on 2021-02-25 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(blank=True, default='Business Name', max_length=100)),
                ('business_img', models.TextField()),
                ('address', models.TextField()),
                ('hours', models.CharField(blank=True, default='Business Hours', max_length=100)),
                ('contact_number', models.CharField(blank=True, default='Business Contact Information', max_length=100)),
                ('offers', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='State Name', max_length=100)),
                ('img_icon', models.TextField()),
                ('average_daily_cases', models.IntegerField(default=1000)),
            ],
        ),
    ]
