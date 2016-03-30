""" Common SurSys Exceptions"""

__author__ = "Gokhan MANKARA"
__email__ = "gokhan@mankara.org"


class BaseException(Exception):
    pass

class WrongInterfaceName(Exception):
    pass

class NotValidIPv4Address(Exception):
    pass
