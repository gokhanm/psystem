import smtplib
import email.utils
from email.mime.text import MIMEText
from errors import EmailUnableRelay


__author__ = 'Gokhan MANKARA'
__email__ = 'gokhan@mankara.org'


class Email:
    def __init__(self, server, port=25, username=None, password=None, relay=True, debug_level=False,
                 tls=False):
        """
            server: Mail Server Hostname or Ip Address
            port:   Mail Server SMTP Connection Port
            username: From mail address username
            password: From mail address password
            relay: If authentication not required. Relay can be False. Otherwiser it can be True
            debug_level = smtplib debug devel settings. If it is not False, it can be integer.
            tls: Put the SMTP connection in TLS (Transport Layer Security) mode.

        """
        self.server = server
        self.port = port
        self.relay = relay
        self.tls = tls

        if self.relay:
            self.username = username
            self.password = password

        self.debug_level = debug_level

    def send(self, destination, mail_from, subject, msg):
        """
            destination: To mail address, str
            mail_from: Mail sending from, str
            subject: Mail Subject, str
            msg: Mail Message, str
        """
        msg = MIMEText(msg)
        msg['To'] = email.utils.formataddr(('Recipient', ', '.join(destination.split())))
        msg['From'] = email.utils.formataddr(('Auto Mail Sender', mail_from))
        msg['Subject'] = subject

        server = smtplib.SMTP(self.server, self.port)
        server.set_debuglevel(self.debug_level)

        if self.tls:
            server.starttls()
        if self.relay:
            try:
                server.login(self.username, self.password)
            except smtplib.SMTPException:
                pass

        try:
            server.sendmail(mail_from, destination, msg.as_string())
        finally:
            server.quit()

