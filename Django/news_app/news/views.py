from django.shortcuts import render
from django.views import generic, View
from django.http import HttpResponseRedirect
from news.models import News, Comment
from news.forms import NewsForm, CommentForm


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
    queryset = Comment.objects.all()[:10]


class NewsDetailView(generic.DetailView):
    model = News
    # template_name = 'news_detail.html'
    # context_object_name = 'news_detail'


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
        return render(request, 'news/news_form_redactor.html', context={'news_form': news_form, 'news_id': news_id})

    def post(self, request, news_id):
        news = News.objects.get(id=news_id)
        news_form = NewsForm(request.POST, instance=news)

        if news_form.is_valid():
            news.save()
        return render(request, 'news/news_form_redactor.html', context={'news_form': news_form, 'news_id': news_id})


class CommentFormView(View):
    # def get(self, request, news_id):
    #     news = News.objects.get(id=news_id)
    #     news_form = NewsForm(instance=news)
    #     return render(request, 'news/news_form_redactor.html', context={'news_form': news_form, 'news_id': news_id})

    # def post(self, request, comment):
    #     comment = Comment.objects.get(id=comment_id)
    #     comment_form = CommentForm(request.POST, instance=comment)
    #
    #     if comment_form.is_valid():
    #         comment.save()
    #     return render(request, 'news/news_detail.html', context={'comment_form': comment_form, 'comment_id': comment_id})

    def get(self, request):
        comment_form = CommentForm()
        return render(request, 'news/news_detail.html', {'comment_form': comment_form})

    def post(self, request):
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            Comment.objects.create(**comment_form.cleaned_data)
            return HttpResponseRedirect('/')
        return render(request, 'news/news_detail.html', {'comment_form': comment_form})
