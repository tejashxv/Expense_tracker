# Generated by Django 5.1.6 on 2025-02-25 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_alter_transaction_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
