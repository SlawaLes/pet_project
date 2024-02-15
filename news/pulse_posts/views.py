from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from pulse_posts.forms import PostsPulse
from pulse_posts.api.pulse import load_posts
from pulse_posts.api.parser_pulse import create_investor, create_instrument
from .models import Investor, Instrument, InstrumentPost, Post
from datetime import datetime


# def loadPost(request):
#     return render(request, 'admin/base.html')
# # Create your views here.

def loadPost(request):
    if request.method == 'POST':
        form = PostsPulse(request.POST)
        if form.is_valid():
            ticker = form.cleaned_data['ticker']
            num_posts = form.cleaned_data['num_posts']
            dt = load_posts(ticker=ticker, number_posts=num_posts)
            if dt:
                for post in dt:
                    #создание инвестора
                    nickname = post['nickname']
                    profile_tinkoff = post['profileId']
                    investor_instanсe = Investor.objects.update_or_create(
                                            nickname=nickname,
                                            profile_tinkoff=profile_tinkoff
                                        )
                    #создание постов
                    likesCount = post['likesCount']
                    commentsCount = post['commentsCount']
                    reactionsCount = post['reactions']
                    inserted = datetime.fromisoformat(post['inserted'])
                    text = post['text']
                    post_instance = Post.objects.update_or_create(
                                        investor=investor_instanсe[0],
                                        likesCount=likesCount,
                                        commentsCount=commentsCount,
                                        reactionsCount=reactionsCount,
                                        inserted=inserted,
                                        text=text
                                    )
                    # создание инструментов
                    for instrument in post['instruments']:
                        ticker = instrument['ticker']
                        name = instrument['briefName']
                        type_i = instrument['type']
                        instrument_instance = Instrument.objects.update_or_create(
                                                ticker=ticker,
                                                name=name,
                                                type=type_i
                                            )
                        InstrumentPost.objects.update_or_create(
                            instrument=instrument_instance[0],
                            post=post_instance[0]
                        )
            return redirect('http://127.0.0.1:8000/')
    else:
        form = PostsPulse()
    return render(request, 'pulse_posts/test.html', context={'form': form})

    #return render(request, 'pulse_posts/form_load_posts.html')