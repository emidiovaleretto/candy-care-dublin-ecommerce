from django.shortcuts import (
    render, get_object_or_404, reverse, redirect)
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from products.models.Models_Product import Product
from products.forms import ProductForm


@login_required(login_url='/auth/login')
def management(request):
    """
    This method loads the management page.
    """
    return render(request, 'api/management.html')


@login_required(login_url='/auth/login')
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
    return render(request, 'api/add_product.html', context=context)
