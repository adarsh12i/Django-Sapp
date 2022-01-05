from django.http.response import HttpResponse
from django.shortcuts import render
import datetime
from django.http import HttpResponse

def k1(request):
    d=datetime.datetime.now()
    s="<h1> the current time is "+str(d)+"</h1>"
    return HttpResponse(s)

def k2(request):
    return render(request, "k2.html", {})

def k3(request):
    s="<h1> Adithya </h1>"
    return HttpResponse(s)