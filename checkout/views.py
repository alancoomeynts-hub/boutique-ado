from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51TxtN5D4MRC466FrHZaHl7U8JJRRiAZqofAFOKfdaSc3cavQbMKvo6P9ZN9ZOvNyBapUeY08gqCOrw5jfCRRQqxC00jWRs0kw1',
        'client_secret': 'test_secret_key'
    }

    return render(request, template, context)