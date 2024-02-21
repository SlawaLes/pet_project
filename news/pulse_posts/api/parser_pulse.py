from .pulse import load_posts
from pulse_posts.models import Investor, Instrument


def create_investor(nickname, profile_tinkoff):
    Investor.objects.update_or_create(nickname=nickname, profile_tinkoff=profile_tinkoff)

def create_instrument(ticker, name, type):
    Instrument.objects.update_or_create(
        ticker=ticker,
        name=name,
        type=type
    )

def investor_pars(posts: list) -> list:
    invs_stay = []
    for post in posts:
        invs_stay.append(
            Investor.objects.get(
            nickname=post['nickname']
            ).values('nickname')
        )
    return invs_stay