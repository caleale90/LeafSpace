import json


class Drink:

    def to_dict(self):
        raise NotImplementedError('Override in sub-classes')

    def __str__(self):
        return json.dumps(self.to_dict())
