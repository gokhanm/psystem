# PSYSTEM

[![PyPI](https://img.shields.io/pypi/v/psystem.svg)](https://pypi.python.org/pypi/psystem)

Psystem aims to collect system modules ( like psutil, netifaces etc. ) under the one roof 
for linux platform developers or sysadmins. You can change system, network settings, 
get current settings and send e-mail with mail module.

# SETUP

```
        pip3 install -r requirements.txt

        python3 setup.py install
```

or

for Python 2.7.x
```
    pip install psystem
```
for Python 3.5.x
```
    pip3 install psystem
```

# Python Version

```
>= 3.4
>= 2.7

```
2.7.x, Not compatible

# USAGE

## System Get Usage

```python
        >>> from psystem import system

        >>> get = system.Get()
        >>> get.hostname
        >>> 'localhost.localdomain'

        >>> get.kernel_version
        '3.16.0-4-amd64'

        >>> get.ntp_current_time
        'Thu Apr 21 10:34:43 2016'

        >>> get.ntp_host = "us.pool.ntp.org"
        >>> get.ntp_current_time
        'Thu Apr 21 10:35:10 2016'

         >>> get.pid('crypto')
         33

         >>> get.uptime
        '1:03:58'

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

## System Stats

```python

        >>> from psystem import stats
        >>> get = stats.Get()
        
        >>> get.memory
        {'swap': {'percent': 0.0, 'total': '2 GB', 'free': '2 GB', 'used': '0'}, 
         'virtual': {'percent': 15.6, 'total': '993.34 MB', 'free': '631.95 MB', 'used': '361.39 MB'}}

        >>> get.cpu()
        0.1

        >>> get.cpu(percpu=True)
        [0.1]

        >>> get.disk
        {'/boot': {'percent': 26.5, 'total': '496.67 MB', 'free': '365.29 MB', 'used': '131.38 MB'}, 
         '/': {'percent': 7.2, 'total': '17.46 GB', 'free': '16.21 GB', 'used': '1.25 GB'}}

        >>> get.network(all_interface=True)
        {'lo': {'errorout': 0, 'packets_sent': '0', 'dropout': 0, 'dropin': 0, 'errin': 0, 'bytes_send': '0',
                'bytes_recv': '0', 'packets_recv': '0'},
         'eth0': {'errorout': 0, 'packets_sent': '6.2 KB', 'dropout': 0, 'dropin': 0, 'errin': 0, 'bytes_send': '683.88 KB',
                  'bytes_recv': '5.46 MB', 'packets_recv': '30.55 KB'}}
        
        >>> get.network()
        {'errorout': 0, 'packets_sent': '6.22 KB', 'dropin': 0, 'errin': 0, 'dropout': 0, 'bytes_sent': '686.43 KB',
         'bytes_recv': '5.47 MB', 'packets_recv': '30.63 KB'}


```

## Shell Local
```python
    >>> from psystem import shell
    >>> shell_local = shell.Local()
    >>> result = shell_local.run(['echo', '-n', 'hello'])
    >>> print(result)
        'hello'
```

## Shell Ssh
```python
    >>> from psystem import shell
    >>> shell_ssh = shell.Ssh(hostname='localhost', username='sam', password='password1')
    >>> result = shell_ssh.run(['echo', '-n', 'hello'])
    >>> print(result)
        'hello'
```

## Sending Mail
```python
        >>> from psystem import mail
        >>> m = mail.Email('mail.domain.com', username=username, password=password, port=587)
        >>> m.send('destination@domain.com', 'from@domain.com', 'subject', 'message')

        # Multi destinations
        >>> destinations = "dest1@domain.com, dest2@domain.com"
        >>> m.send(destinations, 'from@domain.com', 'subject', 'message')
        
```

## TODO

System

Network

## Requirements

Please see the [requirements text file](requirements.txt)
