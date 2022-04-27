from django import forms
from news.models import News, Comment
from django.contrib.auth.models import User


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        if User.is_authenticated:
            exclude = ['user', 'anonusername', 'news']
        # else:
        #     exclude = ['user', 'news']



class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
