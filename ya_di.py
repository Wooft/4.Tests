import requests
from pprint import pprint


class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def create_folder(self, folder_name):
        url = f'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': folder_name}
        headers = self.get_headers()
        response = requests.put(url, headers=headers, params=params)
        print(response.status_code)
        return response.json()

    def get_folders(self):
        pass