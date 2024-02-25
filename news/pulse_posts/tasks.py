from celery import shared_task

from datetime import datetime
from pulse_posts.api.pulse import load_posts
from pulse_posts.models import Investor, Post, Instrument

@shared_task
def post_update(ticker, num_posts):
    dt = load_posts(ticker=ticker, number_posts=num_posts)
    if dt:
        for post in dt:
            list_instruments_create = []
            list_instruments_stay = []
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
                # создание инструментов
                # for instrument in post['instruments']:
                #     ticker = instrument['ticker']
                #     name = instrument['briefName']
                #     type_i = instrument['type']
                #     instrument_instance = Instrument.objects.update_or_create(
                #                             ticker=ticker,
                #                             name=name,
                #                             type=type_i
                #                         )
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

                # InstrumentPost.objects.update_or_create(
                #     instrument=instrument_instance[0],
                #     post=post_instance[0]
                # )
