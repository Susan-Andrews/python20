# go to your gmail account and enable two step authentication.  
# generate app password-  
# create a function to send email.  

 
from email.message import EmailMessage
from app2 import password  # creating another py file and storing password for security reasons
import ssl
import smtplib


email_sender= " Sender Email"
email_password =password  # accesing password

email_reciever= "receiver Email"

subject = "its a mail from python"
body=" its a mail created using python"

em=EmailMessage()
em['From']= email_sender
em['To']=email_reciever
em['subject']=subject
em.set_content(body)

context=ssl.create_default_context()

with smtplib.SMTP_SSL(' Reciever Email',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_reciever,em.as_string())

 
