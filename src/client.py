import socket, threading, os

class Task:
	def receiveData():                                               #Function to listen for incoming data from server
		while True:
			try:
				msg = clientSocket.recv(1024).decode("utf8")
				print(msg)
			except OSError:
				break

	def sendData():                                                  #Function to send messages to server
		msg = input()
		if bool(msg) == True:
			clientSocket.send(bytes(msg, "utf8"))
		else:
			print("Can not send an empty message")

#Initialize the Client

print("Welcome to the chat server.\n Please enter the details of the chat room you want to join \n If left empty, join default server:")

host = input("IP Address: ")
port = input("Port: ")

if not host:
	host = "127.0.0.1"
else:
	pass

if not port:
	port = 9000
else:
	port = int(port)

if bool(host) == True and bool(port) == True:                          #Clear the terminal when the address has been entered
	try:
		os.system("cls")
		os.system("clear")
	except Exception as err:
		pass

	address = (host, port)

	clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	clientSocket.connect(address)

	receiveThread = threading.Thread(target = Task.receiveData)
	receiveThread.daemon = False
	receiveThread.start()

	while True:
		Task.sendData()
