import smtpd
import asyncore

server = smtpd.PureProxy(('bento.stanford.edu', 1026), ('bento.stanford.edu', 465))

asyncore.loop()
