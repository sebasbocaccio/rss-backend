from os import link
from django.db import models
from django.contrib.auth.models import User




class SubscriptionFeeds(models.Model):
    users_subscribed = models.ManyToManyField(User)
    link = models.URLField(max_length=250)
    title = models.CharField(max_length=250)
    image = models.ImageField(null=True, blank = True)
    subscription_articles = models.ManyToManyField('Article')



