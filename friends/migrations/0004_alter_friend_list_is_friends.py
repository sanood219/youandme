# Generated by Django 4.0.5 on 2022-06-08 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0003_remove_friend_request_accepted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend_list',
            name='is_friends',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
