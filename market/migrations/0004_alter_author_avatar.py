# Generated by Django 4.2.3 on 2023-07-30 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_author_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='avatar',
            field=models.ImageField(default='author_avatars/default_author.webp', upload_to='author_avatars'),
        ),
    ]
