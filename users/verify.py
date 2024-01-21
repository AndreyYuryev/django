from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect
from users.models import User


def verify_user(recipient='', verify_url='', key=''):
    send_mail('Регистрация пользователя',
              f'Ваш адрес был указан для регистрации.\n Если это сделали вы перейдите по ссылке http://{verify_url}/?activate_key={key} для завершения регистрации.',
              settings.EMAIL_HOST_USER,
              [recipient, ])


def activate_user(request):
    key = request.GET.get('activate_key')
    current_user = User.objects.filter(is_active=False)
    for user in current_user:
        if str(user.activate_key) == str(key):
            user.is_active = True
            user.activate_key = None
            user.save()
    response = redirect('/users')
    return response


def recover_password(recipient='', password=''):
    current_user = User.objects.filter(email=recipient)
    print(current_user)
    for user in current_user:
        user.set_password(password)
        user.save()
        send_mail('Восстановление пароля', f'Ваш адрес был указан для восстановления пароля.\n Новый пароль {password}',
                  settings.EMAIL_HOST_USER,
                  [recipient, ])
