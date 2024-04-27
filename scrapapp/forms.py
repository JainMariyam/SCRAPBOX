from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from scrapapp.models import Scraps,UserProfile,Bids


class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]


class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile    
        exclude=('user',)  

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField() 


class ScrapForm(forms.ModelForm):
    class Meta:
        model=Scraps
        exclude=('user','created_date')  
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "condition":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "place":forms.TextInput(attrs={"class":"form-control"})
        }    


class BidsForm(forms.ModelForm):
    class Meta:
        model=Bids
        fields=['amount']   
        
        