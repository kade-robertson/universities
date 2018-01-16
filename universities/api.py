import json
import requests
from .models import University


class API(object):

    self.endpoint = r"http://universities.hipolabs.com/search"

    def __init__(self, encoding='utf-8'):
        self.encoding = encoding

    def search(self, name="", country_code="", country=""):
        parameters = dict()
        if any([name, country_code, country]):
            if name:
                parameters["name"] = name
            if country_code:
                parameters["alpha_two_code"] = country_code
            if country:
                parameters["country"] = country
        university_data = requests.get(self.endpoint, params=parameters)
        university_json = json.loads(university_data.text)
        for data in university_json:
            yield University(self.encoding, json=data)

    def lucky(self, name="", country_code="", country=""):
        attempt = self.search(name, country_code, country)
        if len(attempt) > 0:
            return attempt[0]
        return None

    def get_all(self):
        return self.search()
