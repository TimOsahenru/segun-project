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


class AgentCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

