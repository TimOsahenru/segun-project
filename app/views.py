from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView
from .models import *


# ..................... All Houses ......................................
class HouseList(ListView):
    model = House
    context_object_name = 'houses'
    template_name = '../templates/index.html'


# ..................... House details ......................................
class HouseDetail(DetailView):
    model = House
    context_object_name = 'house'
    template_name = '../templates/detail.html'


# ..................... Agent profile ......................................
class AgentProfile(DetailView):
    model = Agent
    template_name = '../templates/profile.html'
    context_object_name = 'agent'

    def get_object(self):
        pk = self.kwargs.get('pk')
        agent = Agent.objects.get(username=pk)
        return agent

    def get_context_data(self, **kwargs):
        context = super(AgentProfile, self).get_context_data()
        pk = self.kwargs.get('pk')
        context['agent'] = Agent.objects.get(username=pk)
        context['houses'] = context['agent'].house_set.all()
        return context


# ..................... Profile Update ......................................
class ProfileUpdate(UpdateView):
    model = Agent
    fields = ['first_name', 'last_name', 'email', 'about', 'skype']
    template_name = '../templates/profile_update.html'

    def get_object(self):
        pk = self.kwargs.get('pk')
        agent = Agent.objects.get(username=pk)
        return agent

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return redirect('profile', pk=self.request.user.username)
        return super(ProfileUpdate, self).form_valid()


# ..................... House Update ......................................
class HouseUpdate(UpdateView):
    model = House
    template_name = '../templates/edit.html'
    fields = '__all__'
    
    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return redirect('profile', pk=self.request.user.username)
        return super(HouseUpdate, self).form_valid()


# ..................... House Create ......................................
class HouseCreate(CreateView):
    model = House
    template_name = '../templates/create.html'
    fields = '__all__'
    
    def form_valid(self, form):
        if form.is_valid():
            form.save(commit=False)
            form.instance.agent = self.request.user
            form.save()
            return redirect('profile', pk=self.request.user.username)
        return super(HouseCreate, self).form_valid(form)
