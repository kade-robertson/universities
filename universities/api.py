import json
import requests
from .models import University


class API(object):
    """API object for making requests to the university database."""

    endpoint = r"http://universities.hipolabs.com/search"

    def __init__(self, encoding='utf-8'):
        """
        Initialize the API object, optionally specifying the encoding
        to use for Python 2.

        :param str encoding: encoding to use when using Python 2
        """
        self.encoding = encoding

    def search(self, name="", country_code="", country=""):
        """
        Search for a university in the database. Each available option
        can be used to narrow down saerch results.

        :param str name: The name of the university.
        :param str country_code: An ISO-3166 2-letter country code.
        :param str country: The country of the university.
        :rtype: generator of models.University objects
        """
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
        """
        Search for a university in the database, and only return the
        first result. This is simply a wrapper on search() that takes
        the resulting generator and returns the first element if it
        exists. Each available option can be used to narrow down search
        results.

        :param str name: The name of the university.
        :param str country_code: An ISO-3166 2-letter country code.
        :param str country: The country of the university.
        :rtype: A models.University object
        """
        attempt = self.search(name, country_code, country)
        try:
            return next(attempt)
        except StopIteration:
            return None
        return None

    def get_all(self):
        """
        Return a generator containing all university data. This is
        simply a wrapper on search() which does not do any filtering.

        :rtype: generator of models.University objects
        """
        return self.search()
