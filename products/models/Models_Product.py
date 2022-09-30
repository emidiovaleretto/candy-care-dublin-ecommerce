from uuid import uuid4
from products.models import *


class Product(models.Model):
    """
    This class is used to create a product.
    """

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    occasion = models.ForeignKey(
        'Occasion', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=100, null=False, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        """
        This method is used to return the name of the product.
        """
        return self.name
