from django.urls import path

from cats.views import APICat, cat_detail

urlpatterns = [
   path('cats/', APICat.as_view(), name='cats_list'),
   path('cats/<int:pk>/', cat_detail, name='cat_detail')
]


