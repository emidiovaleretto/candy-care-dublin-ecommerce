from django.shortcuts import (render, redirect,
                              reverse, get_object_or_404)
from django.contrib import messages

from django.conf import settings
from django.views.decorators.http import require_POST

from django.http import HttpResponse
from .forms import OrderForm

from .models import Order, OrderLineItem
from products.models import Product

from profiles.models.Models_Profile import UserProfile
from profiles.forms import UserProfileForm

from shopping_bag.contexts import shopping_bag_contents

import stripe
import json


def checkout(request):

    stripe_publishable_key = settings.STRIPE_PUBLISHABLE_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        shopping_bag = request.session.get('shopping_bag', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address_1': request.POST['street_address_1'],
            'street_address_2': request.POST['street_address_2'],
            'town_or_city': request.POST['town_or_city'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)

        if order_form.is_valid():

            order = order_form.save(commit=False)
            payment_id = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_payment_id = payment_id
            order.original_bag = json.dumps(shopping_bag)
            order.save()

            for item_id, item_data in shopping_bag.items():
                try:
                    product = get_object_or_404(Product, pk=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data
                        )
                        order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request,
                                   "One of the products in your bag wasn't "
                                   "found in our database. "
                                   "Please call us for assistance!")
                    order.delete()
                    return redirect(reverse('shopping_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(
                reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(
                request,
                'Something went wrong while trying to submit your form. '
                'Please double check your information.')
    else:

        shopping_bag = request.session.get('shopping_bag', {})

        if not shopping_bag:
            messages.error(
                request, "There's nothing in your bag at the moment.")
            return redirect(reverse('products'))

        current_bag = shopping_bag_contents(request)
        total = current_bag['grand_total']

        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key

        payment_intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address_1': profile.default_street_address_1,
                    'street_address_2': profile.default_street_address_2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

        if not stripe_publishable_key:
            messages.warning(
                request,
                'Stripe public key is missing. '
                'Did you forget to set it in your environment?'
            )

    context = {
        'order_form': order_form,
        'stripe_publishable_key': stripe_publishable_key,
        'client_secret': payment_intent.client_secret,
    }

    return render(request, 'checkout/checkout.html', context=context)


def checkout_success(request, order_number):
    """
    This function handles successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address_1': order.street_address_1,
                'default_street_address_2': order.street_address_2,
                'detaul_county': order.county,
            }

            user_profile_form = UserProfileForm(profile_data, instance=profile)

            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(
        request,
        f'Order successfully processed! '
        f'Your order number is {order_number}. '
        f'A email confirmation will be sent to "{order.email}".')

    if 'shopping_bag' in request.session:
        del request.session['shopping_bag']

    context = {
        'order': order,
    }

    return render(request, 'checkout/checkout_success.html', context=context)

    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'shopping_bag' in request.session:
        del request.session['shopping_bag']

    context = {
        'order': order,
    }

    return render(request, 'checkout/checkout_success.html', context=context)