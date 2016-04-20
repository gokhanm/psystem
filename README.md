# PSYSTEM

Psystem is for linux platform developers or sysadmins.

# SETUP

```
        pip3 install -r requirements.txt

        python3 setup.py install
```

# Python Version

```
>= 3.4

not testing 2.7 and above
```

# USAGE

## System Get Usage

```python
        >>> from psystem import system

        >>> get = system.Get()
        >>> get.hostname
        >>> 'localhost.localdomain'

        >>> get.cpu_percent_usage()
        22.5

        >>> get.cpu_percent_usage(percpu=True)
        [24.3, 20.6, 23.8, 21.3]

        >>> get.kernel_version
        '3.16.0-4-amd64'


        >>> get.memory_usage
        {'virtual': {'percent': 39.3, 'total': '7.75 GB', 'used': '5.91 GB', 'free': '1.84 GB'}, 'swap': {'percent': 0.0, 'total': '4.57 GB', 'used': '0', 'free': '4.57 GB'}}


        >>> get.disk_usage
        {'/': {'percent': 31.0, 'total': '105.41 GB', 'used': '32.67 GB', 'free': '67.36 GB'}}

```

## System Set Usage

```python
        >>> from psystem import system
        >>> get = system.Get()
        >>> set = system.Set()

        >>> get.hostname
        'gokhan'
        >>> set.hostname('gokhan.localhost')
        >>> get.hostname
        'gokhan.localhost'


```

## Network Get Usage

```python
        >>> from psystem import network

        >>> get = network.Get()

        >>> get.interfaces
        ['lo', 'eth0', 'docker0']

        >>> get.ip('eth0')
        [{'addr': '10.41.0.164', 'netmask': '255.255.255.0', 'broadcast': '10.41.0.255'}]

        >>> get.mac('eth0')
        [{'addr': 'e4:11:5b:30:2e:c7', 'broadcast': 'ff:ff:ff:ff:ff:ff'}]

        >>> get.default_gateway
        ('10.41.0.1', 'eth0')

        >>> get.all_gateways
        {'default': {2: ('10.41.0.1', 'eth0')}, 2: [('10.41.0.1', 'eth0', True)]}

        >>> get.is_up('eth0')
        True

        >>> get.netmask('eth0')
        '255.255.255.0'
```

## Network Set Usage

```python
        >>> from psystem import network
        >>> set = network.Set()

        >>> set.ip('eth0', '10.10.10.10')

        >>> set.netmask('eth0', '255.255.255.0'
```

## TODO

System

Network

- Send Email

## Requirements

Please see the [requirements text file](requirements.txt)
