# Copyright 2016 Gokhan MANKARA <gokhan@mankara.org>

import spur


class Local():
    """
        Localhost shell class
    """
    def run(self, cmd):
        """
            :param cmd: Shell Command. list
            Usage:
                from psystem import shell
                local_shell = shell.Local()
                local_shell.run(['echo', '-n', 'hello'])
        """
        shell = spur.LocalShell()
        result = shell.run(cmd)

        return result.output


class Ssh():
    """
        :param hostname: Server ssh hostname
        :param username: Server ssh username
        :param password: Server username password
        :param port: Server ssh port. If port is None Default: 22
        :param private_key_file: 'path/to/private.key'
        :param connect_timeout: a timeout in seconds for establishing an SSH connection.
                                Defaults to 60 (one minute).
        :param missing_host_key: by default, an error is raised when a host key is missing.
                                One of the following values can be used to change the behaviour
                                when a host key is missing:

                                * raise_error -- raise an error
                                * warn -- accept the host key and log a warning
                                * accept -- accept the host key
                                * auto_add -- auto add the host key if not exists
        :param shell_type: the type of shell used by the host. The following shell 
                            types are currently supported:

                            * sh -- the Bourne shell. Supports all features.
                            * minimal -- a minimal shell. Several features are unsupported:
                                                    Non-existent commands will not raise spur.NoSuchCommandError.
                                                    The following arguments to spawn and run are unsupported unless
                                                    set to their default values: cwd, update_env, and store_pid.
        :param look_for_private_keys: by default, Spur will search for discoverable private key 
                                        files in ~/.ssh/. Set to False to disable this behaviour.                                                       
        :param load_system_host_keys: by default, Spur will attempt to read host keys from the 
                                        user's known hosts file, as used by OpenSSH, and no exception 
                                        will be raised if the file can't be
                                        read. Set to False to disable this
                                        behaviour.
        :param sock: an open socket or socket-like object to use for
                        communication to the target host.

        Usage:
                from psystem import shell
                ssh_shell = shell.Ssh(hostname='localhost', username='sam', password='password1')
                with ssh_shell:
                    result = ssh_shell.run(["echo", "-n", "hello"])
                    print(result)
    """
    def __init__(self, 
                 hostname,
                 username=None,
                 password=None,
                 port=None,
                 private_key_file=None,
                 connect_timeout=None,
                 missing_host_key='raise_error',
                 shell_type='sh',
                 look_for_private_keys=True,
                 load_system_host_keys=True,
                 sock=None
                 ):

        self._hostname = hostname
        self._username = username
        self._password = password
        self._port = port
        self._private_key_file = private_key_file
        self._connect_timeout = connect_timeout
        self._load_system_host_keys = load_system_host_keys
        self._sock = sock

        if 'sh' == shell_type:
            self._shell_type = spur.ssh.ShellTypes.sh
        elif 'minimal' == shell_type:
            self._shell_type = spur.ssh.ShellTypes.minimal

        if 'raise_error' == missing_host_key:
            self._missing_host_key = spur.ssh.MissingHostKey.raise_error
        elif 'warn' == missing_host_key:
            self._missing_host_key = spur.ssh.MissingHostKey.warn
        elif 'accept' == missing_host_key:
            self._missing_host_key = spur.ssh.MissingHostKey.accept
        elif 'auto_add' == missing_host_key:
            self._missing_host_key = spur.ssh.MissingHostKey.auto_add

    def run(self, cmd):
        """
            :param cmd: Shell Command. list
        """
        shell = spur.SshShell(hostname=self._hostname,
                              username=self._username,
                              password=self._password,
                              port=self._port,
                              private_key_file=self._private_key_file,
                              connect_timeout=self._connect_timeout,
                              missing_host_key=self._missing_host_key,
                              shell_type=self._shell_type,
                              load_system_host_keys=self._load_system_host_keys,
                              sock=self._sock
                              )

        with shell:
            result = shell.run(cmd)

        return result.output

