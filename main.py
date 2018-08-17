import smtplib
import numpy as np
import mail_list
import credentials
a = mail_list.mail_list
sent = []
recipents = 0
for i in a:                                     #for filtering out repeated email addresses
    if i not in sent:
        sent.append(i)
print("Contacts Loaded")
s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()
s.starttls()
s.login(credentials.user_name,credentials.password)
print("Start Sending")
for i in sent:
    to = "To: "+i
    msg = "\r\n".join([
      "From: Your email address here",
      to,
      "Subject: Subject Here ",
      "",
      "Message Body Here"
      ])
    s.sendmail("Your Email Address Here",i,msg)
    recipents+=1
    print("Successfully Sent to ", recipents, " Recipents")
print("\n\n\t\t----------------- Successfully Sent ---------------------")
s.quit()
