# Generated by Django 3.2.18 on 2023-03-17 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lstm_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbabyrelationship',
            name='relation',
            field=models.CharField(blank=True, default='N', max_length=1, null=True),
        ),
    ]