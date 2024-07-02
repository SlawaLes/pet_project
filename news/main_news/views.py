from django.http import HttpResponse, HttpResponseRedirect
from celery.result import AsyncResult
import json
from django.shortcuts import render, reverse
from .forms import ImageForm
from .tasks import generate_photo
from .models import PictureLinks, ImagesGenerated

def get_response_photo(request, task_id):
    result = AsyncResult(task_id)
    response = {
        'status': result.state,
        'data': result.info
    }
    return HttpResponse(json.dumps(response), content_type='application/json')

def generationFormView(request):
    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            task_id = generate_photo.delay(text)
            return HttpResponseRedirect(reverse('main_news:formGenerationTask', args=[task_id]))
    else:
        form = ImageForm()
        img_back = PictureLinks.objects.filter(is_base=True).first()
        return render(request, 'main_news/index_gen.html', context={'form': form, 'img_back_link': img_back.link})


def generationFormViewTask(request, task_id):
    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            task_id = generate_photo.delay(text)
            return HttpResponseRedirect(reverse('main_news:formGenerationTask', args=[task_id]))
    else:
        obj = ImagesGenerated.objects.filter(task_id=task_id).first()
        form = ImageForm(data={'text': obj.text})
        img_back = PictureLinks.objects.filter(is_base=False).order_by('?').first()
        context = {'form': form,
                   'task_id_url': 'http://127.0.0.1:8000/gen/photo/'+task_id+'/',
                   'photo_url': '/generated/'+task_id+'.png',
                   'img_back_link': img_back.link,
                   'obj': obj}

        return render(request, 'main_news/index_gen.html', context=context)