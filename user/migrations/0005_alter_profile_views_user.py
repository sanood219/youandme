# Generated by Django 4.0.5 on 2022-06-10 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_profile_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_views',
            name='user',
            field=models.CharField(max_length=250),
        ),
    ]
