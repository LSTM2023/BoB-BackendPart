# Generated by Django 3.2.20 on 2023-08-21 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lstm_api', '0015_user_token'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='token',
            new_name='ftoken',
        ),
    ]
