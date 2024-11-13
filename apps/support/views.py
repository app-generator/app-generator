from django.shortcuts import render, redirect, get_object_or_404
from apps.support.forms import TicketForm, CommentForm
from apps.common.models import Ticket, StateChoices, PriorityChoices, Comment, Products
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def create_support_ticket(request):
    product_id = request.GET.get('product')
    initial_data = {}

    if product_id:
        product = get_object_or_404(Products, pk=product_id)
        initial_data['product'] = product

    form = TicketForm(initial=initial_data)

    if request.user.is_authenticated and request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.custom_development = True if request.GET.get('custom_development') == '1' else False
                    
            if request.user.profile.pro:
                ticket.priority = PriorityChoices.HIGH
            ticket.save()
            return redirect(request.META.get('HTTP_REFERER'))

    context = {
        'form': form,
        'segment': 'create_ticket',
        'parent': 'support',
        'page_title': 'Dashboard - Create Ticket',
    }

    if not request.user.is_authenticated:
        messages.error(request, "You're not authenticated. Please Sign IN")

    return render(request, 'dashboard/tickets/create.html', context)

@staff_member_required(login_url='/admin/')
def all_tickets(request):
    filter_string = {}
    if search := request.GET.get('search'):
        filter_string['title__icontains'] = search

    sort = request.GET.get('sort')
    if sort == 'high':
        order_by = '-priority'
    elif sort == 'low':
        order_by = 'priority'
    else:
        order_by = '-created_at'

    tickets = Ticket.objects.filter(**filter_string).order_by(order_by)

    page_number = request.GET.get('page', 1) 
    paginator = Paginator(tickets, 10)
    try:
        tickets = paginator.page(page_number)
    except PageNotAnInteger:
        tickets = paginator.page(1)
    except EmptyPage:
        tickets = paginator.page(paginator.num_pages)

    context = { 
        'tickets': tickets,
        'segment': 'all_tickets',
        'parent': 'support',
        'page_title': 'Dashboard - All Tickets',
    }
    return render(request, 'dashboard/tickets/all-tickets.html', context)


@login_required(login_url='/users/signin/')
def comment_to_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    comments = Comment.objects.filter(ticket=ticket).order_by('-created_at')
    form = CommentForm(user=request.user)

    if request.method == 'POST':
        form = CommentForm(request.POST, user=request.user)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.ticket = ticket
            comment.save()

            if ticket.user == request.user:
                ticket.states = StateChoices.CLIENT_REPLY
                email = ticket.user.profile.email
            else:
                ticket.states = request.POST.get('state', StateChoices.ANSWERED)
                email = getattr(settings, 'EMAIL_HOST_USER')
                
            ticket.save()

            subject = f"App-Generator: {ticket.title}"
            ticket_link = request.build_absolute_uri(reverse('comment_to_ticket', args=[ticket.pk]))
            message = (
                "Hello,\n\n"
                "Your issue has been updated.\n"
                f"Please check the status by accessing this link:\n{ticket_link}\n\n"
                "Thank you!\n"
                "< App-Generator.dev > Support"
            )
            send_mail(
                subject,
                message,
                getattr(settings, 'EMAIL_HOST_USER'),
                [email],
                fail_silently=False,
            )

            return redirect(request.META.get('HTTP_REFERER'))
        
    context = {
        'form': form,
        'ticket': ticket,
        'comments': comments,
        'segment': 'my_tickets',
        'parent': 'support',
        'page_title': 'Dashboard - Ticket - Comments',
    }
    return render(request, 'dashboard/tickets/comment.html', context)


@login_required(login_url='/users/signin/')
def close_ticket(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.states = StateChoices.CLOSED
    ticket.save()

    return redirect(reverse('my_tickets'))

@login_required(login_url='/users/signin/')
def my_tickets(request):
    filter_string = {}
    if search := request.GET.get('search'):
        filter_string['title__icontains'] = search
    
    sort = request.GET.get('sort')
    if sort == 'high':
        order_by = '-priority'
    elif sort == 'low':
        order_by = 'priority'
    else:
        order_by = '-created_at'

    tickets = Ticket.objects.filter(user=request.user, **filter_string).order_by(order_by)

    page_number = request.GET.get('page', 1) 
    paginator = Paginator(tickets, 10)
    try:
        tickets = paginator.page(page_number)
    except PageNotAnInteger:
        tickets = paginator.page(1)
    except EmptyPage:
        tickets = paginator.page(paginator.num_pages)

    context = {
        'tickets': tickets,
        'parent': 'support',
        'segment': 'my_tickets',
        'page_title': 'Dashboard - My Tickets',
    }
    return render(request, 'dashboard/tickets/my-tickets.html', context)