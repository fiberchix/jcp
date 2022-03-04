from http import server
import smtplib
from email.message import EmailMessage


# email parameters
msg=EmailMessage()
msg['Subject']='My First Python Project-SMTP EMAIL -- TEST1'
msg['From']='emtestp@gmail.com'
msg['To']='emdionisio777@gmail.com, emtestp@gmail.com'
msg.set_content("Test SMTP LIB using Python from Emilie.\n This is my first Python Project.\
It\'s a simple SMTP protocol that checks if email is working. I\'m doing this project for my class at Generation and I\'m enjoying it. \
Sally, Anu, and David are awesome and so as my classmates.")

# setup email server protocol
server=smtplib.SMTP_SSL('smtp.gmail.com',465)

# setup up login
server.login("","")
server.send_message(msg)
server.quit()


