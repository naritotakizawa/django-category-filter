from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.PostCreate.as_view(), name='post_create'),
]