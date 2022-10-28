from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Hike, Review
from .forms import ReviewForm
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
      context['review_form'] = ReviewForm()
      return context

class HikeUpdate(LoginRequiredMixin, UpdateView):
    model = Hike
    fields = ['location', 'description', 'difficulty']
    def get_success_url(self):
        return f'/hikes/{self.object.id}'


class HikeDelete(LoginRequiredMixin, DeleteView):
    model = Hike
    success_url= '/hikes/'

class ReviewDelete(LoginRequiredMixin, DeleteView):
    model = Review
    def get_success_url(self):
        return f'/hikes/{self.object.hike_id}'

def add_review(request, hike_id):
  # create a FeedingForm instance using
  # the data that was submitted via the form
  form = ReviewForm(request.POST)
  # validate the form
  if form.is_valid():
    # can't save the form/object to the db
    # until we've assigned a cat_id
    new_review = form.save(commit=False)
    new_review.hike_id = hike_id
    new_review.user_id = request.user.id
    new_review.save()
  return redirect(f'/hikes/{hike_id}', hike_id=hike_id)