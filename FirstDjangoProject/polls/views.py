from django.http import HttpResponse
from django.shortcuts import render,redirect 

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs.")


def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect('/')

def show(request,number):
    return HttpResponse('placeholder to display blog number'+ " "+ number)

def edit(request,number):
    print(number)
    return HttpResponse('laceholder to edit blog {}'.format(number))

def destroy(request,number):
    print(number)
    return redirect('/')
