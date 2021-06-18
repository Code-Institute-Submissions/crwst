from django.shortcuts import render, redirect, reverse
from django.contrib import messages
<<<<<<< HEAD
from django.conf import settings
=======
>>>>>>> cb8bce38622265c7383bf087edd6eef0a869585d

from .forms import OrderForm


def checkout(request):
<<<<<<< HEAD
    """
    Checks order form is valid
    Checks items in bag are valid and in database
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY

=======
>>>>>>> cb8bce38622265c7383bf087edd6eef0a869585d
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
<<<<<<< HEAD
        'stripe_public_key': stripe_public_key,
        'client_secret': 'test client secret',
=======
>>>>>>> cb8bce38622265c7383bf087edd6eef0a869585d
    }

    return render(request, template, context)
