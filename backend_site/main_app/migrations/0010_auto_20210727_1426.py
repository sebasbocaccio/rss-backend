# Generated by Django 3.2.4 on 2021-07-27 14:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_alter_userarticle_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='date_time',
        ),
        migrations.AddField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 27, 14, 26, 11, 519242, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='subscriptionfeeds',
            name='link',
            field=models.URLField(max_length=250, unique=True),
        ),
    ]