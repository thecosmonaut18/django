import smtplib

s=smtplib.SMTP('smtp.gmail.com',587)

s.starttls()

s.login("cosmonaut1824@gmail.com","Cosmo1824")

message="Hello welcome"

s.sendmail("cosmonaut1824@gmail.com","jilsonantony2@gmail.com",message)

s.quit()