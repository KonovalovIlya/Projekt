from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('', views.NewsListView.as_view(), name='news_list'),
    path('news/comments/', views.CommentListView.as_view(), name='comment_list'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news_detail'),
    path('news/register/', views.NewsFormView.as_view(), name='news_form'),
    path('news/<int:news_id>/comment_new/', views.CommentFormView.as_view(), name='comment_form'),
    path('news/<int:news_id>/redactor/', views.NewsFormEditView.as_view(), name='news_form_redactor'),
]
