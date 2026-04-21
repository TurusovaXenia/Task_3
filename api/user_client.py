from api.api_client import ApiClient
from urls import Urls


class UserClient(ApiClient):
    def create_user(self, payload):
        return self.post(Urls.CREATE_USER, payload)

    def delete_user(self, token):
        return self.delete(Urls.DELETE_USER, headers={"Authorization": token})
