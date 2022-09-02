#Program: Email Sender
#Date: 09-02-22
#Purpose: Send E-mails using Python
#APP Pass: 

from email.message import EmailMessage
import ssl
import smtplib


#Fill the sender, password, and receiver with appropriate values
email_sender = ''
email_password = ""

email_receiver = ''

subject = "Test Email"
body = """
Hello, this is a test email from Levi, if you weren't supposed to get this then ignore it, duh.

"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())