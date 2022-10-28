from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Hike, Review
# Create your views here.


def auth(request):
    return render(request, 'auth.html')


def hikes_index(request):
    hikes = Hike.objects.all()
    return render(request, 'hikes/index.html', {'hikes': hikes})


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


class HikeCreate(LoginRequiredMixin, CreateView):
    model = Hike
    fields = ['name', 'location', 'description', 'difficulty']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    success_url = '/hikes/'

class HikeDetail(DetailView):
    model = Hike
    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['reviews'] = Review.objects.filter(hike=self.object.id)
      return context

class HikeUpdate(LoginRequiredMixin, UpdateView):
    model = Hike
    fields = ['location', 'description', 'difficulty']
    def get_success_url(self):
        return f'/hikes/{self.object.id}'


class HikeDelete(LoginRequiredMixin, DeleteView):
    model = Hike
    success_url= '/hikes/'
