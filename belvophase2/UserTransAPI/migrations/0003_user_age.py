# Generated by Django 4.0.3 on 2022-04-03 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserTransAPI', '0002_user_transactions'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]