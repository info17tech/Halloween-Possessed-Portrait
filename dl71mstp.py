import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
#Next, log in to the server
server.login("bhavna.j18032001@gmail.com", "tishajosh2")

#Send the mail
msg = "HI THIS IS A TEST MAIL"                                   
server.sendmail("bhavna.j18032001@gmail.com", "vidhya1942000@gmail.com",msg)
server.quit