from django.urls import path
from . import views

app_name = 'app2'

urlpatterns = [
    path('', views.PostCreate.as_view(), name='post_create'),
    path('api/category/get/', views.ajax_get_category, name='ajax_get_category')
]