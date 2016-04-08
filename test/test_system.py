import unittest

from psystem import system

__author__ = "Gokhan MANKARA"
__email__ = "gokhan@mankara.org"


class SystemTestCase(unittest.TestCase):

    def test_get_hostname(self):

        gt = system.Get()

        hostname = gt.hostname

        self.assertIsInstance(hostname, str)

    def test_set_hostname(self):

        st = system.Set()
        gt = system.Get()

        new_hostname = "local.local"

        st.hostname(new_hostname)

        current_hostname = gt.hostname

        self.assertEqual(new_hostname, current_hostname)

    def test_memory_usage(self):

        gt = system.Get()
        memory_info = gt.memory_info

        self.assertIsInstance(memory_info['virtual'], dict)
        self.assertIsInstance(memory_info['swap'], dict)

        self.assertIsInstance(memory_info['virtual']['percent'], float)
        self.assertIsInstance(memory_info['virtual']['total'], int)
        self.assertIsInstance(memory_info['virtual']['free'], int)
        self.assertIsInstance(memory_info['virtual']['used'], int)

        self.assertIsInstance(memory_info['swap']['percent'], float)
        self.assertIsInstance(memory_info['swap']['total'], int)
        self.assertIsInstance(memory_info['swap']['free'], int)
        self.assertIsInstance(memory_info['swap']['used'], int)


if __name__ == '__main__':
    unittest.main()
