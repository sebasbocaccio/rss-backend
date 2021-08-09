from django.contrib.auth.models import User
from django.core.management import BaseCommand, CommandError
from django.core.management import call_command
from io import StringIO
from mock import patch
from rest_framework.test import APITestCase, APIClient

from ...auxiliary.exceptions.no_users_recieved_exception import NotUserReceived
from ...auxiliary.helpers.feed_helper import SubscriptionFeedHelper
from ...auxiliary.helpers.test_helper import TestUtils
from ...models.subscription_feed_model import SubscriptionFeeds


class ImportOPMLFileSubscription(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.test_helper = TestUtils()

    def test_command_raises_error_when_no_arguments_are_passed(self):
        try:
            call_command('import_subscriptions')
        except CommandError as error:
            self.assertEquals(error.args[0], 'Error: the following arguments are required: file')
        else:
            self.fail()

    def test_command_raises_error_when_there_is_not_any_user(self):
        try:
            call_command('import_subscriptions', 'main_app/tests/import_subscriptions_tests/one_feed.opml')
        except NotUserReceived as error:
            self.assertEquals(error.args[0], "Error: Any valid user had been passed")

    @patch.object(SubscriptionFeedHelper, 'parse_data')
    def test_command_create_subscription_for_existing_user_and_subscribe_user(self, url_parser):
        out = StringIO()
        url_parser.return_value = self.test_helper.false_subscription
        user = User.objects.create_user(username='username', password='password', email='email@email.com')
        call_command('import_subscriptions', 'main_app/tests/import_subscriptions_tests/one_feed.opml', 'username',stdout= out  )
        subscription = SubscriptionFeeds.objects.get()
        self.assertEqual(subscription.title, "Mom")
        self.assertNotEqual(SubscriptionFeeds.objects.first(), None)
        self.assertEqual(user in subscription.users_subscribed.all(), True)

    @patch.object(SubscriptionFeedHelper, 'parse_data')
    def test_command_not_create_subscription_if_user_is_not_registered(self, url_parser):
        url_parser.return_value = self.test_helper.false_subscription
        out = StringIO()
        try:
            call_command('import_subscriptions', 'main_app/tests/import_subscriptions_tests/one_feed.opml',
                         'not_registered_user', stdout=out)
        except NotUserReceived as error:
            out = out.getvalue()
            assert ('ERROR: not_registered_user is not registered so is not going to be add to any subscription' in out)
            self.assertEquals(error.args[0], "Error: Any valid user had been passed")
            self.assertEqual(len(SubscriptionFeeds.objects.all()), 0)
            self.assertEqual(len(User.objects.all()), 0)
        else:
            self.fail()

    @patch.object(SubscriptionFeedHelper, 'parse_data')
    def test_command_many_valid_users_can_subscribe_to_subscription(self, url_parser):
        url_parser.return_value = self.test_helper.false_subscription
        out = StringIO()
        user1 = User.objects.create_user(username='username1', password='password', email='email1@email.com')
        user2 = User.objects.create_user(username='username2', password='password', email='email2@email.com')
        user3 = User.objects.create_user(username='username3', password='password', email='email3@email.com')
        users = ['username1', 'username2', 'username3']
        call_command('import_subscriptions', 'main_app/tests/import_subscriptions_tests/one_feed.opml',
                     users, stdout=out)

        subscription = SubscriptionFeeds.objects.get()
        user_subscribed = list(subscription.users_subscribed.all())
        out = out.getvalue()
        assert ((user1 in user_subscribed) and (user2 in user_subscribed) and (user2 in user_subscribed))
        assert ('Successfully added user "username1" to subscription' in out)
        assert ('Successfully added user "username2" to subscription' in out)
        assert ('Successfully added user "username3" to subscription' in out)

    @patch.object(SubscriptionFeedHelper, 'parse_data')
    def test_user_can_not_subscribe_twice_to_a_subscription_using_command(self, url_parser):
        url_parser.return_value = self.test_helper.false_subscription
        out = StringIO()
        User.objects.create_user(username='username', password='password', email='email@email.com')
        call_command('import_subscriptions', 'main_app/tests/import_subscriptions_tests/one_feed.opml','username',stdout =out)
        call_command('import_subscriptions', 'main_app/tests/import_subscriptions_tests/one_feed.opml', 'username',
                     stdout=out)
        out = out.getvalue()
        assert('ERROR: User is already subscribed to that page' in out)