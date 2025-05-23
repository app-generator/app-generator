import json
import stripe
from django.shortcuts import render, redirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from apps.payments.models import Purchase
from apps.common.models import Products
from django.core.mail import send_mail

stripe.api_key = settings.STRIPE_SECRET_KEY
hosting_price = settings.HOSTING_PRICE

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        basket = data.get('basket', [])
        hosting = data.get('hosting', '0')

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

        if hosting == '1':
            line_items.append({
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': '1 year hosting',
                    },
                    'unit_amount': int((hosting_price * 12) * 100),
                },
                'quantity': 1,
            })

        user_email = request.user.email if request.user.is_authenticated and request.user.email else None
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            metadata = {
                'user_id': request.user.id if request.user.is_authenticated else -1,
                'products': ','.join(str(item['id']) for item in basket),
                'hosting': hosting
            },
            success_url=request.build_absolute_uri('/success/') + '?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=request.build_absolute_uri('/cancel/'),
            customer_email=user_email,
        )

        return JsonResponse({'url': session.url})


def success(request):
    session_id = request.GET.get('session_id')
    hosting = False
    products = []

    session = None
    if session_id:
        session = stripe.checkout.Session.retrieve(session_id)

    if session:
        user_id = session['metadata']['user_id']
        hosting = session['metadata']['hosting'] == '1'
        products = session['metadata']['products']
        customer_email = session.get('customer_details', {}).get('email')
        total = session['amount_total'] / 100

        purchase, created = Purchase.objects.get_or_create(
            purchase_id=session_id,
            defaults={
                'user_id': user_id,
                'email': customer_email,
                'purchase_value': total,
                'hosting_price': (hosting_price * 12) if hosting else 0,
            }
        )
        if created:
            product_ids = [int(pid) for pid in products.split(',') if pid]
            products = Products.objects.filter(id__in=product_ids)
            purchase.products.set(product_ids)
            purchase.save() 

        product_list = ""

        for product in products:
            product_list += f"- {product.name}\n"
        
        if hosting:
            product_list += "- 1 year hosting.\n"

        subject = f"New Stripe Purchase - ${total} | {customer_email}"
        message = (
            "The purchase details\n"
            f"{product_list}"
        )

        send_mail(
            subject,
            message,
            getattr(settings, 'EMAIL_HOST_USER'),
            [getattr(settings, 'EMAIL_HOST_USER')],
            fail_silently=False,
        )

    context = {
        'page_title': 'Payment success',
        'hosting': hosting,
        'products': products

    }
    return render(request, 'payments/success.html', context)


def cancel(request):
    context = {
        'page_title': 'Payment cancelled',
    }
    return render(request, 'payments/cancel.html', context)