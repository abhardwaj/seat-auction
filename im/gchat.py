#!/usr/bin/python

import xmpp
import getpass

'''
command-line gchat

name: anant bhardwaj

'''

def handlePresenceEvents(con, event): 
  if event:
    try:
      print "\n"
      print "From: ",event.getFrom()
      #print "Resource: ", event.getFrom().getResource() 
      print "Type: ", event.getType()
      print "Staus: ", event.getStatus()
      print "Show: ", event.getShow()
      if(event.getFrom()=="rish.anubhai@gmail.com"):
        event.setShow("unavailable")
    except:
      pass
       
username = "helloanant007@gmail.com"
password = getpass.getpass("password: ")
server = "gmail.com"
port = 5222
 
jid=xmpp.protocol.JID(username);
xmpp_client=xmpp.Client(jid.getDomain(),debug=[])
 
if not xmpp_client.connect((server,port)):
  print "Could not connect to server..."
  exit(1)
if not xmpp_client.auth(jid.getNode(),password, jid.getResource()):
  print "Authentication failed..."
  exit(1)

xmpp_client.sendInitPresence(requestRoster=1)
'''
roster = xmpp_client.getRoster()
#roster.Request(1)
for _jid in roster.keys():
  try:
    #roster.Subscribe(_jid)
    print _jid
    if(roster.getName(_jid) == None):
      roster.setName(_jid)
    print jid
    print jid.getResource()
    print roster.getRawItem(_jid)
  except:
    print "blocked"
    print _jid
    pass
'''

xmpp_client.RegisterHandler('presence', handlePresenceEvents)

while xmpp_client.Process(1):
  pass

