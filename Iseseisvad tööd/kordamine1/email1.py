import smtplib

sender_email = "vikk.opilane@outlook.com" # saatja email
rec_email = "asmovoitka@gmail.com" # saaja email
password = input(str("Please enter your password : ")) # parooli input
message = "Hey, this was sent using python" # emaili sõnum

server = smtplib.SMTP('smtp-mail.outlook.com', 587) # server
server.starttls()
print("Login Success") # prindib login success
server.sendmail(sender_email, rec_email, message)# võtab saatja ja saaja emaili ning sõnumi
print("Email has been sent to", rec_email) # prindib email on saadetud ja saatja emaili