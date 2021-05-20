import smtplib
from email.message import EmailMessage
from email.utils import formatdate
from mail.cr import passs, usern

def sendingmail():
    if True:
        
        msg = EmailMessage()
        msg.set_content(input("Your Message :- "))
        msg['Subject'] = input("Subject :-")
        msg['From'] = usern
        msg['To'] = input("To :-")
        msg['Date'] = formatdate(localtime=True)

        # Send the message via our own SMTP server.
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(usern, passs)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully")
    else:
        print("not able to send Email")



