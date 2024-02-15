import time
import httpx
from tpulse import TinkoffPulse
from math import ceil

def load_posts(ticker, number_posts):
    pulse = TinkoffPulse()
    cursor = 999999999
    KEYS = ["nickname",
            "profileId",
            "likesCount",
            "commentsCount",
            "inserted",
            "text",
            "instruments"]
    raw_data = []
    batches = ceil(number_posts/30)
    for i in range(batches):
        try:
            response = pulse.get_posts_by_ticker(ticker=ticker, cursor=cursor)
            if not response:
                return None
            cursor = response['nextCursor']
            posts = response['items']
            for post in posts:
                data = {
                    key: post[f'{key}'] for key in KEYS
                }
                data['text'] = post['content']['text']
                data['reactions'] = post['reactions']['totalCount']
                raw_data.append(data)
            if not response['hasNext']:
                return raw_data if len(raw_data) < number_posts else raw_data[:number_posts]
        except httpx.HTTPError:
            pass
        time.sleep(0.01)
    return raw_data[:number_posts]
