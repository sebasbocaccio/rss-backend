import argparse
import sys
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from rest_framework.serializers import ValidationError
from termcolor import colored
from xml.etree import ElementTree

from ...auxiliary.helpers.feed_helper import SubscriptionFeedHelper


class Command(BaseCommand):
    help = 'Parse OPML file with subscriptions and add users to them.'
    def add_arguments(self, parser):
        parser.add_argument('file', type=str)
        parser.add_argument('users', nargs='+', type=str, default = [])

    def handle(self, *args, **options):
        users = self.getUser(options['users'])
        file = options['file']
        feeds = self.OPML_parse(file)
        subscription_helper = SubscriptionFeedHelper()
        for feed in feeds:
            self.stdout.write('Adding users to subscription %s' % feed)
            for user in users:
                try:
                    self.add_user_to_subscription(feed, subscription_helper, user)
                except ValidationError as error:
                    self.stdout.write(self.style.ERROR('ERROR: %s' %error.detail['message']))
                except Exception as error:
                    self.stdout.write(self.style.ERROR('ERROR: %s' %error))
                else:
                    self.stdout.write(self.style.SUCCESS('Successfully added user "%s" to subscription ' %user))

    def add_user_to_subscription(self, feed, subscription_helper, user):
        self.stdout.write('Adding %s to subscription' %user.username)
        data = {'link': feed}
        subscription_helper.create_feed(data, user)

    def OPML_parse(self, file):
        urls = []
        with open(file, 'rt') as f:
            tree = ElementTree.parse(f)
        for node in tree.findall('.//outline'):
            url = node.attrib.get('xmlUrl')
            if url:
                urls.append(url)
        return urls

    def getUser(self, usernames):
        users = []
        self.stdout.write('Starting to retrieve users from database')
        for user in usernames:
            try:
                user = User.objects.get(username=user)
                users.append(user)
            except:
                self.stdout.write(self.style.ERROR('ERROR: %s is not registered so is not going to be add to any subscription' %user))

        self.stdout.write('Retrieving users completed')
        return users
