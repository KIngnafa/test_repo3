#!/usr/bin/python
import smtplib


FROM='oracle@MKIT-DEV-OEM.localdomain'
#variables
TO_EMAIL='stackcloud11@mkitconsulting.net'
SUBJECT='Test Email Yinka'
BODY="This is a test email"
MSG=("\n".join(("From: %s" %FROM, "To: %s" %TO_EMAIL, "Subject: %s:\n" %SUBJECT,"%s" %BODY)))

with smtplib.SMTP('localhost') as my_server:
	my_server.sendmail(FROM,TO_EMAIL,MSG)
	print("Email sent successfully to %s" %TO_EMAIL)
