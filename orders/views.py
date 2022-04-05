from locale import currency
from django.shortcuts import render,redirect
from django.urls import reverse
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.conf import settings
import stripe

stripe.api_key=settings.STRIPE_SECRET_KEY


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        charge=stripe.Charge.create(
            amount='{:.0f}'.format(cart.get_total_price()*100),
            currency='usd',
            description='payer par carte credit',
            source=request.POST['stripeToken']
        )
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=True)
            order.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
            request.session.modeified=True

            order.paid=True
            order.save()
            return redirect('payement:done')
        else:
            return redirect('payement:canceled')
    else:
        form = OrderCreateForm()
        key=settings.STRIPE_PUBLIC_KEY
    return render(request, 'orders/order/create.html', {'cart':cart,'key':key,'form': form})
