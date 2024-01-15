import requests

IAM_TOKEN = 't1.9euelZrJxsiYms2TmY2Qx42bj8vJne3rnpWaz4mcnpPKy5HPjpiXxpKNk5bl8_cgDnFS-e8iJndI_N3z92A8blL57yImd0j8zef1656Vmo6Zj5mcipzGx5CNjYyamcaV7_zF656Vmo6Zj5mcipzGx5CNjYyamcaV.aeiaBObXJTA_kCrg-hftzoS1alQPHk_junV3hb7QglN440bSZkIQu8jXP_UPayEgE8CItGe5oMJM9En03F0KCQ'

folder_id = 'b1gbscfkoclv629e8m5a'
target_language = 'ru'

def translation(text):
    texts = [text, ]

    body = {
        "targetLanguageCode": target_language,
        "texts": texts,
        "folderId": folder_id,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {0}".format(IAM_TOKEN)
    }
    response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
                             json=body,
                             headers=headers
                             )
    return response.json()['translations'][0]['text']

