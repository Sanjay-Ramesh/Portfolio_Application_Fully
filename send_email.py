import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "sanjayramesh1425@gmail.com"
password = "ujzg rwaq mqle mcmy"

receiver = "sanjayramesh1425@gmail.com"

context = ssl.create_default_context()

message = """\
Subject: HI!
How r u?
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)