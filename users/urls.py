from django.urls import path
from users.apps import UsersConfig
from django.contrib.auth.views import LoginView, LogoutView
from users.views import RegisterView, ProfileView, get_email, UserChangePasswordView, UserChangePasswordDoneView
from users.verify import activate_user

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('verify/', activate_user),
    path('recovery/', get_email, name='recovery'),
    path('password_change/', UserChangePasswordView.as_view(), name='password_change'),
    path('password_change/done/', UserChangePasswordDoneView.as_view(), name='password_change_done'),
]