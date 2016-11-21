""" Common SurSys Exceptions"""
# Copyright 2016 Gokhan MANKARA <gokhan@mankara.org>


class BaseException(Exception):
    pass

class WrongInterfaceName(BaseException):
    pass

class NotValidIPv4Address(BaseException):
    pass

class Ipv6GateWayError(BaseException):
    pass

class EmailUnableRelay(BaseException):
    pass

class NotValidInterfaceName(BaseException):
    pass
