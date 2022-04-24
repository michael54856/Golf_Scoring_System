import socket


host, port = "192.168.1.112", 25001
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

while True:
    passStr = input()
    sock.sendall(passStr.encode("UTF-8")) #Converting string to Byte, and sending it to C#
    receivedData = sock.recv(1024).decode("UTF-8") #receiveing data in Byte fron C#, and converting it to String
    print(receivedData)