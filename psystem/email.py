import smtplib
import email.utils
from email.mime.text import MIMEText


__author__ = 'Gokhan MANKARA'
__email__ = 'gokhan@mankara.org'


class Email:
    def __init__(self, server, username, password, port=25):
        self.server = server
        self.port = port

    def send(self, destination, mail_from, subject, msg):

        msg = MIMEText(msg)
        msg['To'] = email.utils.formataddr(('Recipient', destination))
        msg['From'] = email.utils.formataddr((subject, mail_from))
        msg['Subject'] = subject

        server = smtplib.SMTP(self.server, self.port)
        server.set_debuglevel(False)

        try:
            server.sendmail(mail_from, destination, msg.as_string())
        finally:
            server.quit()

