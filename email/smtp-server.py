import smtpd
import asyncore

class SMTPServerX(smtpd.SMTPServer):
    
    def process_message(self, from_addr, disp_from, to, msg):
        print 'From Address	:', from_addr
        print 'From:	', disp_from
        print 'To  :', to
        print 'Msg	:', msg
        return

server = SMTPServerX(('localhost', 25), None)

asyncore.loop()
