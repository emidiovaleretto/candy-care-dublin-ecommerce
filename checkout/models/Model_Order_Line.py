from django.db import models
from .Model_Order import Order

from products.models.Models_Product import Product


class OrderLineItem(models.Model):

    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    product = models.ForeignKey(
        Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, editable=False)

    def save(self, *args, **kwargs):
        """
        This function overrides the original save method to set
        the lineitem_total if it hasn't been set already.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU: {self.product.sku} on order {self.order.order_number}.'
