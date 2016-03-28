""" Common Network Settings """
import netifaces


__author__ = "Gokhan MANKARA <gokhan@mankara.org>"


class Get:
    def __init__(self):
        pass

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


class Set:
    def __init__(self):
        pass



