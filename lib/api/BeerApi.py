from lib.api.Api import Api


class BeerApi(Api):

    BASE_URL = 'https://punkapi.online/v3/beers'

    def __init__(self, endpoint):
        super().__init__(f'{self.BASE_URL}{endpoint}')