from lib.api.ApiRequest import ApiRequest


class BeerApiRequest(ApiRequest):

    def __init__(self, base_url):
        super().__init__(base_url)