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
        memory_info = gt.memory_usage

        self.assertIsInstance(memory_info['virtual'], dict)
        self.assertIsInstance(memory_info['swap'], dict)

        self.assertIsInstance(memory_info['virtual']['percent'], float)
        self.assertIsInstance(memory_info['virtual']['total'], str)
        self.assertIsInstance(memory_info['virtual']['free'], str)
        self.assertIsInstance(memory_info['virtual']['used'], str)

        self.assertIsInstance(memory_info['swap']['percent'], float)
        self.assertIsInstance(memory_info['swap']['total'], str)
        self.assertIsInstance(memory_info['swap']['free'], str)
        self.assertIsInstance(memory_info['swap']['used'], str)

    def test_disk_usage(self):

        gt = system.Get()

        disk_info = gt.disk_usage

        for k, v in disk_info.items():

            self.assertIsInstance(v, dict)
        
            self.assertIsInstance(v['total'], str)
            self.assertIsInstance(v['used'], str)
            self.assertIsInstance(v['free'], str)
            self.assertIsInstance(v['percent'], float)

    def test_cpu_percent_usage(self):

        gt = system.Get()

        cpu_usage = gt.cpu_percent_usage()

        self.assertIsInstance(cput_usage, float)

        cpu_per_usage = gt.cpu_percent_usage(percpu=True)

        self.assertIsInstance(cpu_percent_usage, list)



if __name__ == '__main__':
    unittest.main()
