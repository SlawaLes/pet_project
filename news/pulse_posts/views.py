from django.shortcuts import render, redirect
from pulse_posts.forms import PostsPulse, GraphForm
from .tasks import post_update
from .models import Post
import plotly.express as px
from django.db.models import Count
import datetime
from pulse_posts.services.get_graph_data import get_data_form_graph
from pulse_posts.services.get_graph import plot_graph
from django.http import JsonResponse
from django.http import HttpResponse
from celery.result import AsyncResult
import json

def loadPost(request):
    if request.method == 'POST':
        form = PostsPulse(request.POST)
        if form.is_valid():
            ticker = form.cleaned_data['ticker']
            num_posts = form.cleaned_data['num_posts']
            post_update.delay(ticker=ticker, num_posts=num_posts)
            return redirect('http://127.0.0.1:8000/')
    else:
        form = PostsPulse()
    return render(request, 'pulse_posts/loadPost.html', context={'form': form})


def graphView(request):
    dt = (Post.objects
          .filter(inserted__date__gte=datetime.date.fromisoformat('2023-11-01'))
          .values('inserted__date')
          .annotate(cnt=Count('id'))
          .order_by('inserted__date'))
    context = {'base_graph': plot_graph(dt)}

    if request.method == 'POST':
        form = GraphForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            # queryset = get_data_form_graph(clean_data)
            filter_graph = plot_graph(get_data_form_graph(clean_data), clean_data)
            context['form'] = form
            if not filter_graph:
                context['error_with_graph'] = True
            context['filter_graph'] = filter_graph
            return render(request, 'pulse_posts/graph_main.html', context=context)
    else:
        context['form'] = GraphForm()

    return render(request, 'pulse_posts/graph_main.html', context=context)


def get_response(request, task_id):
    result = AsyncResult(task_id)
    response = {
        'status': result.state,
        'data': result.info
    }
    return HttpResponse(response, content_type='application/json')