
from django.shortcuts import render, redirect
from django.shortcuts import reverse, get_object_or_404

from django.http import HttpResponse
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


def update_shopping_bag(request, item_id):
    """ This function adjust the quantity of an specific product
        to the specific amount. """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))

    shopping_bag = request.session.get('shopping_bag', {})

    if quantity > 0:
        shopping_bag[item_id] = quantity
        messages.success(request,
                         f'Updated {product.name} '
                         f'quantity to {shopping_bag[item_id]}.')
    else:
        shopping_bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag.')

    request.session['shopping_bag'] = shopping_bag
    return redirect(reverse('shopping_bag'))


def remove_item_from_shopping_bag(request, item_id):
    """ This function removes an item from the shopping bag. """

    try:
        product = get_object_or_404(Product, pk=item_id)
        shopping_bag = request.session.get('shopping_bag', {})

        shopping_bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag.')

        request.session['shopping_bag'] = shopping_bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
