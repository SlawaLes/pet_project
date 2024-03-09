import plotly.express as px
from pulse_posts.services.get_graph_data import _validation_items

default_clean = {
    'start': '',
    'end': '',
    'investor': '',
    'ticker': '',
    'is_holiday': True
}

def plot_graph(queryset, input_clean_data=default_clean):
    dt = queryset
    if not dt:
        return None
    else:
        graph = px.line(
            x=[item['inserted__date'] for item in dt],
            y=[item['cnt'] for item in dt],
            title=_get_title(input_clean_data),
            labels={'x': 'Дата', 'y': 'Кол-во постов'}
        )

        graph.update_layout(title={
            'font_size': 25,
            'xanchor': 'center',
            'x': 0.5
        })

        return graph.to_html()


def _get_title(input_clean_data):
    valid_data, is_holiday = _validation_items(input_clean_data)
    if not valid_data['investor']:
        if not valid_data['ticker']:
            return 'Посты по всем инструментам'
        ticker = valid_data['ticker']
        return f'Посты по инструменту {ticker}'
    else:
        if not valid_data['ticker']:
            investor = valid_data['investor']
            return f'Посты автора {investor} по всем инструментам'
        investor = valid_data['investor']
        ticker = valid_data['ticker']
        return f'Посты автора {investor} по инструменту {ticker}'