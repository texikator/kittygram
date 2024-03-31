from django.urls import path

from cats.views import cat_list, cat_detail

urlpatterns = [
   path('cats/', cat_list, name='cats_list'),
   path('cats/<int:pk>/', cat_detail, name='cat_detail')
]


