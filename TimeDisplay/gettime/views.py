from django.http import HttpResponse
from django.shortcuts import render,redirect 
from time import gmtime, strftime


def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    print(context)
    return render(request,'index.html', context)