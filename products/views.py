from django.shortcuts import render


def list_all_products(request):
    """
    This method is used to list all products.
    """
    return render(request, 'products/products.html')
