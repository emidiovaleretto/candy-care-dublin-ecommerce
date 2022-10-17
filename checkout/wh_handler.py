from django.http import HttpResponse
from django.template.loader import render_to_string

from django.core.mail import send_mail
from django.conf import settings

from .models import Order, OrderLineItem
from products.models import Product

from profiles.models.Models_Profile import UserProfile
from time import sleep

import json


class StripeWebHooksHandler:
    """ A class to handle Stripe WebHooks """

    def __init__(self, request):
        self.request = request

    def _send_email_confirmation(self, order):
        """
        This method sends the user a confirmation email.
        """
        customer_email = order.email
        from_email = settings.DEFAULT_FROM_EMAIL

        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})

        message = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(

            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=[
                customer_email,
            ],
            fail_silently=False
        )

    def handle_event(self, event):
        """
        This method handles a generic/unknown/
        unexpected webhook event
        """
        return HttpResponse(
            content=f"Webhook has been received: {event['type']}",
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        This method handles the payment_intent.succeeded
        webhook event from Stripe
        """

        payment_intent = event.data.object
        payment_id = payment_intent.id
        shopping_bag = payment_intent.metadata.shopping_bag
        save_info = payment_intent.metadata.save_info

        billing_details = payment_intent.charges.data[0].billing_details
        shipping_details = payment_intent.shipping

        grand_total = round(payment_intent.charges.data[0].amount / 100, 2)

        for field, value in shipping_details.address.items():
            if value == '':
                shipping_details.address[field] = None

        profile = None
        username = payment_intent.metadata.username

        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = shipping_details.phone,
                profile.default_country = shipping_details.address.country,
                profile.default_postcode = shipping_details.address.postal_code,
                profile.default_town_or_city = shipping_details.address.city,
                profile.default_street_address_1 = shipping_details.address.line1,
                profile.default_street_address_2 = shipping_details.address.line2,
                profile.default_county = shipping_details.address.state,
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address_1__iexact=shipping_details.address.line1,
                    street_address_2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_cart=shopping_bag,
                    stripe_payment_id=payment_id
                )

                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                sleep(1)

        if order_exists:
            self._send_email_confirmation(order)
            return HttpResponse(
                content=f'Webhook has been received: {event["type"]} '
                '| Success: verified order already in database',
                status=200
            )
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address_1=shipping_details.address.line1,
                    street_address_2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_cart=shopping_bag,
                    stripe_payment_id=payment_id
                )
                for item_id, item_data in json.loads(shopping_bag).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data
                        )
                        order_line_item.save()

            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook has been received: {event["type"]} | Error: {e}',
                    status=500
                )

        self._send_email_confirmation(order)
        return HttpResponse(
            content=f'Webhook has been received: {event["type"]} '
            '| Success: order created in webhook',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        This method handles the payment_intent.payment_failed
        webhook event from Stripe.
        """
        return HttpResponse(
            content=f'Webhook has been received: {event["type"]}',
            status=200
        )
