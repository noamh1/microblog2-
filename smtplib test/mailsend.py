import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("noamhermanse3@gmail.com", "qwerty123456a")
 
msg = "YOUR MESSAGE!"
server.sendmail("noamhermanse3@gmail.com", "noamhermanse3@gmail.com", msg)
server.quit()