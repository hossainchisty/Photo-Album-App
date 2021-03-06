from django.shortcuts import render,redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import EditPhoto,EditProfile
from .models import *

# Create your views here.
@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
def photo(request, pk):
    photo = Photo.objects.get(id=pk)
    tags = Hastag.objects.all()
    profiles = Profile.objects.all()

    context = { 'photos':photo,
                'hastags':tags,
                'profile':profiles}
    return render(request,'album.html', context)

@login_required(login_url='login')
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

@login_required(login_url='login')
def deletePhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    if request.method == 'POST':
        photo.delete()
        return redirect('/')    
    context = {'photo':photo}
    return render(request,'deletePhoto.html', context)
    
@login_required(login_url='login')
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

@login_required(login_url='login')
def profile(request):
    profiles = Profile.objects.all()
    context = {'profile':profiles}
    return render(request,'profile.html', context)

def editProfile(request,pk):
    profiles = Profile.objects.get(id=pk)
    print(profiles)
    form = EditProfile(instance=profiles)
    if request.method == "POST":
        form = EditProfile(request.POST, request.FILES, instance=profiles)
        if form.is_valid():
            form.save() 
            return redirect('/profile')

    context = { 'form':form}
    return render(request,'editProfile.html', context)
        
