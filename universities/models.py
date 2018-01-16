class University(object):
    """University object to hold information on a university."""

    def __init__(self, encoding, **kwargs):
        """
        Initialize a new University object, through a variety of ways.
        If a json argument is provided, data will be read from a dict
        that should be identical in structure to the database's data.
        Otherwise, the arguments should be named just as the variables
        are named. If the version is detected as being Python 2, the
        data is encoded properly to avoid errors.

        :params str encoding: String encoding to use with Python 2
        :params dict json: Dictionary containing class data.
        :params str **kwargs: Data to be used if json not provided.
        """
        if "json" in kwargs.keys():
            json = kwargs.get('json')
            self.name = json['name']
            self.domains = json['domains']
            self.web_pages = json['web_pages']
            self.country_code = json['alpha_two_code']
            self.stateprov = json['state-province']
            self.country = json['country']
        else:
            self.name = kwargs.get('name')
            self.domains = kwargs.get('domains')
            self.web_pages = kwargs.get('web_pages')
            self.country_code = kwargs.get('country_code')
            self.stateprov = kwargs.get('stateprov')
            self.country = kwargs.get('country')
        import sys
        if sys.version_info[0] == 2:
            self.name = self.name.encode(encoding)
            self.country_code = self.country_code.encode(encoding)
            if self.stateprov is not None:
                self.stateprov = self.stateprov.encode(encoding)
            self.country = self.country.encode(encoding)

    def __repr__(self):
        out = "{0}.{1}(name={2}, domains={3}, web_pages={4}, " + \
              "country_code={5}, stateprov={6}, country={7})"
        return out.format(
            type(self).__module__,
            type(self).__name__,
            "'{0}'".format(self.name) if self.name else None,
            self.domains,
            self.web_pages,
            "'{0}'".format(self.country_code) if self.country_code else None,
            "'{0}'".format(self.stateprov) if self.stateprov else None,
            "'{0}'".format(self.country) if self.country else None
        )

    def __str__(self):
        out = "Name: {0}\n".format(self.name)
        if self.stateprov:
            out += "State: {0}\n".format(self.stateprov)
        out += "Country: {0}\n".format(self.country)
        if self.domains:
            out += "Domains:\n"
            for domain in self.domains:
                out += " - {0}\n".format(domain)
        if self.web_pages:
            out += "Web Pages:\n"
            for webpage in self.web_pages:
                out += " - {0}\n".format(webpage)
        return out
