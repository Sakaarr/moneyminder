# Generated by Django 5.0.1 on 2024-02-25 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_saving_goal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='income_source',
        ),
    ]
