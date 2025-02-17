class DrinkRequest:

    def get_random(self):
        response = self.api_call()
        return self.build_drink(response.json())

    def api_call(self):
        raise NotImplementedError('Override in sub-classes')

    def build_drink(self, response):
        raise NotImplementedError('Override in sub-classes')
