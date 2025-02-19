from lib.api.Api import Api


class CocktailApi(Api):

    BASE_URL = 'https://www.thecocktaildb.com/api/json/v1/1'

    def __init__(self, endpoint):
        super().__init__(f'{self.BASE_URL}{endpoint}')