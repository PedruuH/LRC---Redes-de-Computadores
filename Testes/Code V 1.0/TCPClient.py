import socket
serverName = '192.168.0.105'
serverPort = 12010
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect((serverName,serverPort))
print 'Connected on server',(serverName,serverPort)
msg = raw_input ('mensagem: ')
tcp_socket.sendto(msg,(serverName,serverPort))
modifiedMsg = tcp_socket.recv(1024)
print('From server',modifiedMsg)
tcp_socket.close()

