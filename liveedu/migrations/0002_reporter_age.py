# Generated by Django 2.1.2 on 2018-10-10 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liveedu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporter',
            name='age',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
