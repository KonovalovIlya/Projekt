from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from news.models import News, Comment


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=40, required=True, help_text='Имя')
    last_name = forms.CharField(max_length=40, required=True, help_text='Фамилия')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')
