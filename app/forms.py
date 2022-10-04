from .models import House, Agent
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = '__all__'
        exclude = ['agent']
        widgets = {
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'house_type': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '8'}),
            'images_one': forms.FileInput(attrs={'class': 'form-control'}),
            'images_two': forms.FileInput(attrs={'class': 'form-control'}),
            'images_three': forms.FileInput(attrs={'class': 'form-control'}),
            'no_of_bedrooms': forms.NumberInput(attrs={'class': 'form-control'}),
            'area_per_meter_square': forms.NumberInput(attrs={'class': 'form-control'}),
            'no_of_bathroom': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class AgentCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AgentUpdateForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['first_name', 'last_name', 'avatar', 'email', 'about', 'skype']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'about': forms.Textarea(attrs={'class': 'form-control', 'rows': '8'}),
            'skype': forms.URLInput(attrs={'class': 'form-control'}),
        }

