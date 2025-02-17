from lib.model.Drink import Drink


class Beer(Drink):

    def __init__(self, name, price, rating_avg, rating_reviews, image):
        self.name = name
        self.price = price
        self.rating_avg = rating_avg
        self.rating_reviews = rating_reviews
        self.image = image

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "rating_avg": self.rating_avg,
            "rating_reviews": self.rating_reviews,
            "image": self.image
        }