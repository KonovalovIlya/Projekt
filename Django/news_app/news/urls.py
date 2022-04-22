from django.urls import path
from . import views


urlpatterns = [
    path('', views.NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news_detail'),
    path('news/register/', views.NewsFormView.as_view(), name='news_form'),
    path('news/<int:news_id>/redactor/', views.NewsFormEditView.as_view(), name='news_form_redactor'),

]