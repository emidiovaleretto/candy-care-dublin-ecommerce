from django.contrib import admin
from .models import *
# Register your models here.
class ShoppingBagAdmin(admin.ModelAdmin):
    list_display=('user', 'created_at', 'updated_at', )
    ordering = ('user',)

class ShoppingBagItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'shopping_bag')


admin.site.register(ShoppingBag,ShoppingBagAdmin)
admin.site.register(ShoppingBagItem,ShoppingBagItemAdmin)