from peernode import store
from peernode import append_Inbox
from peernode import fetch
from peernode import read_Inbox
from peernode import Emailheader
from email.utils import make_msgid
import hashlib
import os, sys, time, signal
import twisted.internet.reactor
import random,string
from entangled.node import EntangledNode
from entangled.kademlia.datastore import SQLiteDataStore



def generate_session_key():
    return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(32))

def main():
    import sys, os
    if len(sys.argv) < 2:
        print 'Usage:\n%s UDP_PORT [KNOWN_NODE_IP  KNOWN_NODE_PORT]' % sys.argv[0]
        print 'or:\n%s UDP_PORT [FILE_WITH_KNOWN_NODES]' % sys.argv[0]
        print '\nIf a file is specified, it should containg one IP address and UDP port\nper line, seperated by a space.'
        sys.exit(1)
    try:
        int(sys.argv[1])
    except ValueError:
        print '\nUDP_PORT must be an integer value.\n'
        print 'Usage:\n%s UDP_PORT  [KNOWN_NODE_IP  KNOWN_NODE_PORT]' % sys.argv[0]
        print 'or:\n%s UDP_PORT  [FILE_WITH_KNOWN_NODES]' % sys.argv[0]
        print '\nIf a file is specified, it should contain one IP address and UDP port\nper line, seperated by a space.'
        sys.exit(1)

    if len(sys.argv) == 4:
        knownNodes = [(sys.argv[2], int(sys.argv[3]))]
    elif len(sys.argv) == 3:
        knownNodes = []
        f = open(sys.argv[2], 'r')
        lines = f.readlines()
        f.close()
        for line in lines:
            ipAddress, udpPort = line.split()
            knownNodes.append((ipAddress, int(udpPort)))
    else:
        knownNodes = None
        print '\nNOTE: You have not specified any remote DHT node(s) to connect to'
        print 'It will thus not be aware of any existing DHT, but will still function as a self-contained DHT (until another node contacts it).'
        print 'Run this script without any arguments for info.\n'
    # Set up SQLite-based data store (you could use an in-memory store instead, for example)
    if os.path.isfile('/tmp/dbFile%s.db' % sys.argv[1]):
        os.remove('/tmp/dbFile%s.db' % sys.argv[1])
    dataStore = SQLiteDataStore(dbFile = '/tmp/dbFile%s.db' % sys.argv[1])
    
    node = EntangledNode( udpPort=int(sys.argv[1]), dataStore=dataStore )
    node.joinNetwork(knownNodes)

    print("Enter the receiver's email:")
    rcv_id = str(raw_input())
    print("Enter your message:")
    msg = str(raw_input())
    session_key = generate_session_key()
    msgid = make_msgid()

    #stroe the messageid and message in the DHT ?????????
    #node.store(str(msgid),msg)
    store(node,msgid[0:12],msg)
    
    #generate email header
    hash_sha1 = hashlib.sha1(msg)
    header = Emailheader(session_key,msgid,hash_sha1.digest())
    
    #stroe the email address and email head in the DHT
    append_Inbox(node,rcv_id, msgid[0:12])

    '''print("Enter your email:")
    rcv_id = str(raw_input())
    read_Inbox(node,rcv_id)
    '''

if __name__ == "__main__":
    main()
