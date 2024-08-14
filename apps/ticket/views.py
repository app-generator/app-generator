from django.shortcuts import render, redirect, get_object_or_404
from apps.ticket.forms import TicketForm, CommentForm
from apps.common.models import Ticket, StateChoices, PriorityChoices, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse

# Create your views here.


@login_required(login_url='/users/signin/')
def create_support_ticket(request):
    form = TicketForm()

    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
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
    return render(request, 'dashboard/tickets/create.html', context)

@staff_member_required(login_url='/admin/')
def all_tickets(request):
    filter_string = {}
    if search := request.GET.get('search'):
        filter_string['title__icontains'] = search

    tickets = Ticket.objects.filter(states=StateChoices.OPEN, **filter_string)

    context = { 
        'tickets': tickets,
        'segment': 'my_tickets',
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

            ticket.states = request.POST.get('state', StateChoices.OPEN)
            ticket.save()

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
def my_tickets(request):
    filter_string = {}
    if search := request.GET.get('search'):
        filter_string['title__icontains'] = search

    tickets = Ticket.objects.filter(user=request.user, states=StateChoices.OPEN, **filter_string)

    context = {
        'tickets': tickets,
        'parent': 'support',
        'segment': 'my_tickets',
        'page_title': 'Dashboard - My Tickets',
    }
    return render(request, 'dashboard/tickets/my-tickets.html', context)