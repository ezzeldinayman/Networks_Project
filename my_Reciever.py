# my_Receiver.py
import time, socket, sys
import random



#Welcome Message
print("\nWelcome to The Room\n")
print("Initialising....\n")
time.sleep(1)

#Connecting to The Host
s = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)

#Entering Sender Address/Room Address
print(shost, "(", ip, ")\n")
host = input(str("Enter server address: "))
name = input(str("\nEnter your name: "))
port = 1234

#Sending connection request to sender
print("\nTrying to connect to ", host, "(", port, ")\n")
time.sleep(1)
s.connect((host, port)) #Request connection for host-address (IP) at port No. 1234
print("Connected...\n")

#Send Reciever Name to The Sender and Recieve sender Name
s.send(name.encode())
s_name = s.recv(1024)
s_name = s_name.decode()
print(s_name, "has joined the chat room\nEnter [e] to exit chat room\n")

while True:

    #Recieve Message Size from Sender
    m = s.recv(1024)
    m = m.decode()

    #Recieve Message Size from Sender
    k = s.recv(1024)
    k = k.decode()

    k = int(k)
    i = 0
    a = ""
    b = ""


    message = ""

    while i != k:
        # Randomly Send Negative ACK to the Sender, When f = 0
        f = random.randint(0, 3)
        if (f == 0):
            b = "ACK Lost"
            message = s.recv(1024)
            message = message.decode()
            s.send(b.encode())

        else:
            b = "ACK " + str(i)
            message = s.recv(1024)
            message = message.decode()

            s.send(b.encode())
            a = a + message
            i = i + 1

    print("The message received is :", m)

