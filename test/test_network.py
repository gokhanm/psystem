import unittest

from psystem import network
from psystem.errors import *

__author__ = "Gokhan MANKARA"
__email__ = "gokhan@mankara.org"

warnings.simplefilter("ignore", ResourceWarning)


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

    def test_is_up(self):

        get = network.Get()
        result = get.is_up('eth0')

        self.assertIsInstance(result, bool)

    def test_wrong_typo_interface_name_exception(self):
        get = network.Get()

        self.assertRaises(ValueError, get.ip, 'ethh1')

    def test_set_ip(self):
        st = network.Set()
        get = network.Get()

        set_ip = st.ip('eth0', '10.41.0.164')
        current_ip = get.ip('eth0')[0]['addr']

        self.assertEqual(current_ip, '10.41.0.164')

    def test_false_interface_name_set_ip(self):
        st = network.Set()

        self.assertRaises(WrongInterfaceName, st.ip, 'eth', '10.41.0.164')

    def test_not_valid_ipv4_address_set(self):
        st = network.Set()

        self.assertRaises(NotValidIPv4Address, st.ip, 'eth0', '10.41.0')

if __name__ == '__main__':
    unittest.main()
