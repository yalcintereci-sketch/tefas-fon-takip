import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class MailSender:

    def __init__(self, smtp_server, port, username, password):
        self.smtp_server = smtp_server
        self.port = port
        self.username = username
        self.password = password

    def send(self, receiver, subject, message):

        mail = MIMEMultipart()

        mail["From"] = self.username
        mail["To"] = receiver
        mail["Subject"] = subject

        mail.attach(MIMEText(message, "plain", "utf-8"))

        with smtplib.SMTP_SSL(self.smtp_server, self.port) as server:
            server.login(self.username, self.password)
            server.send_message(mail)

        print("E-posta başarıyla gönderildi.")
