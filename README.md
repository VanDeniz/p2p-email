# Peer to peer email system

CIS 433 

Haomin He, Yanting Liu, Zhibin Zhang

Winter, 2017

Project: Secure peer to peer email system

Objectives: 

-- Design the entire email system

-- Implement P2P framework library

-- Implement sending secure email method

-- Implement receiving secure email method

-- Build a mini-database 

We are building an email system of confidentiality, integrity, and authentication. The current program we are working on involves three main functions: a distributed hash table to keep track of messages of users, a method to send encrypted and signed email, and a method to verify and decrypt received email.
 

Implementation Usage: 
	>python useragent.py 5000 127.0.0.1 4000
	>Enter send or receive
	receive
	>Enter your email:
	123@123.com
	
Interface Usage:  
	>python p2pemailUI_readmail.py 
	>python p2pemailUI_sendmail.py 

![alt tag](https://github.com/VanDeniz/p2p-email/blob/master/uesImages/1.GIF)
![alt tag](https://github.com/VanDeniz/p2p-email/blob/master/uesImages/2.GIF)
![alt tag](https://github.com/VanDeniz/p2p-email/blob/master/uesImages/3.GIF)

