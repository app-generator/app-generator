import json
import stripe
from django.shortcuts import render, redirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from apps.payments.models import Purchase

stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        basket = data.get('basket', [])

        line_items = []
        for item in basket:
            line_items.append({
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item['name'],
                    },
                    'unit_amount': int(item['price'] * 100),
                },
                'quantity': 1,
            })

        user_email = request.user.email if request.user.is_authenticated else None
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            metadata = {
                'user_id': request.user.id if request.user.is_authenticated else -1,
                'products': ','.join(str(item['id']) for item in basket)
            },
            success_url=request.build_absolute_uri('/success/') + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=request.build_absolute_uri('/cancel/'),
            customer_email=user_email,
        )

        return JsonResponse({'url': session.url})


def success(request):
    session_id = request.GET.get('session_id')
    session = None
    if session_id:
        session = stripe.checkout.Session.retrieve(session_id)
    
    if session:
        user_id = session['metadata']['user_id']
        customer_email = session['customer_details']['email']
        total = session['amount_total'] / 100

        Purchase.objects.get_or_create(
            purchase_id=session_id,
            defaults={
                'user_id': user_id,
                'email': customer_email,
                'purchase_value': total,
            }
        )

    context = {
        'page_title': 'Payment success',
    }
    return render(request, 'payments/success.html', context)


def cancel(request):
    context = {
        'page_title': 'Payment cancelled',
    }
    return render(request, 'payments/cancel.html', context)