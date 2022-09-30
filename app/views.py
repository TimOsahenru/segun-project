from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
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


# ..................... House Update ......................................
class HouseUpdate(UpdateView):
    model = House
    template_name = '../templates/edit.html'
    success_url = 'houses'  # Change to profile

