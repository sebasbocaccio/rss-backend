# Generated by Django 3.2.4 on 2021-07-20 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_subscriptionfeeds_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionfeeds',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
