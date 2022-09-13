from django.test import TestCase
from .models import Category, Product


class TestModelsCategory(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Category 1')
        self.category.save()

    def tearDown(self):
        self.category.delete()

    def test_create_new_product_category(self):
        self.assertTrue(self.category is not None)
        self.assertEqual(1, Category.objects.count())
        self.assertIsInstance(self.category, Category)

    def test_str_name_repr(self):
        self.assertEqual(str(self.category), self.category.name)

    def test_verbose_name_plural(self):
        self.assertEqual(str(self.category._meta.verbose_name_plural), "Categories")


class TestModelsProduct(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name='Product 1',
            description='Testing Model Products',
            price=100
        )
        self.product.save()

    def tearDown(self):
        self.product.delete()

    def test_create_new_product(self):
        self.assertTrue(self.product is not None)
        self.assertEqual(1, Product.objects.count())

    def test_str_name_repr(self):
        self.assertEqual(str(self.product), self.product.name)

    def test_instance_product(self):
        self.assertIsInstance(self.product, Product)
