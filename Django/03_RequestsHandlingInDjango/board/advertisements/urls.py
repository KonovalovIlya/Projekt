from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPage.as_view(), name='main_page'),
    path('advertisement_list/', views.advertisement_list, name='advertisement_list'),
    path('advertisements/', views.Advertisements.as_view(), name='advertisements'),
    path('contacts/', views.Contacts.as_view(), name='contacts'),
    path('about/', views.About.as_view(), name='about'),
]
