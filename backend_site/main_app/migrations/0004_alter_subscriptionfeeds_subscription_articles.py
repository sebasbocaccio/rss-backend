# Generated by Django 3.2.4 on 2021-07-26 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20210726_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionfeeds',
            name='subscription_articles',
            field=models.ManyToManyField(to='main_app.Article'),
        ),
    ]