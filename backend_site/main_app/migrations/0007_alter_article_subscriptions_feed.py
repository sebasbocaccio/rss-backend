# Generated by Django 3.2.4 on 2021-07-26 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20210726_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='subscriptions_feed',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.subscriptionfeeds'),
        ),
    ]