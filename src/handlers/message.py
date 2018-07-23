def handle(msg, sender, client, connected_clients):
	otherClients = {}                               #Define an empty dictionary to add the clients to broadcast the message to
	author = sender[5:-6]  						#Slice the sender array to get the author user

	for key, value in connected_clients.items():
		if value != author:
			otherClients[key] = value             	#Push the key, value pair into the dict defined earlier

	for sock in otherClients:
		sock.send(bytes(sender, "utf8") + msg)		#Broadcast the message to everyone except the author