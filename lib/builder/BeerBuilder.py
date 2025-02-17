from lib.model.Beer import Beer


class BeerBuilder:
    def __init__(self):
        self.name = None
        self.price = None
        self.rating_avg = None
        self.rating_reviews = []
        self.image = None

    def set_name(self, name):
        self.name = name
        return self

    def set_price(self, price):
        self.price = price
        return self

    def set_rating_avg(self, rating_avg):
        self.rating_avg = rating_avg
        return self

    def set_image(self, image):
        self.image = image
        return self

    def add_rating_review(self, rating_review):
        self.rating_reviews.append(rating_review)
        return self

    def build(self):
        if not self.name or not self.price:
            raise ValueError("Name and price are required for a beer")
        return Beer(self.name, self.price, self.rating_avg, self.rating_reviews, self.image)