from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class homePageView(TemplateView):
    template_name = 'home.html'


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
