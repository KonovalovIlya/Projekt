from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    # path('', views.NewsListView.as_view(), name='news_list'),
    path('', views.news_list, name='news_list'),
    path('tag/<slug:tag_slug>/', views.news_list, name='news_list_by_tag'),
    path('news/comments/', views.CommentListView.as_view(), name='comment_list'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news_detail'),
    path('news/register/', views.NewsFormView.as_view(), name='news_form'),
    path('news/<int:news_id>/comment_new/', views.CommentFormView.as_view(), name='comment_form'),
    path('news/<int:news_id>/redactor/', views.NewsFormEditView.as_view(), name='news_form_redactor'),
    path('users/register/', views.register_view, name='register'),
    path('users/profile/<int:pk>', views.ProfileDetailView.as_view(), name='profile'),
    # path('news/tag/tag_<tag>', views.tag_list_view, name='tag_list'),

]
