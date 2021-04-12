# Skeleton Python Code for the Mail Client
from socket import *
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'localhost'
mailPort = 25

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, mailPort))
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')


# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print (recv) 
if recv1[:3] != '250':
    print('250 reply not received from server.')


# Send MAIL FROM command and print server response.
mailFromCommand = '<alice@crepes.fr>\r\n'
clientSocket.send(mailFromCommand)
recv1 = clientSocket.recv(1024)
print (recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send RCPT TO command and print server response. 
rcptToCommand = '<roneil.sembrano@sjsu.edu>\r\n' 
clientSocket.send(rcptToCommand)
print (recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send DATA command and print server response. 
dataCommand = 'Data'
print (dataCommand)
clientSocket.send(dataCommand)
recv1 = clientSocket.recv(1024)
print (recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send message data.
message = raw_input('Type message here:')


# Message ends with a single period.
mailMessageEnd = '\r\n. \r\n'
clientSocket.send(message+mailMessageEnd) 
print (recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send QUIT command and get server response.
quitCommand = 'Quit\r\n'
print (quitCommand)
clientSocket.send(quitCommand)
print (recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')
