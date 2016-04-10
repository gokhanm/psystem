import socket
import syslog
import os
import platform
import psutil


__author__ = "Gokhan MANKARA"
__email__ = "gokhan@mankara.org"


class Get:

    @property
    def hostname(self):
        """ Return String System Hostname """

        return socket.gethostname()

    @property
    def kernel_version(self):

        """ Return system current kernel version"""
        
        return platform.release()
    
    def bytes2mb(self, n):
        return ( n / 1024 ) / 1024

    @property
    def memory_info(self):
        """ 
            Return system virtual memory and swap usage 
            Converting byte to mb and rounded result
        
        """
        mem = psutil.virtual_memory()
        mem_total = self.bytes2mb(mem.total)
        mem_used = self.bytes2mb(mem.used)
        mem_free = self.bytes2mb(mem.free)
        mem_percent = mem.percent

        swap_mem = psutil.swap_memory()

        swap_total = self.bytes2mb(swap_mem.total)
        swap_used = self.bytes2mb(swap_mem.used)
        swap_free = self.bytes2mb(swap_mem.free)
        swap_percent = self.bytes2mb(swap_mem.percent)

        mem = {
                'virtual': {
                            'total': round(mem_total),
                            'used': round(mem_used),
                            'free': round(mem_free),
                            'percent': mem_percent
                            },
                'swap': {
                            'total': round(swap_total),
                            'used': round(swap_used),
                            'free': round(swap_free),
                            'percent': swap_percent
                        }
                }

        return mem


class Set:

    def __init__(self):
        self.get = Get()
        self.hostname_file = '/etc/hostname'

    def __set_hostname(self, txt_file, new_hostname):
        """
            Running in hostname function. Find old hostname in /etc/hostname
            and replace with new hostname
            if hostname file is empty, new_hostname writing in file.
            if hostname file is not empty, using replace function for new_hostname and old_hostname
        """
        
        old_hostname = self.get.hostname

        f = open(txt_file, 'r')
        set_host = f.read()
        f.close()

        replace_hostname = set_host.replace(old_hostname, new_hostname)

        f = open(txt_file, 'w')

        if len(replace_hostname) == 0:
            f.write(new_hostname)
        else:
            f.write(replace_hostname)

        f.close()

    def hostname(self, new_hostname):
        """ Change system hostname """

        self.__set_hostname(self.hostname_file, new_hostname)

        os.system('/bin/hostname %s' % new_hostname)
        syslog.syslog

