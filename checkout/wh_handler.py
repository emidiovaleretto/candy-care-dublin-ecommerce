from django.http import HttpResponse


class StripeWebHooksHandler:
    """ A class to handle Stripe WebHooks """

    def __init__(self, request):
        self.request = request

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
        print(payment_intent)
        return HttpResponse(
            content=f"Webhook has been received: {event['type']}",
            status=200
        )
