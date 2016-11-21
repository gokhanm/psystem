import unittest

from psystem import shell

__author__ = 'Gokhan MANKARA'
__email__ = 'gokhan@mankara.org'


class ShellTestCase(unittest.TestCase):
    def test_local_shell(self):
        local_shell = shell.Local()
        result = local_shell.run(['echo', '-n', 'hello'])

        self.assertEqual(result, 'hello')



if __name__ == '__main__':
    unittest.main()
