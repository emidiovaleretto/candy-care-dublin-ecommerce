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

    order_form = OrderForm()

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
