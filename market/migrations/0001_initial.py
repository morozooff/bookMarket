# Generated by Django 4.2.3 on 2023-07-15 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('biography', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('pages_num', models.IntegerField()),
                ('cost', models.IntegerField()),
                ('review', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.author')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('S', 'Started'), ('NP', 'Not paid'), ('C', 'Construct'), ('ID', 'In Delivery'), ('D', 'Delivered'), ('ND', 'Not Delivered')], default='S', max_length=2)),
                ('books', models.ManyToManyField(to='market.book')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('orders', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.order')),
            ],
        ),
    ]
