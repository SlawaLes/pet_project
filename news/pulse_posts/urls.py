from django.urls import path
from .views import loadPost, graphView

app_name = 'pulse_posts'

urlpatterns = [
    path('load_posts/',  loadPost, name='load'),
    path('graph/', graphView, name='graph')
]