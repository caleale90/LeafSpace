class DrinkRequest:

    def get_random(self):
        return self.perform(self.random_api_call)

    def search_by_letter(self, letter):
        return self.perform(self.search_by_letter_call, letter)

    def perform(self, api_call_fn, *args, **kwargs):
        response = api_call_fn(*args, **kwargs)
        print(response.json())
        return self.build_drink(response.json())

    def random_api_call(self):
        raise NotImplementedError('Override in sub-classes')

    def search_by_letter_call(self, letter):
        raise NotImplementedError('Override in sub-classes')

    def build_drink(self, response):
        raise NotImplementedError('Override in sub-classes')



