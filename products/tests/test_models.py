from django.test import TestCase
from ..models import Category, Product, Occasion


class TestModelsCategory(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='category_1')
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
        self.assertEqual(
            str(self.category._meta.verbose_name_plural), "Categories")


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


class TestModelsOccasion(TestCase):

    def setUp(self):
        self.occasion = Occasion.objects.create(
            name='mothers_day',
            friendly_name="Mother's Day"
        )
        self.occasion.save()

    def tearDown(self):
        self.occasion.delete()

    def test_create_new_occasion(self):
        self.assertEqual(1, Occasion.objects.count())
        self.assertEqual(self.occasion.name, 'mothers_day')
        self.assertTrue(self.occasion)

    def test_str_name_repr(self):
        self.assertEqual(str(self.occasion), self.occasion.name)

    def test_instance_of_occasion(self):
        self.assertIsInstance(self.occasion, Occasion)
