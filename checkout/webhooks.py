from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from checkout.webhook_handler import StripeWH_Handler

import stripe
import sys


@require_POST
@csrf_exempt
def webhook(request):
    print("Webhook")
    sys.stdout.flush()
    """ Listen to webhooks from Stripe """
    # Setup
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY
    print("Webhook 2")
    sys.stdout.flush()
    # Get the webhook data and verify its signature
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    print("Webhook 3")
    sys.stdout.flush()
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        print("Webhook 4")
        sys.stdout.flush()
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        print("Webhook 5")
        sys.stdout.flush()
        return HttpResponse(status=400)
    except Exception as e:
        print("Webhook 6")
        sys.stdout.flush()
        return HttpResponse(content=e, status=400)

    # Set up a webhook handler
    print("Webhook 7")
    sys.stdout.flush()
    handler = StripeWH_Handler(request)
    print("Webhook 8")
    sys.stdout.flush()
    # Map webhook events to relevant handler functions
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_payment_failed,
    }
    print("Webhook 9")
    sys.stdout.flush()
    # Get the webhook type from Stripe
    event_type = event['type']

    # If there is a handler for it, get it from the event map
    # Use the generic one by default
    print("Webhook 10")
    sys.stdout.flush()
    event_handler = event_map.get(event_type, handler.handle_event)
    print("Webhook 11")
    sys.stdout.flush()
    # Call the event handler with the event
    response = event_handler(event)
    return response
