import json
import requests
from .models import University

_endpoint = r"http://universities.hipolabs.com/search"

def search(name = "", country_code = "", country = ""):
    parameters = dict()
    if any([name, country_code, country]):
        if name: parameters["name"] = name
        if country_code: parameters["alpha_two_code"] = country_code
        if country: parameters["country"] = country
    university_data = requests.get(_endpoint, params = parameters)
    university_json = json.loads(university_data.text)
    return [University(json = data) for data in university_json]

def lucky(name = "", country_code = "", country = ""):
    attempt = search(name, country_code, country)
    if len(attempt) > 0:
        return attempt[0]
    return None

def get_all():
    return search()