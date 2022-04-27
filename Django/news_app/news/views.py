from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from news.models import News, Comment
from news.forms import NewsForm, CommentForm, AuthForm
from django.contrib.auth.models import User


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


# @login_required
# LoginRequiredMixin,
class CommentFormView(View):
    # login_url = '../'
    # redirect_field_name = 'redirect_to'
    def get(self, request, news_id):
        comment_form = CommentForm()
        return render(request, 'news/comment_new.html', {'comment_form': comment_form, 'news_id': news_id})


    def post(self, request, news_id):
        comment_form = CommentForm(request.POST)
        news = News.objects.get(id=news_id)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            if request.user.is_authenticated:
                comment.user = request.user
            else:
                comment.anonusername = 'anonim'.join(comment.anonusername)
                # comment.user = request.user
            comment.news = news
            comment.save()
            return HttpResponseRedirect('/')
        return render(request, 'news/comment_new.html', {'comment_form': comment_form, 'news_id': news_id})

# class CommentFormForAllView(View):
#
#     def get(self, request):
#         comment_form = CommentForm()
#         return render(request, 'news/pub_comment_new.html', {'comment_form': comment_form})
#
#     def post(self, request):
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             return HttpResponseRedirect('/')
#         return render(request, 'news/pub_comment_new.html', {'comment_form': comment_form})



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


# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from .forms import NewsContentForm
#
# # Create your views here.
# def news(request):
#     return render(request,'news/news.html')
# @login_required
# def makePost(request):
#     form = NewsContentForm(request.POST or None)
#     if request.method == "POST":
#         new_post = form.save()
#         print(form.cleaned_data.get('username'))
#         return redirect('/news/')
#     return render(request, 'news/makePost.html',locals())