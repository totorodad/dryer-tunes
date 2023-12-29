#dryer_sms.py
#Free and open source
#J. Nolan (totorodad@gmail.com)

import smtplib
import subprocess
from datetime import datetime

#note don't name this file email.py or it won't cooperate with smtplib 

#1. setup new gmail (link to your account if you want)
#2. make it less secure:
# 	https://myaccount.google.com/lesssecureapps
#3. Set the below variables to match your e-mail account

SMTP_SERVER = 'smtp.gmail.com' #Email Server (don't change!)
SMTP_PORT = 587 #Server Port (don't change!)
GMAIL_USERNAME = '<your dryers email address once you set it up>@gmail.com' #change this to match your gmail account
GMAIL_PASSWORD = '<your dryers password>'  #change this to match your gmail password
 
class Emailer:
	def sendmail(self, recipient, subject, content):
		#Create Headers
		headers = ["From: " + GMAIL_USERNAME, "Subject: " + subject, "To: "+ ", ".join(recipient),
		"MIME-Version: 1.0", "Content-Type: text/html"]
		headers = "\r\n".join(headers)

		#Connect to Gmail Server
		session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
		session.ehlo()
		session.starttls()
		session.ehlo()
        
		#Login to Gmail
		session.login(GMAIL_USERNAME, GMAIL_PASSWORD)
		
		#Send Email & Exit
		session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
		session.quit

def dryer_done_msg():
	sender = Emailer()

	# change the below sendTo, emailContent to what you want
	sendTo = ['<phone number 1 to receive text>@vtext.com', '<phone number 2 to receive text>@vtext.com']
	emailSubject = "Dryer is Done"

	now = datetime.now()
	emailContent = '\nDrying completed: [' + now.strftime("%m/%d/%Y, %H:%M:%S") + ']\n'
	print('Sending SMS' + '\nTo: ' + ', '.join(sendTo) + '\nContent: ' + emailContent + '\n')
	sender.sendmail(sendTo, emailSubject, emailContent) 

#uncomment the following line to send SMS with this python 
#dryer_done_msg()
