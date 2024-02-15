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

