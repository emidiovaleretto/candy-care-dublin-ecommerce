from uuid import uuid4
from products.models import *

from django_resized import ResizedImageField


class Product(models.Model):
    """
    This class is used to create a product.
    """

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    occasion = models.ForeignKey(
        'Occasion', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(blank=True, max_length=254, null=True)
    name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=100, null=False, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = ResizedImageField(
        size=[640, 480],
        quality=75, 
        force_format='JPEG'
    )

    def __str__(self):
        """
        This method is used to return the name of the product.
        """
        return self.name
