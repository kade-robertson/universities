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
    return list(map(University, university_json))

def get_all():
    return search()