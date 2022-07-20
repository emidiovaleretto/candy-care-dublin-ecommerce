from django.shortcuts import get_object_or_404
from django.conf import settings
from products.models import Product
from decimal import Decimal


def shopping_bag_contents(request):

    shopping_bag_items = []
    total = 0
    product_count = 0
    shopping_bag = request.session.get('shopping_bag', {})

    for item_id, item_data in shopping_bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            shopping_bag_items.append({
                'item_id': item_id,
                'product': product,
                'quantity': item_data,
            })
        
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total

    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'shopping_bag_items': shopping_bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'free_delivery_delta': free_delivery_delta,
        'grand_total': grand_total
    }

    return context