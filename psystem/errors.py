""" Common SurSys Exceptions"""
# Copyright 2016 Gokhan MANKARA <gokhan@mankara.org>


class BaseException(Exception):
    pass

class WrongInterfaceName(Exception):
    pass

class NotValidIPv4Address(Exception):
    pass

class Ipv6GateWayError(Exception):
    pass

class EmailUnableRelay(Exception):
    pass
