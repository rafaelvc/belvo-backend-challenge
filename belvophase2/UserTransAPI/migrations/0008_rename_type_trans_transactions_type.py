# Generated by Django 4.0.3 on 2022-04-04 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserTransAPI', '0007_alter_transactions_type_trans'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transactions',
            old_name='type_trans',
            new_name='type',
        ),
    ]
