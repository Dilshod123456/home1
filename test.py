# import smtplib
# s = smtplib.SMTP('smtp.gmail.com', 587)
# s.starttls()
# s.login('tuygunovdilshod21@gmail.com', "petr mdak xpvi keml")
# message = 'Pythonda szga sms kevoti'
# s.sendmail("tuygunovdilshod21@gmail.com", "tuygunoff4545@gmail.com", message)
# s.quit()


import smtplib
 
# list of email_id to send the mail
li = ["tuygunoff@gmail.com", "tuygunovdilshod21@gmail.com"]
 
for dest in li:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("tuygunovdilshod21@gmail.com", "petr mdak xpvi keml")
    message = "Message_you_need_to_send"
    s.sendmail("tuygunovdilshod21@gmail.com", dest, message)
    s.quit()