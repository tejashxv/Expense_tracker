# Generated by Django 5.1.6 on 2025-02-25 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_remove_transaction_id_alter_transaction_uuid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ('description',)},
        ),
    ]
