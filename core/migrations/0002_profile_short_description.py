# Generated by Django 2.1 on 2018-08-18 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='short_description',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]