from django.shortcuts import render, redirect
from pulse_posts.forms import PostsPulse
from .tasks import post_update



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
    return render(request, 'pulse_posts/test.html', context={'form': form})