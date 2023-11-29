from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Candidate


class Create(SuccessMessageMixin, CreateView):
    model = Candidate
    fields = '__all__'
    success_url = reverse_lazy('read')
    success_message = "Candidate : %(name)s created succesfully!"


class Read(ListView):
    model = Candidate
    queryset = Candidate.objects.all()


class Update(SuccessMessageMixin, UpdateView):
    model = Candidate
    fields = '__all__'
    success_url = reverse_lazy('read')
    success_message = "Candidate : %(name)s updated succesfully!"


class Delete(DeleteView):
    model = Candidate

    def get_success_url(self):
        messages.success(self.request, "Candidate deleted succesfully! ")
        return reverse('read')