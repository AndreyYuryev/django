from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, TemplateView
from users.models import User
from users.forms import UserRegisterForm, UserProfileForm, ResetPasswordForm
from users.verify import verify_user, recover_password
import random
import string



# Create your views here.
class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        if form.is_valid():
            user = form.save()
            user.activate_key = ''.join(random.choice(string.digits) for i in range(10))
            user.is_active = False
            user.save()
            verify_user(user.email, '127.0.0.1:8000/users/verify', user.activate_key)
        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def get_email(request):
    if request.method == "POST":
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            recover_password(email, password=''.join(random.choice(string.digits) for i in range(10)))
            return redirect('users:login')
    elif request.method == 'GET':
        form = ResetPasswordForm()
    return render(request, "users/recovery.html", {"form": form})
