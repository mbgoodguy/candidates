from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

from .models import Candidate


class Create(CreateView):
    model = Candidate
    fields = '__all__'
    success_url = reverse_lazy('read')


class Read(ListView):
    model = Candidate
    queryset = Candidate.objects.all()


class Update(UpdateView):
    model = Candidate
    fields = '__all__'
    success_url = reverse_lazy('read')


class Delete(DeleteView):
    queryset = Candidate.objects.all()
    success_url = reverse_lazy('read')


def handler500(request):
    response = render(request, '500.html', {})
    response.status_code = 500
    return response
