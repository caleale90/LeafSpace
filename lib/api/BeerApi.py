from lib.api.Api import Api


class BeerApi(Api):

    def __init__(self, base_url):
        super().__init__(base_url)