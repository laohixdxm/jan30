#!/usr/bin/env python
from smtplib import SMTP
from smtplib import SMTPException
from email.mime.text import MIMEText
import sys

#Global variables
EMAIL_SUBJECT = "Email from Python script"
EMAIL_RECEIVERS = ['laohixdxm@126.com']
EMAIL_SENDER = 'laohixdxm@gmail.com'
GMAIL_SMTP = "smtp.gmail.com"
GMAIL_SMTP_PORT = 587
TEXT_SUBTYPE = "plain"

def listToStr(lst):
	"""This method makes comma seperated list item string"""
	return ','.join(lst)

def send_email(content, pswd):
	"""This method sends an email"""

	#Create the message
	msg = MIMEText(content, TEXT_SUBTYPE)
	msg["Subject"] = EMAIL_SUBJECT
	msg["From"] = EMAIL_SENDER
	msg["To"] = listToStr(EMAIL_RECEIVERS)

	try:
	  smtpObj = SMTP(GMAIL_SMTP, GMAIL_SMTP_PORT)
	  #Identify yourself to GMAIL EMSMTP server.
  	  smtpObj.ehlo()
	  #Put SMTP connection in TLS mode all ehlo again
	  smtpObj.starttls()
	  smtpObj.ehlo()
  	  #Login to service
	  smtpObj.login(user=EMAIL_SENDER, password=pswd)
	  #send email
 	  smtpObj.sendmail(EMAIL_SENDER, EMAIL_RECEIVERS, msg.as_string())
	  #close connection and session
	  smtpObj.quit()
	except SMTPException as error:
	  print "Errro: unable to send email : {err}".format(err=error)
	
def main(pswd):
	send_email("hello", pswd)

if __name__ == "__main__":
	main(sys.argv[1])
	
	  



