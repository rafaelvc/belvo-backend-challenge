# Generated by Django 4.0.3 on 2022-04-04 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserTransAPI', '0004_transactions_amount_transactions_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='category',
            field=models.CharField(max_length=255),
        ),
    ]