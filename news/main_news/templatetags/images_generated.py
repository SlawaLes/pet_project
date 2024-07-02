from django import template
from main_news.models import ImagesGenerated

register = template.Library()

@register.simple_tag(name='get_images')
def last_generated_images():
    return ImagesGenerated.objects.filter(is_ready=True).order_by('-date')[:5]