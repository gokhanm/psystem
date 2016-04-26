import unittest

from psystem import stats

__author__ = "Gokhan MANKARA"
__email__ = "gokhan@mankara.org"


class TestStats(unittest.TestCase):

    def test_memory_usage(self):

        gt = stats.Get()
        memory_info = gt.memory

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

        gt = stats.Get()

        disk_info = gt.disk

        for k, v in disk_info.items():

            self.assertIsInstance(v, dict)
        
            self.assertIsInstance(v['total'], str)
            self.assertIsInstance(v['used'], str)
            self.assertIsInstance(v['free'], str)
            self.assertIsInstance(v['percent'], float)

    def test_cpu_percent_usage(self):

        gt = stats.Get()

        cpu_usage = gt.cpu()

        self.assertIsInstance(cpu_usage, float)

        cpu_per_usage = gt.cpu(percpu=True)

        self.assertIsInstance(cpu_per_usage, list)        

    def test_network_statistics(self):

        gt = stats.Get()

        n_stats = gt.network()

        self.assertIsInstance(n_stats, dict)

        all_n_stats = gt.network(all_interface=True)

        self.assertIsInstance(all_n_stats, dict)



if __name__ == '__main__':
    unittest.main()
