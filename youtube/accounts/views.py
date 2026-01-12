from django.shortcuts import redirect
from django.contrib.auth import login
from django.views.generic import CreateView, TemplateView, DetailView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


from django.contrib import messages

# Create your views here.
class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('accounts:login')
    template_name = "accounts/register.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("/")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        messages.success(self.request, f"Welcome to YouTube Clone, {self.object.username}! Your account has been created.")
        return redirect("/")

class AboutView(TemplateView):
    template_name = "accounts/about.html"

class BotView(TemplateView):
    template_name = "accounts/bot.html"

class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = "accounts/profile.html"
    context_object_name = "profile_user"

    def get_object(self):
        return self.request.user