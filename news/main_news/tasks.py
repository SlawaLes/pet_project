from main_news.api_news.test_image import generator
from celery import shared_task
from .models import ImagesGenerated, UserPictures
from django.contrib.auth.models import User
import base64
from django.core.files.base import ContentFile


@shared_task(bind=True)
def generate_photo(self, text):
    self.update_state(state='PROGRESS',
                      meta={'task_id': self.request.id})
    obj = ImagesGenerated.objects.create(
                text=text,
                task_id=self.request.id
            )
    result = generator(text)
    name = f'{self.request.id}.png'
    img = ContentFile(base64.b64decode(result), name=name)
    obj.image = img
    obj.is_ready = True
    obj.save()
    return {'task_id': self.request.id}
