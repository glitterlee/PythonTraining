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
            msg_form = NewMessageForm()

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

def edit_msg(request, msg_id):
    message = Message.objects.filter(id=msg_id).first()

    if message is None:
        return HttpResponseForbidden("This message doesn't exist.")
    else:
        msg_form = NewMessageForm(request.POST or None, instance=message)

        if msg_form.is_valid():
            msg_form.save()
            return redirect(reverse('index'))
        
    return render(request, 'edit.html', {
        'msg_form': msg_form,
        'message': message,
    })