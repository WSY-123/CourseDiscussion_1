# Generated by Django 3.0.5 on 2020-05-30 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0006_auto_20200530_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='credit',
            field=models.FloatField(default=2.0),
        ),
    ]
