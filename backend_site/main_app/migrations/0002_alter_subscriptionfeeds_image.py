# Generated by Django 3.2.4 on 2021-07-18 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionfeeds',
            name='image',
            field=models.ImageField(upload_to='photos'),
        ),
    ]