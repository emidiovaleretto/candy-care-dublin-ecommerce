from django.shortcuts import (
    render, redirect, get_object_or_404, reverse)
from django.db.models.functions import Lower
from django.contrib import messages

from .models.Models_Product import Product
from .models.Models_Occasion import Occasion
from .forms import ProductForm


def list_all_products(request):
    """ 
    This function list all products,
    including sorting 
    """

    products = Product.objects.all()
    occasions = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'occasion' in request.GET:
            occasion = request.GET['occasion']
            products = products.filter(occasion__name__icontains=occasion)
            occasions = Occasion.objects.filter(name__icontains=occasion)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'current_occasions': occasions,
        'current_sorting': current_sorting
    }

    return render(request, 'products/products.html', context=context)


def product_detail(request, slug):
    """ 
    This function returns an individual product by its slug 
    """

    product = get_object_or_404(Product.objects.filter(slug=slug))
    suggestions = Product.objects.exclude(slug=slug)[:4]

    context = {
        'product': product,
        'suggestions': suggestions
    }

    return render(request, 'products/product_detail.html', context=context)
