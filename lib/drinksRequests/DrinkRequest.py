class DrinkRequest:

    def get_random(self):
        response = self.random_api_call()
        print(response.json())
        return self.build_drink(response.json())

    def search_by_letter(self, letter):
        response = self.search_by_letter_call()
        print(response.json())
        return self.build_drink(response.json())

    def random_api_call(self):
        raise NotImplementedError('Override in sub-classes')

    def search_by_letter_call(self):
        raise NotImplementedError('Override in sub-classes')

    def build_drink(self, response):
        raise NotImplementedError('Override in sub-classes')



