import twisted.internet.reactor
import hashlib
from twisted.internet import defer

import kademlia.node
#from kademlia.node import 

from entangled.node import EntangledNode
"""
class Emailheader:
    """Email header
    """
    def __init__(self,session_key,msgid,digest):
        self.session_key = session_key
        self.msgid = msgid
        self.digest = digest
    add encode function?
"""


"""
class PeerNode(EntangledNode):
    Peer node
    
    def __init__(self,udpPort=4000, dataStore=None, routingTable=None, networkProtocol=None):
        EntangledNode.__init__(self, udpPort, dataStore, routingTable, networkProtocol)
        self.invalidKeyworkds = []
        self.keywordSplitters = ['_','.','/','@']
"""
def store(node,identifier,object,originalPublisherID=None,age=0):
    """
    identifier: 1.message: RFC 2822 message ID
    object: 1.message body
    """
    #Store the value in the DHT.(deferred Result?)
    deferredResult = node.iterativeStore(identifier,object,originalPublisherID,age)
    deferredResult.addCallback(storeCallback)
    deferredResult.addErrback(genericErrorCallback)

def storeCallback(*args, **kwargs):
    """Callback function that is invoked when the store operation succeeds
    """
    print'Value has been stored in the DHT'
    #twisted.internet.reactor.callLater(2.5, fetch,self,)


def genericErrorCallback(failure):
    print'An error has occurredx:', failure.getErrorMessage()
    #twisted.internet.reactor.callLater(0,stop)


def fetch(node,identifier):
    """
    retrieve stored objects(encrypted message body)
    """
    deferredResult = node.iterativeFindValue(identifier)
    deferredResult.addCallback(fetchCallback,identifier)
    deferredResult.addErrback(genericErrorCallback)

def fetchCallback(result,identifier):
    if type(result) == dict:
        print 'Value successfully retrieved'
        #print the email on the screem
        print(result[identifier])
        #return ???
    else:
        print'Value not found'

def delete(node,identifier, eaddress):
    """
     delete unneeded objects from its storage.
    identifier:object identifier
    eaddress: email address
    """
    #certificate?
    deferredResult = node.iterativeDelete(identifier)
    deferredResutl.addCallback(deleteCallback)
    deferredResult.addErrback(genericErrorCallback)

def deleteValueCallback(result):
    print'Key/value pair deleted'

def append_Inbox(node,eaddress,header):
    """
    append email message headers to a recipient inbox
    eaddress:email address
    ehead: email head
    """
    deferredResult = node.iterativeStore(eaddress,header)
    deferredResult.addCallback(appendCallback)
    deferredResult.addErrback(genericErrorCallback)

def appendCallback(*args,**kwargs):
    print'notification has been stored in inbox'

#def genericErrorCallback(failure):
    #print'An error has occurred',failure.getErrorMessage()

def read_Inbox(node,eaddress):
    deferredResult = node.iterativeFindValue(eaddress)
    deferredResult.addCallback(readInboxCallback,eaddress,node)
    deferredResult.addErrback(genericErrorCallback)

def readInboxCallback(result,eaddress,node):
    """ Callback function that is invoked when the read_Inbox() operation succeeds """
    # Check if the key was found (result is a dict of format {key: value}) or not (in which case a list of "closest" Kademlia contacts would be returned instead")
    if type(result) == dict:
        #can
        fetch(node,result[eaddress])
        #print 'Value successfully retrieved'
    else:
        print 'Value not found'


if __name__ == '__main__':
    import twisted.internet.reactor
    from kademlia.datastore import SQLiteDataStore
    import sys, os
    if len(sys.argv) < 2:
        print 'Usage:\n%s UDP_PORT  [KNOWN_NODE_IP  KNOWN_NODE_PORT]' % sys.argv[0]
        print 'or:\n%s UDP_PORT  [FILE_WITH_KNOWN_NODES]' % sys.argv[0]
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
        if os.path.isfile('/tmp/dbFile%s.db' % sys.argv[1]):
            os.remove('/tmp/dbFile%s.db' % sys.argv[1])
        dataStore = SQLiteDataStore(dbFile = '/tmp/dbFile%s.db' % sys.argv[1])
        node = EntangledNode( udpPort=int(sys.argv[1]), dataStore=dataStore )
        #node = EntangledNode( udpPort=int(sys.argv[1]) )
        node.joinNetwork(knownNodes)
        twisted.internet.reactor.run()



