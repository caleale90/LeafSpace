
class User:

    def __init__(self, name, timeshift):
        self.name = name
        self.timeshift = timeshift

    def get_first_letter(self):
        return self.name[0].lower()

    def get_timeshift(self):
        return self.timeshift
