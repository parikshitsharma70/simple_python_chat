import socket, threading
from handlers import connection, message

def acceptingConnections():
	while True:
		client, client_address = server.accept()				                              #Server.accept returns two args : client and it's address
		print("New incoming connection: %s:%s" % client_address)                              #Prints the IP and port of the incoming connection
		client.send(bytes("Welcome to the chat, please enter a username:", "utf8"))                  #Send the welcome message to the connected client

		addresses[client] = client_address
		                                                    								  #Push the client adress to the addresses 
		handleConnection = threading.Thread(target = handlingConnections, args = (client,))   #Start a new thread to handle the connection after accepting
		handleConnection.start()

def handlingConnections(client):
	connection.handle(client, broadcast, users, connected_clients)


def broadcast(msg, sender = "", client = ""):
	message.handle(msg, sender, client, connected_clients)

#Client information

users = []
connected_clients = {}
addresses = {}

#Server information

host = "127.0.0.1"
port = 9000
address = (host, port)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)

if __name__ == "__main__":
	server.listen(5)                                                               #Accepts upto 5 incoming connections
	print("Server has been started, waiting for incoming connections")
	acceptingConnectionsThread = threading.Thread(target = acceptingConnections)
	acceptingConnectionsThread.start()
	acceptingConnectionsThread.join()


	server.close() 

