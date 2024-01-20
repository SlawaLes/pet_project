import requests

IAM_TOKEN = 't1.9euelZqYm5WQz4yMnJvGyMfIyMyUme3rnpWaz4mcnpPKy5HPjpiXxpKNk5bl8_c7G1FS-e8nYEQr_t3z93tJTlL57ydgRCv-zef1656Vms2KipvPm46dipabyJSTkMvP7_zF656Vms2KipvPm46dipabyJSTkMvP.k3yOFkySyGJ3wUe92qXSPgF_G5zHe567sGQmI7fq-7wjlN4FGlILbeFFWs4FzLr8oLCiGAgFAz5rOoAgm6gaDw'

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

