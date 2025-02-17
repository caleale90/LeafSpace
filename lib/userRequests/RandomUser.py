import requests

from lib.model.User import User


class RandomUser:

    def get(self):
        response = requests.get('https://randomuser.me/api/').json()
        user_data = response['results'][0]
        name = user_data['name']['first']
        timeshift = user_data['location']['timezone']['offset']
        return User(name, timeshift)