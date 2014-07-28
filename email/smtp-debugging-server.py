import smtpd
import asyncore

server = smtpd.DebuggingServer(('bento.stanford.edu', 25), None)

asyncore.loop()
