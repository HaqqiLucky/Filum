from django.shortcuts import render

def home(request) :
    return render(request, 'home.html')

def search(request) :
    return render(request, 'search.html')

def profile(request) :
    return render(request, 'profile.html')