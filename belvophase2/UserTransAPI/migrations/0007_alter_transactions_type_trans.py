# Generated by Django 4.0.3 on 2022-04-04 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserTransAPI', '0006_alter_transactions_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='type_trans',
            field=models.CharField(max_length=255),
        ),
    ]
