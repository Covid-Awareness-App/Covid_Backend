# Generated by Django 3.1.7 on 2021-03-01 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('covidapp', '0003_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='address',
        ),
        migrations.AlterField(
            model_name='feedback',
            name='business_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to='covidapp.location'),
        ),
    ]