# Generated by Django 4.2.3 on 2023-07-30 21:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_alter_order_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 30, 21, 10, 28, 420069)),
        ),
    ]