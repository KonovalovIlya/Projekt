from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views import generic, View
from django.http import HttpResponseRedirect
from news.models import News, Comment
from news.forms import NewsForm, CommentForm, AuthForm


# Create your views here.
class NewsListView(generic.ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news_list'
    queryset = News.objects.all()[:10]


class CommentListView(generic.ListView):
    model = Comment
    template_name = 'news_detail.html'
    context_object_name = 'comment_list'


class NewsDetailView(generic.DetailView):
    model = News
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_list'] = Comment.objects.all()
        return context



class CommentFormView(View):

    def get(self, request, news_id):
        comment_form = CommentForm()
        if request.user.is_authenticated:
            del comment_form.fields['user']
            del comment_form.fields['anonusername']
            del comment_form.fields['news']
        else:
            del comment_form.fields['user']
            del comment_form.fields['news']
        return render(request, 'news/comment_new.html', {'comment_form': comment_form, 'news_id': news_id})


    def post(self, request, news_id):
        comment_form = CommentForm(request.POST)
        news = News.objects.get(id=news_id)
        if request.user.is_authenticated:
            del comment_form.fields['user']
            del comment_form.fields['anonusername']
            del comment_form.fields['news']
        else:
            del comment_form.fields['user']
            del comment_form.fields['news']
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            if request.user.is_authenticated:
                comment.user = request.user
            else:
                comment.anonusername = ''.join(['anonim', comment.anonusername])
            comment.news = news
            comment.save()
            return HttpResponseRedirect('/')
        return render(request, 'news/comment_new.html', {'comment_form': comment_form, 'news_id': news_id})


class NewsFormView(View):

    def get(self, request):
        news_form = NewsForm()
        return render(request, 'news/news_form.html', {'news_form': news_form})

    def post(self, request):
        news_form = NewsForm(request.POST)

        if news_form.is_valid():
            News.objects.create(**news_form.cleaned_data)
            return HttpResponseRedirect('/')
        return render(request, 'news/news_form.html', {'news_form': news_form})


class NewsFormEditView(View):
    def get(self, request, news_id):
        news = News.objects.get(id=news_id)
        news_form = NewsForm(instance=news)
        return render(
            request,
            'news/news_form_redactor.html',
            context={'news_form': news_form, 'news_id': news_id}
        )

    def post(self, request, news_id):
        news = News.objects.get(id=news_id)
        news_form = NewsForm(request.POST, instance=news)

        if news_form.is_valid():
            news.save()
        return render(request, 'news/news_form_redactor.html', context={'news_form': news_form, 'news_id': news_id})


class LoginView(LoginView):
    template_name = 'news/login.html'


class LogoutView(LogoutView):
    next_page = '/'

