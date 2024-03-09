from pulse_posts.models import Post
from django.db.models import Count
from calendar_holidays.models import Holidays


def get_data_form_graph(input_clean_data: dict):
    items, is_holiday = _validation_items(input_clean_data)
    filters = _filter_identify(items)
    valuse_list = _values_identify(items)
    if is_holiday:

        return (Post.objects.filter(**filters)
                .values(*valuse_list)
                .annotate(cnt=Count('id'))
                .order_by('inserted__date'))
    else:
        if not items['start']:
            queryset = Holidays.objects.all()
        else:
            start = items['start']
            queryset = Holidays.objects.filter(holiday__gte=start)
        holidays_lst = [item.holiday for item in queryset]

        return (Post.objects.filter(**filters)
                .values(*valuse_list)
                .exclude(inserted__date__in=holidays_lst)
                .annotate(cnt=Count('id'))
                .order_by('inserted__date'))



def _validation_items(dic: dict):
    res_dict = {}
    for i,j in dict(list(dic.items())[:-1]).items():
        if j == '' or j is None:
            res_dict[f'{i}'] = None
        else:
            res_dict[f'{i}'] = j
    return res_dict, dic['is_holiday']

def _filter_identify(dic: dict) -> dict:
    mapper = {
        'start': 'inserted__date__gte',
        'end': 'inserted__date__lte',
        'ticker': 'instrument__ticker',
        'investor': 'investor__nickname'
    }
    return {mapper[key]: dic[key] for key in dic if dic[key]}

def _values_identify(dic: dict) -> list:
    mapper = {
        'start': 'inserted__date',
        'end': 'inserted__date',
        'ticker': 'instrument__ticker',
        'investor': 'investor__nickname'
    }
    return list(set([mapper[key] for key in dic if dic[key]] + ['inserted__date']))
