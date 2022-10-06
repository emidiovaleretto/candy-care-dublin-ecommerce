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
