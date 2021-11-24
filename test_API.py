import requests
import pytest


token = [('AQAAAAADVkwOAAdea6y8enLE0U0wq7KTdA6dD_w')]


@pytest.mark.parametrize('token', token)
class TestApi:

    def test_api_test_create_folder(self, token):
        response = requests.put('https://cloud-api.yandex.net:443/v1/disk/resources',
                                headers={"Content-Type": "application/json",
                                         "Authorization": f"OAuth {token}"},
                                params={'path': '/Просто папка'})
        assert response.status_code == 201 or response.status_code == 409

    def test_api_test_check_folder(self, token):
        response = requests.get('https://cloud-api.yandex.net:443/v1/disk/resources',
                                headers={"Content-Type": "application/json",
                                         "Authorization": f"OAuth {token}"},
                                params={'path': '/Просто папка'})
        assert response.status_code == 200

