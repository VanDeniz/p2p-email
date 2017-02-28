# Haomin He
# PyCrypto is a library, which provides secure hash functions and 
# various encryption algrithms. 
# Available at: https://www.dlitz.net/software/pycrypto/
# Commandline Installation: sudo pip install pycrypto

from Crypto.Cipher import AES


def encryptionM(enString):
    #Encryption
    encryption_suite = AES.new('This is a key123', AES.MODE_ECB)
    #print len(enString)
    message = enString
    extra = len(message) % 16
    if extra > 0:
        message = message + (' ' * (16 - extra))
    print message

    cipher_text = encryption_suite.encrypt(message)
    print cipher_text
    return cipher_text


def decryptionM(deString):
    #Decryption
    #print deString
    decryption_suite = AES.new('This is a key123', AES.MODE_ECB)
    plain_text = decryption_suite.decrypt(deString)
    print plain_text
    return plain_text



if __name__ == "__main__":
    #print "this is crypo"
    message = "A really secret message. Not for prying eyes."
    enMessage = encryptionM(message)
    #print enMessage
    decryptionM(enMessage)
