# Generated by Django 3.1.7 on 2021-02-25 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('covidapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='covidapp.state'),
        ),
    ]