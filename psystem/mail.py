import smtplib
import email.utils
from email.mime.text import MIMEText
from errors import EmailUnableRelay


__author__ = 'Gokhan MANKARA'
__email__ = 'gokhan@mankara.org'


class Email:

    def __init__(self, server, username, password, port=25, relay=False, debug_level=False):
        self.server = server
        self.port = port
        self.relay = relay

        if self.relay:
            self.username = username
            self.password = password

        self.debug_level = debug_level

    def send(self, destination, mail_from, subject, msg):

        msg = MIMEText(msg)
        msg['To'] = email.utils.formataddr(('Recipient', destination))
        msg['From'] = email.utils.formataddr((subject, mail_from))
        msg['Subject'] = subject

        server = smtplib.SMTP(self.server, self.port)
        server.set_debuglevel(self.debug_level)

        if self.relay:
            try:
                server.login(self.username, self.password)
            except smtplib.SMTPException:
                pass

        try:
            server.sendmail(mail_from, destination, msg.as_string())
        finally:
            server.quit()

