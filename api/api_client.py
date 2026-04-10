import requests

from urls import Urls
from utils import helpers


class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def post(self, url, payload, headers=None):
        return self.session.post(self.base_url + url, data=payload, headers=headers)

    def delete(self, url, headers):
        return self.session.delete(self.base_url + url, headers=headers)

    def create_user(self, payload):
        return self.post(Urls.CREATE_USER, payload)

    def delete_user(self, token):
        return self.delete(Urls.DELETE_USER, headers={"Authorization": token})
