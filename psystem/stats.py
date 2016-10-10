# Copyright 2016 Gokhan MANKARA <gokhan@mankara.org>

import psutil


class Get:
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
    def memory(self):
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

    def cpu(self, percpu=False):
        """ 
            System cpu usage

            if percpu is True, return per cpu usage in list
            if percpu is False, return cpu usage float
        """
        if percpu:
            cpu = psutil.cpu_percent(interval=0, percpu=True)
        else:
            cpu = psutil.cpu_percent(interval=0)

        return cpu    

    def partition(self, partition):
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
    def disk(self):
        """
            Per system partition disk usage on system
            Converting byte to human readable format
            
            Return dict
        """
        disk_info = {}
        parts = self.disk_partitions

        for i in parts:
            part = i.mountpoint
            part_usage = self.partition(part)
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

    def network(self, all_interface=False):
        """
            all_interface: if true, shows all interface network statistics
            Return: dict
        """
        if all_interface:
            stats = psutil.net_io_counters(pernic=True)
        else:
            stats = psutil.net_io_counters()

        if all_interface:
            n = {}
            for k, v in stats.items():
                n[k] = {
                            "bytes_send": self.hr(v.bytes_sent),
                            "bytes_recv": self.hr(v.bytes_recv),
                            "packets_sent": self.hr(v.packets_sent),
                            "packets_recv": self.hr(v.packets_recv),
                            "errin": v.errin,
                            "errorout": v.errout,
                            "dropin": v.dropin,
                            "dropout": v.dropout
                        }
        else:
            n = {
                    "bytes_sent": self.hr(stats.bytes_sent),
                    "bytes_recv": self.hr(stats.bytes_recv),
                    "packets_sent": self.hr(stats.packets_sent),
                    "packets_recv": self.hr(stats.packets_recv),
                    "errin": stats.errin,
                    "errorout": stats.errout,
                    "dropin": stats.dropin,
                    "dropout": stats.dropout
                }

        return n

