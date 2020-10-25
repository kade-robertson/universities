from setuptools import setup, find_packages

long_desc = ""
try:
    import pypandoc
    long_desc = pypandoc.convert('README.md', 'rst', extra_args = ('--eol', 'lf'))
except(IOError, ImportError):
    long_desc = open('README.md').read()

setup(
    name = "universities",
    version = "1.1.0",
    description = "Search a large university database for basic information.",
    long_description = long_desc,
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy"
    ],
    keywords = "university data search api",
    author = "Kade Robertson",
    author_email = "kade@kaderobertson.pw",
    url = "https://github.com/kade-robertson/universities",
    license = "MIT",
    packages = find_packages(),
    install_requires = [
        "requests",
    ],
    python_requires = '>=2.6, <4',
)
