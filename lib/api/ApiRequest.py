import requests


class ApiRequest:

    def __init__(self, base_url):
        self.base_url = base_url

    def call_api(self):
        return requests.get(self.base_url)

