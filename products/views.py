from django.shortcuts import (
    render, redirect, get_object_or_404, reverse)
from django.db.models.functions import Lower
from django.contrib import messages

from .models.Models_Product import Product
from .forms import ProductForm


def list_all_products(request):
    """ 
    This function list all products,
    including sorting 
    """

    products = Product.objects.all()
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

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
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


def management(request):
    """
    This method loads the management page.
    """
    return render(request, 'products/management.html')


def add_product(request):
    """
    This method adds a product to the store.
    """
    if not request.user.is_superuser:
        messages.error(request,
                       'It appears you tried to access a page that you do not have permission. \
                        Please contact the store owner for assistance.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.slug]))
        else:
            messages.error(
                request,
                'Something went wrong while trying to add a product. '
                'Please ensure the form is valid.')
    else:
        form = ProductForm()

    context = {
        'form': form,
    }
    return render(request, 'products/add_product.html', context=context)
