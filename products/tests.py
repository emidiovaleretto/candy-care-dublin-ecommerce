from django.test import TestCase
from .models import Category, Product


class TestModelsCategory(TestCase):

    def test_create_new_product_category(self):
        Category.objects.create(name='Category 1')
        self.assertTrue(Category.objects.exists())

    def test_str_name_repr(self):
        entry = Category(name='Category 1')
        self.assertEqual(str(entry), entry.name)

    def test_verbose_name_plural(self):
        self.assertEqual(str(Category._meta.verbose_name_plural), "Categories")


class TestModelsProduct(TestCase):

    def test_create_new_product(self):
        Product.objects.create(
            name='Product 1',
            description='Testing Model Products',
            price=100
        )
        self.assertTrue(Product.objects.exists())

    def test_str_name_repr(self):
        entry = Category(name='Category 1')
        self.assertEqual(str(entry), entry.name)

    def test_instance_product(self):
        product = Product.objects.create(
            name='Product 1',
            description='Testing Model Products',
            price=100
        )
        self.assertIsInstance(product, Product)
