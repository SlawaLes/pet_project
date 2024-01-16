import requests

IAM_TOKEN = 't1.9euelZrNjMzOz4_GzJuSiZuezceJje3rnpWaz4mcnpPKy5HPjpiXxpKNk5bl8_coPWlS-e8-PTV1_t3z92hrZlL57z49NXX-zef1656VmsfGzpaVyoyVmoqMjsuPyczP7_zF656VmsfGzpaVyoyVmoqMjsuPyczP.P1wZbVs8yFqjEonmnvXUUZwemKRi2TtKxVGm0hPMKz9N7hnmoPh8ou-i-m6cVb7WMFG0GAl0XoZwmhi424tFBQ'
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

