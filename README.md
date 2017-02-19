# P2P-email

CIS 433 

Haomin He, Yanting Liu, Zhibin Zhang

Winter, 2017

Project: Secured peer to peer email system

Objectives: 

-- Design the entire email system

-- Implement P2P framework library

-- Implement sending secure email method

-- Implement receiving secure email method

-- Build a mini-database 

We are building an email system of confidentiality, integrity, and authentication. We use both symmetric-key and public-key encryption. Our cryptographic library is OpenSSL. The current program we are working on involves three main functions: a mini-database to keep track of certificates of users, a method to send encrypted and signed email, and a method to verify and decrypt received email.
 
The following is the tentative scheme we are using:
 
Cert Database

-- A certificate is always verified using the certificate authority (CA), which is created through OpenSSL.

--  A certificate is always verified using the CA’s public key after being extracted from the database to ensure someone has not tampered with it.
 
Send encrypted email

1. Get the cert of the target from the database.

2. Verify the signature on this cert for the email target.

3. Generate a 32-character pass-phrase.

4. Encrypt the message with AES in cipher block chaining mode with the session key and a random initialization vector.

5. Encrypt the session password with the target’s public key.

6. Sign all described previously, using SHA-1 and our private key.
 
Receive encrypted email

1. Obtain sender’s email address from mail header.

2. Find sender’s cert in the database. Verified that the cert is signed by CA.

3. Verify signature of the email using SHA-1 and public key of sender. If invalid, reject.

4. Decrypt session key with private key.

5. Use session key to decrypt the email.


