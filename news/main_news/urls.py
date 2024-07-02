from django.urls import path
from .views import  get_response_photo, generationFormView, generationFormViewTask

app_name = 'main_news'

urlpatterns = [
    path('photo/<slug:task_id>/', get_response_photo, name='photo_status'),
    path('form/<slug:task_id>/', generationFormViewTask, name='formGenerationTask'),
    path('form/', generationFormView, name='formGeneration'),
]