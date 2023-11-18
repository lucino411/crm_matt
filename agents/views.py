import random

from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.shortcuts import reverse
from django.core.mail import send_mail
from leads.models import Agent
from .forms import AgentModelForm
from .mixins import OrganisorAndLoginRequiredMixin


class AgentListView(OrganisorAndLoginRequiredMixin, ListView):
    template_name = 'agents/agent_list.html'

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)
    
class AgentCreateView(OrganisorAndLoginRequiredMixin, CreateView):
    template_name = 'agents/agent_create.html'
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse('agents:agents_list')        
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_agent = True
        user.is_organisor = False
        user.set_password(f"{random.randint(0, 1000000)}")
        user.save()
        Agent.objects.create (
            user=user,
            organisation=self.request.user.userprofile,
        )
        send_mail(
            subject='You are invetid to be an agent',
            message='You were added as an agent on DJCRM. Please login',
            from_email='admin@test.com',
            recipient_list=[user.email]
        )
        return super(AgentCreateView, self).form_valid(form)
    

class AgentDetailView(OrganisorAndLoginRequiredMixin, DetailView):
    template_name = 'agents/agent_detail.html'
    context_object_name = 'agent'

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation) 
    
class AgentUpdateView(OrganisorAndLoginRequiredMixin, UpdateView):
    template_name = 'agents/agent_update.html'
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse('agents:agents_list')
    
    def get_queryset(self):
        return Agent.objects.all()

class AgentDeleteView(OrganisorAndLoginRequiredMixin, DeleteView):
    template_name = 'agents/agent_delete.html'
    context_object_name = 'agent'

    def get_success_url(self):
        return reverse('agents:agents_list')

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Agent.objects.filter(organisation=organisation)
