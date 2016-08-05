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

    @property
    def hostname(self):
        """ Return String System Hostname """
        return socket.gethostname()

    @property
    def kernel_version(self):
        """ Return String, System Current Kernel Version"""
        return platform.release()
    
    @property
    def cpu_info(self):
        """ CPU Model Information

            Return string
        """
        cpu_info =  platform.processor()

        if len(cpu_info) != 0:
            return cpu_info

    @property
    def ntp_host(self):
        """
            Return: NTP server default host name
        """
        return self.host

    @ntp_host.setter
    def ntp_host(self, new_host):
        """
            You can change self.host ntp server host
            Return: New NTP Server Host Name
        """
        self.host = new_host

        return self.host

    @property
    def ntp_current_time(self):
        """
            Connected self.host ntp server
            Return: YYYY MM DD HH:MM:SS Time Format
        """
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
        """
            System Current Time
            Return: YYYY MM DD HH:MM:SS Time Format
        """
        now = datetime.datetime.now()
        c_t = datetime.datetime.strftime(now, '%Y %m %d %H:%M:%S')

        return c_t

    @property
    def uptime(self):
        """
            System Uptime 
            Return: str 'HH:MM:SS' 
        """
        with open('/proc/uptime', 'r') as f:
            up_s = float(f.readline().split()[0].split('.')[0])
            up_str = str(datetime.timedelta(seconds=up_s))
        f.close()

        return up_str

    def pid(self, process_name):
        """
            process_name: System Process Name
            return: Process name's pid, integer
        """
        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=['pid', 'name'])
                p_name = pinfo['name']
                p_pid = pinfo['pid']

                if process_name == p_name:
                    return p_pid

            except psutil.NoSuchProcess:
                pass
    

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

