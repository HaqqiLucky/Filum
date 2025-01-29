from django.shortcuts import render
from .forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request) :
    if request.method == 'POST' :
        form = UserRegisterForm(request.POST)
        if form.is_valid() :
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            pp = form.cleaned_data('photo_profile')
            slug = form.cleaned_data['slug']
            if 'save' in request.POST:
                form.save()
                message = "save"
                return render(request, 'sucesfail/sucess.html')
            else:
                return render(request, 'sucesfail/fail.html')
        else:
            print("form is not valid")
    else:
        print("GET Request")
        return render(request, 'registerlogin/register.html', {'form' : UserRegisterForm()})

def register_view(request) :
    form= UserCreationForm()
    return render


def profile(request) :
    return render (request, 'profile.html')