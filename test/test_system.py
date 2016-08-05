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

    def test_ntp_current_time(self):
        gt = system.Get()
        current_time = gt.ntp_current_time
        self.assertIsInstance(current_time, str)

    def test_current_time(self):
        gt = system.Get()
        t = gt.current_time
        self.assertIsInstance(t, str)

    def test_uptime(self):
        gt = system.Get()
        uptime = gt.uptime
        self.assertIsInstance(uptime, str)

    def test_pid(self):
        gt = system.Get()
        pid = gt.pid('crypto')
        self.assertIsInstance(pid, int)


if __name__ == '__main__':
    unittest.main()
