from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from news.models import News, Comment, Profile


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'


class NewsSortedForm(forms.Form):
    ordering = forms.ChoiceField(label='Сортировать', required=False, choices=[
        ['created_at', 'сначала новые'],
        ['-created_at', 'сначала старые']
    ])


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
    phone_number = forms.CharField(max_length=36, required=False, help_text='Номер телефона')
    city = forms.CharField(max_length=36, required=False, help_text='Город')
    verification = forms.BooleanField(required=False)
    publish_count = forms.IntegerField(required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
