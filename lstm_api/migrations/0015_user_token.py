# Generated by Django 3.2.20 on 2023-08-21 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lstm_api', '0014_auto_20230724_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.TextField(blank=True, null=True, verbose_name='firebase 토큰'),
        ),
    ]
