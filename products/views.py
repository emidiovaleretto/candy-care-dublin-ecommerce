from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.db.models.functions import Lower

from .models.Models_Product import Product


def list_all_products(request):
    """ This function list all products,
        including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
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

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']

            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting
    }

    return render(request, 'products/products.html', context=context)


def product_detail(request, product_id):
    """ This function returns an individual product by its id """

    product = get_object_or_404(Product, pk=product_id)
    suggestions = Product.objects.exclude(pk=product_id)[:4]

    context = {
        'product': product,
        'suggestions': suggestions
    }

    return render(request, 'products/product_detail.html', context=context)
