from django.shortcuts import render
from news_app.models import News
from django.views import generic


# Create your views here.
class NewsListView(generic.ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news_list'
    queryset = News.objects.all()[:10]


class NewsDetailView(generic.DetailView):
    model = News
    template_name = 'news_detail.html'


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
    def get(self, request, profile_id):
        news = News.objects.get(id=profile_id)