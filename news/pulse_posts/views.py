from django.shortcuts import render, redirect
from pulse_posts.forms import PostsPulse, GraphForm
from .tasks import post_update
from .models import Post
import plotly.express as px
from django.db.models import Count

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
    form = GraphForm()
    dt = (Post.objects.values('inserted__date')
          .annotate(cnt=Count('id'))
          .order_by('inserted__date'))

    fig = px.line(
        x=[item['inserted__date'] for item in dt],
        y=[item['cnt'] for item in dt],
        title='Посты по всем инструментам'
    )

    fig.update_layout(title={
        'font_size': 25,
        'xanchor': 'center',
        'x': 0.5
    })

    graph = fig.to_html()

    context = {
        'graph': graph,
        'form': form
    }

    return render(request, 'pulse_posts/formGraphNew_test.html', context=context)