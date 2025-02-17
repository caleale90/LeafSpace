from lib.api.ApiRequest import ApiRequest


class CocktailApiRequest(ApiRequest):

    def __init__(self, base_url):
        super().__init__(base_url)