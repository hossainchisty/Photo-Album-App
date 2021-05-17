from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True,blank=True, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, blank=True,null=True)
    # is_verified = models.BooleanField(default=False)
    image = models.ImageField(default='profile.png')
    bio = models.TextField()
    joind_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

class Category(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name

class Hastag(models.Model):
    tags = models.CharField(max_length=200, null=True,blank=True)
    
    def __str__(self):
        return self.tags

class Photo(models.Model):
    user = models.ForeignKey(User, null=True,blank=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True,blank=True, on_delete=models.SET_NULL)
    hastags = models.ForeignKey(Hastag, null=True,blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=500, null=False,blank=False)
    image = models.ImageField(blank=False,null=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # modified_date = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.title

    