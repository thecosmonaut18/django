# Python code to illustrate Sending mail with attachments
# from your Gmail account  
 
# # libraries to be imported
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email import encoders    
# fromaddr = "fromadd"
# toaddr = "toadd"  
# # instance of MIMEMultipart
# msg = MIMEMultipart()  
# # storing the senders email address  
# msg['From'] = 'frmadd'  
# # storing the receivers email address  
# msg['To'] = 'toadd'  
# # storing the subject  
# msg['Subject'] = "Subject of the Mail"  
# # string to store the body of the mail
# body = "Body_of_the_mail"  
# # attach the body with the msg instance
# msg.attach(MIMEText(body, 'plain'))  
# # open the file to be sent  
# filename = "v.txt"
# attachment = open(filename, "rb")  
# # instance of MIMEBase and named as p
# p = MIMEBase('application', 'octet-stream')  
# # To change the pay___load into encoded form
# p.set_payload((attachment).read())  
# # encode into base64
# encoders.encode_base64(p)    
# p.add_header('Content-Disposition', "attachment; filename= %s" % filename)  
# # attach the instance 'p' to instance 'msg'
# msg.attach(p)  
# # creates SMTP session
# s = smtplib.SMTP('smtp.gmail.com', 587)  
# # start TLS for security
# s.starttls()
 
# # Authentication
# s.login(fromaddr, "password")
 
# # Converts the Multipart msg into a string
# text = msg.as_string()
 
# # sending the mail
# s.sendmail(fromaddr, toaddr, text)
 
# # terminating the session
# s.quit()




# a=[11,55,23,[44,12,89,[2,6],41]]

# a[3][1]=66

# print(a[3][1])

# print(a)



