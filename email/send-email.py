#!/usr/b!in/python

import getpass
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import optparse
import sys, os, cgi
import datetime, time




msg_body = """
Yo, what's up?
"""



def main():    
	#### Email ####	
	email_subject = "Yo"
	from_addr="congratbot@google.com"
	to_addr = ["anantb@google.com"]
	
	msg = MIMEMultipart()
	msg['From'] = "CongratBot <congratbot@google.com>"
	msg['To'] = ",".join(to_addr)
	msg['Reply-to'] = from_addr
	msg['Subject'] = email_subject
	msg.attach(MIMEText(msg_body))	
	
	
	#username = raw_input("username: ")
	#password = getpass.getpass("password: ")
	smtp_conn = smtplib.SMTP('smtp.corp.google.com')
	smtp_conn.login("anantb", "*******")	
	smtp_conn.set_debuglevel(True)	
	smtp_conn.sendmail(from_addr, to_addr, msg.as_string())
	smtp_conn.close() 

if __name__ == "__main__":
    main()
