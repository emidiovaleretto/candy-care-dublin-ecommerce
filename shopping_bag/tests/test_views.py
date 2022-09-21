from django.test import TestCase
from django.urls import reverse

from products.models import Product


class TestShoppingBagViews(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name='Test',
            description='This is a test',
            price=100.00
        )
        self.product.save()

    def tearDown(self):
        self.product.delete()

    def test_request_shopping_bag_must_return_200(self):
        response = self.client.get(reverse('shopping_bag'))
        self.assertEqual(response.status_code, 200)

    def test_template_used_in_shopping_bag(self):
        response = self.client.get(reverse('shopping_bag'))
        self.assertTemplateUsed('shopping_bag.html')

    def test_add_a_single_item_to_shopping_bag(self):
        shopping_bag = self.client.session.get('shopping_bag', {
            'product': self.product
        })
        self.client.session['shopping_bag'] = shopping_bag

        self.assertEqual(len(shopping_bag.keys()), 1)
        self.assertTrue(shopping_bag is not None)
