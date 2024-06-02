from django.shortcuts import render, redirect, get_object_or_404
from apps.ticket.forms import TicketForm, CommentForm
from apps.common.models import Ticket, StateChoices
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
            ticket.save()
            return redirect(request.META.get('HTTP_REFERER'))

    context = {
        'form': form,
        'segment': 'ticket'
    }
    return render(request, 'dashboard/tickets/create.html', context)

@staff_member_required(login_url='/admin/')
def oeprate_ticket(request):
    filter_string = {}
    if search := request.GET.get('search'):
        filter_string['title__icontains'] = search

    tickets = Ticket.objects.filter(states=StateChoices.OPEN, **filter_string)

    context = { 
        'segment': 'ticket',
        'tickets': tickets
    }
    return render(request, 'dashboard/tickets/operate.html', context)


@staff_member_required(login_url='/admin/')
def comment_to_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.ticket = ticket
            comment.save()

            ticket.states = request.POST.get('state', StateChoices.OPEN)
            ticket.save()

            return redirect(reverse('oeprate_ticket'))
        
    context = {
        'form': form,
        'ticket': ticket,
        'segment': 'ticket'
    }
    return render(request, 'dashboard/tickets/comment.html', context)