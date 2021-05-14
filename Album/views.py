from django.shortcuts import render,redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm,PasswordChangeForm
from django.contrib.auth.decorators import  login_required
from .forms import EditPhoto
from .models import *


# Create your views here.
@login_required(login_url='sign-in')
def album(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)
        
    categories = Category.objects.all()
    profiles = Profile.objects.all()
    #photos = Photo.objects.all()
    categories = Category.objects.all()
  
    tags = Hastag.objects.all()

  
    context = { 'categories':categories,
                'photos':photos ,
                'hastags':tags,
                'profile':profiles,
                }

    return render(request,'home.html',context)

@login_required(login_url='sign-in')
def result(request):
    
    profiles = Profile.objects.all()
    try:
        query = request.GET['search']
        print("Search",query)
        # filedname__icontains
        filter_by = Photo.objects.filter(title__icontains=query)
        print('Filter data', filter_by)
    except MultiValueDictKeyError:
        print('Just for checking this error...')
    
   
    context = { 'filter_by':filter_by,
                'profile':profiles,} 
    return render(request,'result.html',context)

@login_required(login_url='sign-in')
def photo(request, pk):
    photo = Photo.objects.get(id=pk)
    tags = Hastag.objects.all()
    profiles = Profile.objects.all()

    context = { 'photos':photo,
                'hastags':tags,
                'profile':profiles}
    return render(request,'album.html', context)

@login_required(login_url='sign-in')
def editPhoto(request, pk):
    photo = Photo.objects.get(id=pk)

    form = EditPhoto(instance=photo)
    #request.FILES
    if request.method == "POST":
        form = EditPhoto(request.POST,request.FILES, instance=photo)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = { 'form':form ,'photo':photo}
    return render(request,'editPhoto.html', context)

@login_required(login_url='sign-in')
def deletePhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    if request.method == 'POST':
        photo.delete()
        return redirect('/')    
    context = {'photo':photo}
    return render(request,'deletePhoto.html', context)
    
@login_required(login_url='sign-in')
def addPhoto(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        user_data = request.POST
        images = request.FILES.get('image')

        if user_data['category'] != None:
            category = Category.objects.get(id=user_data['category'])
        elif user_data['new_category'] != '':
            category  = Category.objects.get_or_create(name=user_data['new_category'])
        else:
            category = None

        photos = Photo.objects.create(
            title=user_data['title'],
            description=user_data['description'],
            category=category,
            image=images
        )
        
        return redirect('home')

    context = {

        'categories':categories,
    }

    template_name = 'addPhoto.html'
    return render(request, template_name, context)

@login_required(login_url='sign-in')
def profile(request):
    profiles = Profile.objects.all()
    context = {'profile':profiles}
    return render(request,'profile.html', context)


def Index(request):
    # now = datetime.datetime.now()

    # context = {
    #     'first': 4,
    #     'second':1000000,
    #     'third': 1234,
    #     'fourth':23222,
    #     'fifth': 190,
    #     'ordinal': 1,
    #     'now': now,
    #     'today': now,
    #     'other_date': now + datetime.timedelta(days=-4),
    #     'future_date': now + datetime.timedelta(days=-540, ),
    #     'past_date': now - datetime.timedelta(days=-741),
    #     'test': "Joel is a slug" ,

    # }

    context = {'UserCreationForm': UserCreationForm}

    template_name = "humanize.html"

    return render(request, template_name, context)