# Generated by Django 3.2.18 on 2023-04-10 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lstm_api', '0006_alter_userbabyrelationship_relation'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbabyrelationship',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
