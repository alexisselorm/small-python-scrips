# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 21:55:16 2021

@author: Alexis
"""

# Sending an email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
from pathlib import Path
from string import Template

template = Template(Path("template.html").read_text())
body = template.substitute({"name": "John"})

message = MIMEMultipart()
message["from"] = "Alexis"
message["to"] = "alexisgb1738@gmail.com"
message["subject"] = "Hope this Python script works"
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path("betway.png").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("agbeckor2@gmail.com", "1killerbeanforever")
    smtp.send_message(message)
    print("Sent...")
