# Generated by Django 4.0.3 on 2022-04-05 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserTransAPI', '0009_delete_hero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactions',
            name='id',
        ),
        migrations.AlterField(
            model_name='transactions',
            name='reference',
            field=models.CharField(max_length=255, primary_key=True, serialize=False, unique=True),
        ),
    ]
