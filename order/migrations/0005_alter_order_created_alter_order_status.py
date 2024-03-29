# Generated by Django 4.2.3 on 2023-07-26 20:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_order_created_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 26, 20, 10, 1, 304335)),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('S', 'Формируется'), ('NP', 'Не оплачен'), ('C', 'Собран'), ('ID', 'В доставке'), ('D', 'Доставлен'), ('ND', 'Недоставлен')], default='S', max_length=100),
        ),
    ]
