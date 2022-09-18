
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from products.models import Product


def view_shopping_bag(request):
    """ This function renders the cart content. """
    return render(request, 'shopping_bag/shopping_bag.html')


def add_to_shopping_bag(request, item_id):
    """ This function add a quantity of an specific product
        to the shopping bag. """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    shopping_bag = request.session.get('shopping_bag', {})

    if item_id in list(shopping_bag.keys()):
        shopping_bag[item_id] += quantity
        messages.success(request,
                         f'Updated {product.name} '
                         f'quantity to {shopping_bag[item_id]}.')
    else:
        shopping_bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag.')

    request.session['shopping_bag'] = shopping_bag
    return redirect(redirect_url)
