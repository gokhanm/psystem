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

    @property
    def interfaces(self):
        """
            Network Interfaces
            Return List
        """
        return netifaces.interfaces()

    def ip(self, interface_name):
        """
            interface: str, Interface Name
            return: List
                    [{'broadcast': '10.100.0.255', 'addr': '10.100.0.164', 'netmask': '255.255.255.0'}]
        """
        interface_check = self.interfaces

        if not interface_name in interface_check:
            raise WrongInterfaceName("Wrong Interface Name %s" % interface_name)
        
        addrs = netifaces.ifaddresses(interface_name)

        return addrs[netifaces.AF_INET]

    def mac(self, interface_name):
        """
            interface: str , Interface Name
            return: List
                    [{'addr': '00:12:34:56:78:9a'}]

        """
        interface_check = self.interfaces

        if not interface_name in interface_check:
            raise WrongInterfaceName("Wrong Interface Name %s" % interface_name)

        addrs = netifaces.ifaddresses(interface_name)

        return addrs[netifaces.AF_LINK]

    @property
    def default_gateway(self):
        """
            Default Interface Gateway
            Return: tuple
        """

        gws = netifaces.gateways()

        try:
            return gws['default'][netifaces.AF_INET]
        except KeyError:
            return gws['default'][netifaces.AF_INET6]
            
    @property
    def all_gateways(self):
        """
            List of gateways on machine.
            Return: dict
        """
        return netifaces.gateways()

    def is_up(self, interface_name):
        ''' Return True if the interface is up, False otherwise. '''

        interface_check = self.interfaces

        if not interface_name in interface_check:
            raise WrongInterfaceName("Wrong Interface Name %s" % interface_name)
        
        ifname = interface_name.encode(encoding='UTF-8')

        # Get existing device flags
        ifreq = struct.pack('16sh', ifname, 0)
        flags = struct.unpack('16sh', fcntl.ioctl(self.sock, SIOCGIFFLAGS, ifreq))[1]

        # Set new flags
        if flags & IFF_UP:
            return True
        else:
            return False

    def netmask(self, interface_name):
        """ 
            interface_name = str, Interface Name
            Return: str

        """

        interface_check = self.interfaces

        if not interface_name in interface_check:
            raise WrongInterfaceName("Wrong Interface Name %s" % interface_name)

        ip_list = self.ip(interface_name)

        netmask = ip_list[0]['netmask']

        return netmask


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

        interface_check = Get().interfaces

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

    def get_net_size(self, netmask):
        """ 
            Calculate network prefix len

            netmask: iterator like ['255', '255', '255', '0']
            return: int
        """

        binary_str = ""
        
        for octet in netmask:
            binary_str += bin(int(octet))[2:].zfill(8)

        return len(binary_str.rstrip('0'))

    def netmask(self, interface_name, netmask):
        """
            Checking interface first, if interface name found in Get().interfaces()
            validating Ipv4. After that applied ip address to interace

            interface_name = Applied Interface
            netmask = New netmask ip address
        """

        interface_check = Get().interfaces

        valid_ipv4 = validators.ipv4(netmask)

        if not interface_name in interface_check:
            raise WrongInterfaceName("Wrong Interface Name %s" % interface_name)

        elif not valid_ipv4 is True:
            raise NotValidIPv4Address("Not Valid IPv4 Address %s" % netmask)

        else:

            prefix_len = self.get_net_size(netmask.split('.'))

            ifname = interface_name.encode(encoding='UTF-8')

            netmask = ctypes.c_uint32(~((2 ** (32 - prefix_len)) - 1)).value
            nmbytes = socket.htonl(netmask)
            ifreq = struct.pack('16sH2sI8s', ifname, AF_INET, b'\x00'*2, nmbytes, b'\x00'*8) 
            fcntl.ioctl(self.sock, SIOCSIFNETMASK, ifreq)

