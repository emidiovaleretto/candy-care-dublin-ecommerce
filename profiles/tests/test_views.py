from django.test import TestCase
from django.contrib.auth.models import User


class TestViewAuthentication(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='test',
            password='12test12',
            email='test@test.com'
        )
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_user_exists_must_return_200(self):
        context = {
            'username': self.user.username,
            'password': self.user.password
        }

        response = self.client.post('/auth/login/', data=context)
        self.assertTrue(response)
        self.assertEqual(200, response.status_code)
