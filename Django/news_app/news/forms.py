from django import forms
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
