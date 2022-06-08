from products.models import *


class Category(models.Model):
    """
    This class is used to create a category.
    """

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """
        This method is used to return the name of the category.
        """
        return self.name

    def get_friendly_name(self):
        """
        This method is used to return the friendly name of the category.
        """
        return self.friendly_name
