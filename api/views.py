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


@login_required(login_url='/auth/login')
def edit_all_products(request):
    """
    This method loads a list of
    all products available for editing.
    """
    products = Product.objects.all()

    context = {
        'products': products
    }

    return render(request, 'api/edit_products.html', context=context)


@login_required(login_url='/auth/login')
def edit_product(request, product_id):
    """
    This method edits a product in the store.
    """
    if not request.user.is_superuser:
        messages.error(request,
                       'It appears you tried to access a page that you do not have permission. \
                        Please contact the store owner for assistance.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'{product.name} updated successfully!')
            return redirect(reverse('product_detail', args=[product.slug]))
        else:
            messages.error(request,
                           'Something went wrong while trying to update your product. \
                            Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing [{product.name}]')

    context = {
        'form': form,
        'product': product,
    }

    return render(request, 'api/edit_product.html', context=context)


@login_required(login_url='/auth/login')
def delete_a_product(request, product_id):
    """
    This method deletes a product in the store.
    """
    if not request.user.is_superuser:
        messages.error(request,
                       "It looks like you tried to access a page for which you don't have permission. \
                        Please contact the store owner for assistance.")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.info(request, f"{product.name} deleted successfully!")

    return redirect(reverse('edit_all_products'))
