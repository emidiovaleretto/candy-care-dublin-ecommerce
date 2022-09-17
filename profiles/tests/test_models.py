from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from ..models import Models_Profile


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
        self.assertTrue(self.user)
        self.assertIsInstance(self.user, User)
        self.assertEqual(1, User.objects.count())
        self.assertIsNotNone(self.user)


class TestModelsProfile(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='test',
            password='12test12',
            email='test@test.com'
        )
        self.user.save()

        self.profile = Models_Profile.UserProfile(user=self.user)

    def tearDown(self):
        self.user.delete()

    def test_profile_creation(self):
        self.assertTrue(self.profile)
        self.assertIsInstance(self.profile, Models_Profile.UserProfile)
        self.assertEqual(1, Models_Profile.UserProfile.objects.count())
        self.assertIsNotNone(self.profile)


class TestSignin(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='test',
            password='12test12',
            email='test@test.com'
        )
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_user_is_authenticated_must_return_true(self):
        self.assertTrue((self.user is not None) and self.user.is_authenticated)

    def test_user_signin_with_wrong_username_must_return_false(self):
        user = authenticate(username='test_wrong_username',
                            password='12test12')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_user_signin_with_wrong_password_must_return_false(self):
        user = authenticate(username='test', password='wrong password')
        self.assertFalse((user is not None) and user.is_authenticated)
