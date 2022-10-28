from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Hike
# Create your views here.

def auth(request):
    return render(request, 'auth.html')

def home(request):
  hike = Hike.objects.all()
  return render(request, 'home.html', {'hike': hike})

def signup(request):
  error_message =''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('/home/')
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
  success_url = '/home/'