from django.shortcuts import render, redirect
from .import forms
from .import models
from django.views.generic import CreateView,UpdateView
from django.urls import reverse_lazy
# Create your views here.

class AddMusicianView(CreateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('add_musician')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditMusicianView(UpdateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'add_musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')