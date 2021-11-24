'''
Creates views for checkout app
'''
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing in your bag")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JjikvFmWTEbwtxzDWZCRK1xBMVFA745dxAf3iwxhyknhpdJOZoKwr6MUOo1Yk1OO64HOLdel30yV2CuMrlZ2V7v00XDVgIPHl',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
