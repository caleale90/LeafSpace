from lib.model.Drink import Drink


class Beer(Drink):

    def __init__(self, name, tagline, image):
        self.name = name
        self.tagline = tagline
        self.image = image

    def to_dict(self):
        return {
            "name": self.name,
            "tagline": self.tagline,
            "image": self.image
        }