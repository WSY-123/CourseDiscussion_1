# Generated by Django 3.0.5 on 2020-05-15 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_lessons_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='number',
            field=models.CharField(max_length=10),
        ),
    ]
