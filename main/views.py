from django.shortcuts import render
from django.http import HttpResponse
from main.models import Message


def home(request):
    messages = Message.objects.all()
    output = "Messages:<br>"
    
    for msg in messages:
        output += msg.text + "<br>"
    
    return HttpResponse(output)

def about(request):
    return render(request, 'main/about.html')