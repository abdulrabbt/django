from django.shortcuts import render, redirect
import string
from django.utils.crypto import get_random_string

def index(request):
    new_random = get_random_string(length=14)
    
    if 'counter' not in request.session:
        request.session['counter'] = 1
        print ("counter inside"), request.session['counter']
    print ("counter outside", request.session['counter'])
    context = {
        'random': new_random,
        'counter': request.session['counter'],
    }
    return render(request, 'index.html', context)

def increment(request):
    request.session['counter'] += 1
    return redirect('/')

def clear(request):
    try:
        request.session['counter'] = 1
    except KeyError:
        pass
    return redirect('/')