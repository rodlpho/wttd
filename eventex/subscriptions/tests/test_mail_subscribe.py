from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Henrique Bastos', cpf='12345678901',
                    email='rodolphodeales@gmail.com', phone='21-11111-1111')

        self.resp = self.client.post('/inscricao/',data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expected = 'Confirmação de inscrição'
        self.assertEqual(expected, self.email.subject)

    def test_subscription_email_from(self):
        expected = 'rodolphodeales@gmail.com'

        self.assertEqual(expected, self.email.from_email)

    def test_subscription_email_to(self):
        expected = ['rodolphodeales@gmail.com', 'rodolphodeales@gmail.com']

        self.assertEqual(expected, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Henrique Bastos',
            '12345678901',
            'rodolphodeales@gmail.com',
            '21-11111-1111',

        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
