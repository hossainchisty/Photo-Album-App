from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm,PasswordChangeForm
from django.contrib.auth.forms import AuthenticationForm

# We are importing the following dependencies from Django

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'username': forms.TextInput(attrs={'placeholder': 'Enter username'}),
            # 'first_name': forms.TextInput(attrs={'placeholder': 'Enter firstname'}),
            # 'last_name': forms.TextInput(attrs={'placeholder': 'Enter lastname'}),
        
          }


    def __init__(self, *args, **kwargs):
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': ('Enter password')})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Re-enter Password'})
     

     
        for key,value in self.fields.items():
            value.widget.attrs['class'] = 'h-12 px-2 w-full rounded focus:outline-none focus:border-indigo-600'
        