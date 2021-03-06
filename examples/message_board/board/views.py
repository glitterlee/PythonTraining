from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse

from .models import Message
from .forms import NewMessageForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        msg_form = NewMessageForm(request.POST)
        if msg_form.is_valid():
            msg = msg_form.save()
            return redirect(reverse('index'))

    else:
        msg_form = NewMessageForm()
    
    messages = Message.objects.all().order_by('pub_date')
    return render(request, 'index.html', {
        'messages': messages,
        'msg_form': msg_form,
    })

def clear_all(request):
    Message.objects.all().delete()
    return redirect(reverse('index'))
