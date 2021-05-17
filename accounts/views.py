from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate,login

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            
            user = authenticate(request, username=username,password=password)
            login(request,user)
            
            return redirect('/')

    else:
        form = RegistrationForm()
    
    context = {'form':form}

    return render(request, 'register.html', context)


