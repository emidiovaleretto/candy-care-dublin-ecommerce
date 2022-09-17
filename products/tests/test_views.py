from django.test import TestCase
from django.urls import reverse
from ..views import list_all_products, product_detail


class TestProductViews(TestCase):

    def test_list_all_products_views_must_return_200(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)

    def test_template_used_in_list_all_products_views(self):
        response = self.client.get(reverse('products'))
        self.assertTemplateUsed('products.html')

    def test_template_used_in_product_detail_views(self):
        response = self.client.get(1)
        self.assertTemplateUsed('product_detail.html')