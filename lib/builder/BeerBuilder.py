from lib.model.Beer import Beer


class BeerBuilder:
    def __init__(self):
        self.name = None
        self.tagline = None
        self.image = None

    def set_name(self, name):
        self.name = name
        return self

    def set_tagline(self, tagline):
        self.tagline = tagline
        return self

    def set_image(self, image):
        self.image = image
        return self

    def build(self):
        if not self.name or not self.tagline:
            raise ValueError("Name and tagline are required for a beer")
        return Beer(self.name, self.tagline, self.image)