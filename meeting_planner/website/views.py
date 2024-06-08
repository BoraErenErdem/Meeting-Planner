import datetime

from django.shortcuts import render
from django.http import HttpResponse
from meetings.models import Meeting

# Create your views here.

def welcome(request):
    return render(  # render fonksiyonu 3 kısımdan oluşur. request=request kısmı gelen talebi requeste yönlendirir.
        request=request,
        template_name='website/welcome.html',
        context={'message':'Welcome to the Meeting Planner App',
                    'num_meetings': Meeting.objects.count(),
                    'meetings': Meeting.objects.all()}
                )

def date(request):
    return HttpResponse(f'Thi page was servered at {str(datetime.datetime.now())}')

def about(request):
    return HttpResponse(f'Copyright Erdem Solutions')