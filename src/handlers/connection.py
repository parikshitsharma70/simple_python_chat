def handle(client, broadcast, users, connected_clients):     #Params to be called
	username = client.recv(1024).decode("utf8")              #Recieve the username first as client connects
	
	while username in users:
		client.send(bytes("Sorry, but the username you have chosen has been taken. Please enter another: ", "utf8"))  #Checking for unique username
		username = client.recv(1024).decode("utf8")																	  #Re-enter username if not unique			
		print(username)			

	users.append(username)									   #Add username to list of users 	
	connected_clients[client] = username			           #Add username to list of connected clients with the key "client" 
	print(username)

	client.send(bytes("| Successfully joined to the server |\n-users connected: %s\n" % len(users), "utf8"))  
	broadcast(bytes("- %s has joined" % username, "utf8"))

	while True:
		msg = client.recv(1024)                               #Processing the message entered by user

		if msg.lower() == bytes("/help", "utf8"):
			Commands = ["/help", "/users", "/leave"]
			client.send(bytes("Available Commands are : {} \n".format(Commands), "utf8"))

		elif msg.lower() == bytes("/users", "utf8"):
			client.send(bytes("Connected users are : ({}) \n".format(len(users), users), "utf8"))

		elif msg.lower() == bytes("/leave", "utf8"):
			client.close()
			client.send(bytes("The user %s has left the chatroom" %username, "utf8"))
			del connected_clients[client]
			break

		else:
			broadcast(msg, username + ": ", client)