# Generated by Django 4.1.7 on 2023-03-31 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lstm_api', '0003_user_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='relation',
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default='', max_length=100),
        ),
    ]
