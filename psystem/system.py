import datetime
import socket
import struct
import time
import sys
import syslog
import os
import platform
import psutil


__author__ = "Gokhan MANKARA"
__email__ = "gokhan@mankara.org"


class Get:
    def __init__(self):
        self.host = "pool.ntp.org"

    def hr(self, byt):
        """
            Convert byte to human readable
        """
        
        suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']

        if byt == 0:
            return '0'

        i = 0
        while byt >= 1024 and i < len(suffixes)-1:
            byt /= 1024.
            i += 1
        f = ('%.2f' % byt).rstrip('0').rstrip('.')
        return '%s %s' % (f, suffixes[i])

    @property
    def hostname(self):
        """ Return String System Hostname """

        return socket.gethostname()

    @property
    def kernel_version(self):

        """ Return String, System Current Kernel Version"""
        
        return platform.release()
    
    @property
    def memory_usage(self):
        """ 
            System virtual memory and swap usage 
            Converting byte to mb and rounded result
            
            Return dict
        
        """
        mem = psutil.virtual_memory()
        mem_total = self.hr(mem.total)
        mem_used = self.hr(mem.used)
        mem_free = self.hr(mem.free)
        mem_percent = mem.percent

        swap_mem = psutil.swap_memory()

        swap_total = self.hr(swap_mem.total)
        swap_used = self.hr(swap_mem.used)
        swap_free = self.hr(swap_mem.free)
        swap_percent = swap_mem.percent

        mem = {
                'virtual': {
                            'total': mem_total,
                            'used': mem_used,
                            'free': mem_free,
                            'percent': mem_percent
                            },
                'swap': {
                            'total': swap_total,
                            'used': swap_used,
                            'free': swap_free,
                            'percent': swap_percent
                        }
                }

        return mem

    def cpu_percent_usage(self, percpu=False):
        """ 
            System cpu usage

            if percpu is True, return per cpu usage in list
            if percpu is False, return cpu usage float
        """
        
        if percpu:
            cpu_percent = psutil.cpu_percent(interval=0, percpu=True)
        else:
            cpu_percent = psutil.cpu_percent(interval=0)

        return cpu_percent

    @property
    def cpu_info(self):
        """ CPU Model Information

            Return string
        """

        cpu_info =  platform.processor()

        if len(cpu_info) != 0:
            return cpu_info
        # else:
        #     pass

    def partition_usage(self, partition):
        """
            System disk partition usage

            Return psutil class
        """
        usage = psutil.disk_usage(str(partition))

        return usage

    @property
    def disk_partitions(self):
        """ 
            System disk partitions

            Return list
        """

        partitions = psutil.disk_partitions()

        return partitions

    @property
    def disk_usage(self):

        """
            Per system partition disk usage on system
            Converting byte to human readable format
            
            Return dict
        """
        
        disk_info = {}

        parts = self.disk_partitions

        for i in parts:
            part = i.mountpoint
            part_usage = self.partition_usage(part)

            total = self.hr(part_usage.total)
            used = self.hr(part_usage.used)
            free = self.hr(part_usage.free)
            percent = part_usage.percent
            
            disk_info[part] = {
                                "total": total,
                                "used": used,
                                "free": free,
                                "percent": percent
                              }

        return disk_info

    @property
    def ntp_host(self):
        return self.host

    @ntp_host.setter
    def ntp_host(self, new_host):
        self.host = new_host
        return self.host

    @property
    def ntp_current_time(self):
        port = 123
        buf = 1024
        address = (self.host, port)
        msg = bytes('\x1b' + 47 * '\0', 'UTF-8')

        # reference time
        ref_time = 2208988800 # 1970-01-01 00:00:00

        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client.sendto(msg, address)
        msg, address = client.recvfrom(buf)

        t = struct.unpack("!12I", msg)[10]

        t -= ref_time

        return time.strftime('%Y %m %d %H:%M:%S', time.gmtime(t))

    @property
    def current_time(self):

        now = datetime.datetime.now()
        c_t = datetime.datetime.strftime(now, '%Y %m %d %H:%M:%S')

        return c_t
    

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

