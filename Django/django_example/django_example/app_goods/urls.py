from django.urls import path
from app_goods.views import items_list, upload_price


urlpatterns = [
    path('items/', items_list, name='items_list'),
    path('upload_price/', upload_price, name='upload_price'),

]
