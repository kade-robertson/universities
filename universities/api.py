import json
import requests
import warnings
from .models import University


def _deprecated(msg):
    warnings.simplefilter('always')
    warnings.warn(msg, category=DeprecationWarning, stacklevel=2)
    warnings.simplefilter('default')


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
        self.session = requests.Session()

    def search(self, name="", domain="", country_code="", country=""):
        """
        Search for a university in the database. Each available option
        can be used to narrow down saerch results.

        :param str name: The name of the university.
        :param str domain: The domain the university uses.
        :param str country_code: DEPRECATED, DOES NOTHING
        :param str country: The country of the university.
        :rtype: generator of models.University objects
        """
        parameters = dict()
        if any([name, domain, country_code, country]):
            if name:
                parameters["name"] = name
            if domain:
                parameters["domain"] = domain
            if country_code:
                _deprecated("Country code filters have no function for now.")
                parameters["alpha_two_code"] = country_code
            if country:
                parameters["country"] = country
        university_data = self.session.get(
            self.endpoint,
            params=parameters
        ).json()
        for data in university_data:
            yield University(self.encoding, json=data)

    def lucky(self, name="", domain="", country_code="", country=""):
        """
        Search for a university in the database, and only return the
        first result. This is simply a wrapper on search() that takes
        the resulting generator and returns the first element if it
        exists. Each available option can be used to narrow down search
        results.

        :param str name: The name of the university.
        :param str domain: The domain the university uses.
        :param str country_code: DEPRECATED, DOES NOTHING
        :param str country: The country of the university.
        :rtype: A models.University object
        """
        attempt = self.search(name, domain, country_code, country)
        try:
            return next(attempt)
        except StopIteration:
            return None

    def get_all(self):
        """
        Return a generator containing all university data. This is
        simply a wrapper on search() which does not do any filtering.

        :rtype: generator of models.University objects
        """
        return self.search()

    def __del__(self):
        self.session.close()
