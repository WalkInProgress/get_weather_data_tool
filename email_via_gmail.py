import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from GMAIL_PWD import GMAIL_PWD

def send_gmail(msg_file):
    with open(msg_file, mode='rb') as message:           #Open report html file for readinig
        msg = MIMEText(message.read(), 'html', 'html')   #Create html message

    msg



