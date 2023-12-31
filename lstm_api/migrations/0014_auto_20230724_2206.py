# Generated by Django 3.2.20 on 2023-07-24 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lstm_api', '0013_healthcheck_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='qaAnswer',
            field=models.TextField(blank=True, null=True, verbose_name='질문 답안'),
        ),
        migrations.AddField(
            model_name='user',
            name='qatype',
            field=models.IntegerField(blank=True, null=True, verbose_name='질문 타입'),
        ),
        migrations.AlterField(
            model_name='growthlog',
            name='date',
            field=models.DateField(verbose_name='날짜'),
        ),
    ]
