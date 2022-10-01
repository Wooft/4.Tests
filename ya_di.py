import json
import os
import pathlib

import requests

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
        return response.status_code

    def delete_folder(self, folder_n):
        url = f'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': folder_n, 'permanently': True}
        headers = self.get_headers()
        response = requests.delete(url, headers=headers, params=params)
        return  response.status_code

def get_path():
    path = pathlib.Path.cwd()
    return path

def get_token():
    os.chdir(get_path())
    with open('tokens.json', 'r') as file:
        data = json.load(file)
        token = data['yandex.drive']
    return token
def create_folder(folder_name):
    Yandex = YandexDisk(token=get_token())
    answer = Yandex.create_folder(folder_name=folder_name)
    return answer

def delete_folder(folder_name):
    Yandex = YandexDisk(token=get_token())
    answer = Yandex.delete_folder(folder_n=folder_name)
    return answer

if __name__ == '__main__':
    print(create_folder('Новая папка'))
    print(delete_folder('Новая папка'))