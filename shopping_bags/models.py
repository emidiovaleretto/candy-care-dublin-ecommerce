from django.db import models
from django.contrib.auth.models import User
from products.models.Models_Product import Product
from django.core.validators import MinValueValidator

# Create your models here.

class ShoppingBag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'user: {self.user}, updated_at: {self.updated_at}, created_at: {self.created_at}'


    @property
    def items(self):
        return ShoppingBagItem.objects.filter(shopping_bag = self.id)


    @property
    def total_price(self):
        return sum(el.total_price for el in self.items)


class ShoppingBagItem(models.Model):
    product = models.ForeignKey(Product, on_delete = models.SET_NULL, null= True)
    quantity = models.PositiveIntegerField(default = 1, validators = [MinValueValidator(limit_value=1,message="Quantity can not be less than 1!")])
    shopping_bag = models.ForeignKey(ShoppingBag,on_delete=models.CASCADE)

    def __str__(self):
        return f'product: {self.product.name}, quantity: {self.quantity}, shopping bag:{self.shopping_bag}'



    @property
    def total_price(self):
        return self.quantity*self.product.price
