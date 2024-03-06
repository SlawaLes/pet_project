import requests
IAM_TOKEN = 't1.9euelZqWzp2ZnYqRxsfLmsrLjMySze3rnpWaz4mcnpPKy5HPjpiXxpKNk5bl9PcAcXBQ-e9oKXCA3fT3QB9uUPnvaClwgM3n9euelZrOlZCLnZjOxsidjMyejpTKku_8xeuelZrOlZCLnZjOxsidjMyejpTKkg.YSKfDeCQh7R4DHgOirgNOCOFj5wVTDo9vZBouupI5Z-dWlVhCvIaaGFwC56NQAHU-DfkwEchsG8xgb-e8v0KCg'
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

