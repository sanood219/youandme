# Generated by Django 4.0.5 on 2022-06-08 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_friendrequest_friend_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friendrequest',
            name='from_user',
        ),
        migrations.RemoveField(
            model_name='friendrequest',
            name='to_user',
        ),
        migrations.DeleteModel(
            name='Friend_list',
        ),
        migrations.DeleteModel(
            name='FriendRequest',
        ),
    ]
