from django.urls import path, re_path
from .views import loadPost, graphView, get_response

app_name = 'pulse_posts'

urlpatterns = [
    path('load_posts/',  loadPost, name='load'),
    path('graph/', graphView, name='graph'),
    path('detail/<slug:task_id>/', get_response, name='task_status')
]