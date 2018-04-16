from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.

def index(request):
    
    if 'attempt' not in request.session:
        request.session['attempt'] = 0
    else:
        request.session['attempt'] += 1
    
    random_word = {
        "word": get_random_string(length=14),
        "attempt": request.session['attempt']
    }
    return render(request,'first_app/index.html', random_word)

def reset(request):
    if request.method == 'POST':
        request.session['attempt'] = 0
        return redirect('/')

def generate(request):
    if request.method == 'POST':
        return redirect('/')