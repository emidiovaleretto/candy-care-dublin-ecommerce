from django.test import TestCase
from django.contrib.auth.models import User


class TestModelsUser(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='test',
            password='12test12',
            email='test@test.com'
        )
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_create_new_user(self):
        user = User(
            username='test',
            password='12test12',
            email='test@test.com'
        )
        self.assertTrue(user)
        self.assertIsInstance(user, User)
        self.assertEqual(1, User.objects.count())
        self.assertIsNotNone(user)
