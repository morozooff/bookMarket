# Generated by Django 4.2.3 on 2023-07-26 11:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_delete_order'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created',), 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='books',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_id',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='Moscow', max_length=250),
        ),
        migrations.AddField(
            model_name='order',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 26, 11, 8, 1, 389226)),
        ),
        migrations.AddField(
            model_name='order',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='postal_code',
            field=models.CharField(default='aboba', max_length=20),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.PositiveIntegerField()),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='market.book')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='order.order')),
            ],
        ),
    ]
