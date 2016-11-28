import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "psystem",
    version = "0.2.0",
    author = "Gokhan Mankara",
    author_email = "gokhan@mankara.org",
    description = ("Linux System Python Module"),
    license = "GNU GENERAL PUBLIC LICENSE",
    keywords = ["linux system", "network", "mail", "shell", "log"],
    url = "https://github.com/gokhanm/psystem",
    packages=['psystem', 'test'],
    long_description=read('README.md'),
    install_requires=list(filter(None, [
        'netifaces',
        'pyroute2',
        'validators',
        'psutil',
        'spur',
    ])),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: GNU License',
        'Topic :: System :: Systems Administration',

    ]
)
