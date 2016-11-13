import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "psystem",
    version = "0.1.1",
    author = "Gokhan Mankara",
    author_email = "gokhan@mankara.org",
    description = ("Linux System Python Module"),
    license = "GNU GENERAL PUBLIC LICENSE",
    keywords = "linux system",
    url = "",
    packages=['psystem', 'test'],
    long_description=read('README.md'),
)
