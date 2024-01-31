import requests
IAM_TOKEN = 't1.9euelZrHm8fKysfOicydnMbJms6Lme3rnpWaz4mcnpPKy5HPjpiXxpKNk5bl8_c9HzpS-e9hUzBt_d3z931NN1L572FTMG39zef1656Vmo3Hk5COzZvIl83Gi53Nl83N7_zF656Vmo3Hk5COzZvIl83Gi53Nl83N.wohq0wMbHJNmc1IbshuwvAAaFkBfuL7sAHoVrT98j4E1RkQ5z9ade_qPRu2XHO26-iTOVTEKbbjlm4OevTj_Cg'
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

