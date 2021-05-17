from django.forms import ModelForm
from django.forms import forms
from .models import Photo, Profile

class EditPhoto(ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'
        exclude = ['user','hastags',]

    def __init__(self, *args, **kwargs):
        super(EditPhoto, self).__init__(*args, **kwargs)
        for key,value in self.fields.items():
            value.widget.attrs['class'] = 'mt-3 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 relative bg-white bg-white rounded text-sm border border-blueGray-300 outline-none focus:outline-none focus:ring w-full'

class EditProfile(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user','hastags',]
