# universities

[![PyPI](https://img.shields.io/pypi/v/universities.svg?style=flat-square)](https://pypi.python.org/pypi/universities)

Python package to search for basic university information. This packages obtains information from [Hipo/university-domains-list](https://github.com/Hipo/university-domains-list)'s database. It is fully compatible with Python 2.6 and up.

## Installation

Your preference should be to use PyPi: `pip install universities`

Source and wheel distributions are available in the releases tab as well.

## Usage

```python
import universities

uni = universities.API() # can specify encoding for use in Python 2

canadian = uni.search(country = "Canada")
only_mit = uni.search(domain = "mit.edu")
all_data = uni.get_all()
waterloo = uni.lucky(name = "Waterloo") # As in "I'm feeling lucky"
```

## Available Functions

 - `universities.search` searches the entire database for universities matching the specified critera. You may filter by `name`, `domain` or `country` as arguments to `search`. This returns a list of `universities.models.University` objects.
 - `universities.lucky` is an alias for `search` which only returns the first result of the search. All the same parameters are available, and a single `universities.models.University` is returned.
 - `universities.get_all` returns all of the entries in the database, in the same format as `search`. In fact, this is simply an alias for `search` that uses no arguments.

 Any query which reurns multiple objects will return a Generator.

## Models

 - `universities.models.University` is the basic model returned in all requests. It contains six fields:
   - `name`: The name of the university.
   - `domains`: A list of domain names the university uses (for emails, etc).
   - `web_pages`: A list of web pages associated with the university.
   - `country_code`: The two-letter ISO-3166 country code where the university is located.
   - `stateprov`: The state or province the university is located. This is usually not populated.
   - `country`: The full country name where the university is located.

## Requirements

The only requirement is `requests`.

## Development

1. Clone/fork the git repository.
2. `cd` to the directory and install the requirements if necessary: `pip install -r requirements.txt`
3. Edit to your heart's content!
4. If you wish to contribute, push your changes to GitHub on your own fork and make a pull request.

Note: Any contributions should be made following the PEP8 standard.