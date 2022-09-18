from django.test import TestCase
from django.urls import reverse


class TestShoppingBagViews(TestCase):

    def test_request_shopping_bag_must_return_200(self):
        response = self.client.get(reverse('shopping_bag'))
        self.assertEqual(response.status_code, 200)

    def test_template_used_in_shopping_bag(self):
        response = self.client.get(reverse('shopping_bag'))
        self.assertTemplateUsed('shopping_bag.html')
