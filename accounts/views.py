from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from accounts.forms import UserForm
# Create your views here.

@csrf_exempt
def sign_up(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            email = request.POST['email']
            password = request.POST['password1']
            user = authenticate(request, email=email,password=password)
            login(request,user)

            return redirect('sign-in')
    else:
        form = UserForm()

    context = {'form':form}

    return render(request, 'sign_up.html', context)



@csrf_exempt
def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
        # A backend authenticated the credentials
                    login(request,user)
        else:
        # No backend authenticated the credentials
                    messages.error(request, 'Credential is incorrect')
        return redirect('dashboard')

    template_name = 'login.html'
    context = {}
    return render(request, template_name, context)