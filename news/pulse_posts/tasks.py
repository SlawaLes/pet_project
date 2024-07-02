import time

from celery import shared_task

from datetime import datetime
from pulse_posts.api.pulse import load_posts
from pulse_posts.models import Investor, Post, Instrument

import os
from celery import Celery
from django.conf import settings
import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news.settings')

app = Celery('news')
app.config_from_object('django.conf:settings')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.conf.result_backend = settings.CELERY_RESULT_BACKEND
app.autodiscover_tasks()



@shared_task
def post_update(ticker, num_posts):
    dt = load_posts(ticker=ticker, number_posts=num_posts)
    if dt:
        for post in dt:
            #создание инвестора
            nickname = post['nickname']
            profile_tinkoff = post['profileId']
            investor_instanсe = Investor.objects.get_or_create(
                                    nickname=nickname,
                                    profile_tinkoff=profile_tinkoff
                                )
            #создание постов
            likesCount = post['likesCount']
            commentsCount = post['commentsCount']
            reactionsCount = post['reactions']
            inserted = datetime.fromisoformat(post['inserted'])
            text = post['text']
            post_instance = Post.objects.get_or_create(
                                investor=investor_instanсe[0],
                                likesCount=likesCount,
                                commentsCount=commentsCount,
                                reactionsCount=reactionsCount,
                                inserted=inserted,
                                text=text
                            )
            #если пост создался (НЕ ВЗЯЛСЯ ИЗ БАЗЫ), идем дальше создавать инструменты
            if post_instance[1]:
                list_instruments_stay = [
                    instrument
                        for instrument in Instrument.objects.filter(ticker__in=[
                            inst['ticker'] for inst in post['instruments']
                            ])
                ]
                list_instruments_create = [
                    instrument
                        for instrument in post['instruments']
                        if instrument['ticker'] not in [
                            instr.ticker for instr in list_instruments_stay
                        ]
                ]

                instruments_create_list = [Instrument(
                                            ticker=instrument['ticker'],
                                            name=instrument['briefName'],
                                            type=instrument['type']
                                            ) for instrument in list_instruments_create]

                Instrument.objects.bulk_create(instruments_create_list)

                #Привязываю пост к созданным и существующим бумагам в базе
                post_instance[0].instrument.add(*instruments_create_list+list_instruments_stay)



@shared_task(bind=True)
def loop(self, i):

    for j in range(i):
        print(f'item = {j}')
        time.sleep(1)
        self.update_state(state='PROGRESS',
                          meta={'current': j, 'total': i})
    print('task_end!!')
    return {'current': 100, 'total': 100}