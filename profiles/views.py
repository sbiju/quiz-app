from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView
from django.core.urlresolvers import reverse_lazy

User = get_user_model()

from .forms import  MasterProfileForm, ParticipantProfileForm
from .models import MasterProfile, ParticipantProfile
from .mixins import StaffRequiredMixin, LoginRequiredMixin


class HomePageView(TemplateView):
    template_name = "home.html"


class MasterListView(ListView):
    model = MasterProfile


class ParticipantListView(LoginRequiredMixin, ListView):
    model = ParticipantProfile


class MasterDetailView(LoginRequiredMixin, DetailView):
    model = MasterProfile


class ParticipantDetailView(LoginRequiredMixin, DetailView):
    model = ParticipantProfile


class ParticipantCreateView(LoginRequiredMixin, CreateView):
    model = ParticipantProfile
    form_class = ParticipantProfileForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(ParticipantCreateView, self).form_valid(form)


class MasterCreateView(StaffRequiredMixin, CreateView):
    model = MasterProfile
    form_class = MasterProfileForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(MasterCreateView, self).form_valid(form)


class MasterUpdateView(StaffRequiredMixin, UpdateView):
    model = MasterProfile
    form_class = MasterProfileForm


class ParticipantUpdateView(LoginRequiredMixin, UpdateView):
    model = ParticipantProfile
    form_class = ParticipantProfileForm


class ParticipantDeleteView(LoginRequiredMixin, DeleteView):
    model = ParticipantProfile
    success_url = reverse_lazy('member_list')
    template_name = 'profiles/confirm_delete.html'


class MasterDeleteView(StaffRequiredMixin, DeleteView):
    model = MasterProfile
    success_url = reverse_lazy('master_list')
    template_name = 'profiles/confirm_delete.html'







