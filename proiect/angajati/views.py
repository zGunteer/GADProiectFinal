from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from angajati.models import Angajati


# Create your views here.
class AngajatiView(LoginRequiredMixin, ListView):
    model = Angajati
    template_name = 'angajati/angajati_index.html'


class CreateAngajatiView(LoginRequiredMixin, CreateView):
    model = Angajati
    fields = ['nume', 'varsta']
    template_name = 'angajati/angajati_form.html'

    def get_success_url(self):
        return reverse('angajati:lista_angajati')


class UpdateAngajatiView(LoginRequiredMixin, UpdateView):
    model = Angajati
    fields = ['nume', 'varsta']
    template_name = 'angajati/angajati_form.html'

    def get_success_url(self):
        return reverse('angajati:lista_angajati')

@login_required
def delete_angajati(request, pk):
    Angajati.objects.filter(id=pk).update(status=0)
    return redirect('angajati:lista_angajati')

@login_required
def activate_angajati(request, pk):
    Angajati.objects.filter(id=pk).update(status=1)
    return redirect('angajati:lista_angajati')