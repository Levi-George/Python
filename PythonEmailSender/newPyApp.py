#Program: Email Sender
#Date: 09-02-22
#Purpose: Send E-mails using Python
#APP Pass: 

from email.message import EmailMessage
import ssl
import smtplib
import re

#Fill the sender, password, and receiver with appropriate values
email_sender = ""
email_password = ""

email_receiver = ""

subject = "Test Email"
body = """
Hello, this is a test email from Levi, if you weren't supposed to get this then ignore it, duh.
"""

email_regex = "^[A-Za-z0-9]*@[A-Za-z0-9]*\.com"

while(((re.search(email_regex, email_sender))) == None):
    email_sender = input(f"Please enter a valid e-mail ")

email_password = input(f"Enter your e-mail password")

while(((re.search(email_regex, email_sender))) == None):
    email_receiver = input(f"Please enter a valid e-mail for the receiver")

subject = input(f"Enter the subject of your e-mail")

body = input(f"Enter the message you would like to send")

print(f"Thank you, please wait while we send the e-mail")


em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())