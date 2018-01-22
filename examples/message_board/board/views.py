from django.shortcuts import render
from django.http import HttpResponse

from .models import Message

# Create your views here.

def index(request):
    messages = Message.objects.all().order_by('pub_date')
    return render(request, 'index.html', {
        'messages': messages,
    })
