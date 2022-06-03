from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from app_users.forms import AuthForm, RegisterForm, RestorePasswordForm
from app_users.models import Profile


def login_view(request):
    if request.method == 'POST':
        auth_form = AuthForm(request.POST) #  Для POST пытаемся аутентифицировать пользователя.
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Вы успешно вошли в систему')
                else:
                    auth_form.add_error('__all__', 'Ошибка! Учетная запись не активна')
            else:
                auth_form.add_error('__all__', 'Ошибка! Не верно указан пароль или логин')
    else: #  Для всех остальных запросов отображаем страничку логина
        auth_form = AuthForm
    context = {
        'form': auth_form
    }
    return render(request, 'users/login.html', context=context)


class AnotherLoginView(LoginView):
    template_name = 'users/login.html'


def logout_view(request):
    logout(request)
    return HttpResponse('Вы разлогинились')


class AnotherLogoutView(LogoutView):
    # template_name = 'users/logout.html'
    next_page = '/'


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def another_register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            birth_date = form.cleaned_data.get('birth_date')
            city = form.cleaned_data.get('city')
            Profile.objects.create(
                user=user,
                city=city,
                birth_date=birth_date
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


def restore_password(request):
    if request.method == 'POST':
        restore_password_form = RestorePasswordForm(request.POST)
        if restore_password_form.is_valid():
            user_email = restore_password_form.cleaned_data['email']
            new_password = User.objects.make_random_password()
            current_user = User.objects.filter(email=user_email).first()
            if current_user:
                current_user.set_password(new_password)
                current_user.save()
            send_mail(
                subject='Восстановление пароля',
                message='Test',
                from_email='admin@company.com',
                recipient_list=[restore_password_form.cleaned_data['email']]
            )
            return HttpResponse('Письмо с новым паролем было успешно отправлено')
    restore_password_form = RestorePasswordForm()
    return render(request, 'users/restore_password.html', {'form': restore_password_form})
