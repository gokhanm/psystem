""" Common Network Settings """
import netifaces
import socket
import struct
import ctypes
import fcntl
import socket
import validators

from psystem.errors import *


__author__ = "Gokhan MANKARA"
__email__ = "gokhan@mankara.org"


# From linux/sockios.h
SIOCSIFNETMASK = 0x891C
SIOCSIFADDR = 0x8916
SIOCGIFFLAGS = 0x8913

# From linux/if.h
IFF_UP       = 0x1

# From linux/socket.h
AF_UNIX      = 1
AF_INET      = 2


class Get:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def interfaces(self):
        """
            return: Network Interfaces List
        """
        return netifaces.interfaces()

    def ip(self, interface):
        """
            interface: str, Interface Name
            return: Interface Ip Information in List.
                    [{'broadcast': '10.100.0.255', 'addr': '10.100.0.164', 'netmask': '255.255.255.0'}]
        """
        
        addrs = netifaces.ifaddresses(interface)

        return addrs[netifaces.AF_INET]

    def mac(self, interface):
        """
            interface: str , Interface Name
            return: Interface Mac Addresse in List
                    [{'addr': '00:12:34:56:78:9a'}]

        """
        addrs = netifaces.ifaddresses(interface)

        return addrs[netifaces.AF_LINK]

    def default_gateway(self):
        """
            return: tuple, Default Interface Gateway
        """
        gws = netifaces.gateways()
        return gws['default'][netifaces.AF_INET]

    def all_gateways(self):
        """
            return: dict, List of gateways on machine.
        """
        return netifaces.gateways()

    def is_up(self, interface_name):
        ''' Return True if the interface is up, False otherwise. '''
        
        ifname = interface_name.encode(encoding='UTF-8')

        # Get existing device flags
        ifreq = struct.pack('16sh', ifname, 0)
        flags = struct.unpack('16sh', fcntl.ioctl(self.sock, SIOCGIFFLAGS, ifreq))[1]

        # Set new flags
        if flags & IFF_UP:
            return True
        else:
            return False


class Set:
    
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def ip(self, interface_name, newip):
        """
            Checking interface first, if interface name found in Get().interfaces()
            validating Ipv4. After that applied ip address to interface

            interface_name: Applied Interface
            newip: New Ip Address

        """

        interface_check = Get().interfaces()

        valid_ipv4 = validators.ipv4(newip)

        if not interface_name in interface_check:
            raise WrongInterfaceName("Wrong Interface Name %s" % interface_name)

        elif not valid_ipv4 is True:
            raise NotValidIPv4Address("Not Valid IPv4 Address %s" % newip)

        else:
            ifname = interface_name.encode(encoding='UTF-8')

            ipbytes = socket.inet_aton(newip)
            ifreq = struct.pack('16sH2s4s8s', ifname, AF_INET, b'\x00'*2, ipbytes, b'\x00'*8)
            fcntl.ioctl(self.sock, SIOCSIFADDR, ifreq)

    def netmask(self, interface_name, netmask):
        interface_check = Get().interfaces()

        valid_ipv4 = validators.ipv4(newip)

        if not interface_name in interface_check:
            raise WrongInterfaceName("Wrong Interface Name %s" % interface_name)

        elif not valid_ipv4 is True:
            raise NotValidIPv4Address("Not Valid IPv4 Address %s" % newip)

        else:
            ifname = interface_name.encode(encoding='UTF-8')

            netmask = ctypes.c_uint32(~((2 ** (32 - netmask)) - 1)).value
            nmbytes = socket.htonl(netmask)
            ifreq = struct.pack('16sH2sI8s', ifname, AF_INET, b'\x00'*2, nmbytes, b'\x00'*8) 
            fcntl.ioctl(self.sock, SIOCSIFNETMASK, ifreq)


