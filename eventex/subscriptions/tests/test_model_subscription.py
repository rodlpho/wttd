from datetime import datetime
from django.test import TestCase
from eventex.subscriptions.models import Subscription
from django.shortcuts import resolve_url as r


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Rodolpho Pinto',
            cpf='13245678935',
            email='test@rodolpho.com',
            phone='19-999999999'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created at attribute."""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Rodolpho Pinto', str(self.obj))

    def test_paid_default_to_False(self):
        """By default paid must be False"""
        self.assertFalse(self.obj.paid)

    def test_get_absolute_url(self):
        url = r('subscriptions:detail', self.obj.hash_url)
        self.assertEqual(url, self.obj.get_absolute_url())
