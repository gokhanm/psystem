import unittest

from psystem import network

__author__ = "Gokhan MANKARA <gokhan@mankara.org>"


class NetworkTestCase(unittest.TestCase):

    def test_get_interfaces(self):
        get = network.Get()
        interfaces = get.interfaces()
        self.assertIsInstance(interfaces, list)
        return interfaces

    def test_get_ip(self):
        get = network.Get()

        interface_list = self.test_get_interfaces()
        
        for i in interface_list:
            interface_addrs = get.ip(i)
            self.assertIsInstance(interface_addrs, list)

    def test_get_mac(self):
        get = network.Get()
        interface_list = self.test_get_interfaces()

        for i in interface_list:
            interface_mac = get.mac(i)
            self.assertIsInstance(interface_mac, list)

    def test_get_default_gateway(self):
        get = network.Get()
        default_gw = get.default_gateway()
        self.assertIsInstance(default_gw, tuple)

    def test_all_getaways(self):
        get = network.Get()

        all_gw = get.all_gateways()
        self.assertIsInstance(all_gw, dict)

    def test_wrong_typo_interface_name_exception(self):
        get = network.Get()

        self.assertRaises(ValueError, get.ip, 'ethh1')


if __name__ == '__main__':
    unittest.main()
