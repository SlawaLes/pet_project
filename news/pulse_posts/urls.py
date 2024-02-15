from django.urls import path
from .views import loadPost

app_name = 'pulse_posts'

urlpatterns = [
    path('load_posts/',  loadPost, name='load'),
]