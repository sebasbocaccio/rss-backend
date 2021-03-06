# Generated by Django 3.2.4 on 2021-07-26 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_subscriptionfeeds_subscription_articles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='subscriptions_feed',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main_app.subscriptionfeeds'),
        ),
        migrations.AlterField(
            model_name='subscriptionfeeds',
            name='subscription_articles',
            field=models.ManyToManyField(default=None, to='main_app.Article'),
        ),
    ]
