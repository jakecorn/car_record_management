# Generated by Django 3.0.5 on 2020-04-28 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0003_carsequence'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='sequence',
        ),
    ]
