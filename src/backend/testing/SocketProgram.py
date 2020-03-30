#############################################################################
# Author: Jayden Lee (Jayden.Lee@student.uts.edu.au), Vivian Huynh, Albert
# - Feurgson
# Date: 27/08/19
# Purpose: Socket Programming Assignment for Network Fundamentals. 
#############################################################################

#############################################################################

import socket

#############################################################################
# Input: Port(The one we want to run on), Debug 
# This function takes an IP Address and a Socket and creates a HTTP Web Server
# that will send a file to the client requesting it. 
# Output: NULL
#############################################################################

def HTTPServer(Port, Debug):

	serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

	# Creating a socket object from socket "namespace" or module and 
	# taking the socket variables and use them for the inputs of the function

	toBind = '', Port

	# Python String Manipulation where '' is nothing the use of , adds a space
	# between the bank information and Port so it looks like " 80" to the function
	# in terms of a string

	serverSocket.bind(toBind) # Default Port of 80 for HTTP
	serverSocket.listen(1) # Enables listening on the Port specified

	while True:
		#Establish the connection
		print('Ready to serve...')
		connectionSocket, addr = serverSocket.accept()
		# Creates the connectionSocket, which we use for recieving and sending of
		# http information
		# and we also get the address of the host requesting the document.  
		print("Requried Connection", addr) 
		# Printing the address

		# Try and except in Python works so if we detect and error, it sends us to 
		# the except "clause" ---- Albert help me with my terminology. 

		try:
			message = connectionSocket.recv(1024) # Recieves 1024 bytes from
			# the client. Here it is taking in the file that the client is 
			# looking for, example index.html or HelloWorld.html. This actually
			# recieves the HTTP header information and we break it apart

			filename = message.split()[1]
			# Splits the inbound TCP header information and extracts the file name
			if Debug == 1:
				print(filename)
				print("\n")

			fileObject = open(filename[1:])
			# Remove the /from the HTTP header.

			# Opens the file to the fileObject, starting from the first position.
			outputdata = fileObject.read()

			# Here it reads the objects and turns it into something 
			# that is read-able by Python
			# and we can then send this. 

			if Debug == 1: # To understand WTAF is going on.
				print(message)
				print("\n")
				print(outputdata)
				print("\n")

			for i in range(0, len(outputdata)): # Python Loop for size of outputData            
				connectionSocket.send(outputdata[i].encode()) #Send the data out, letter by letter
				# might be able to use sendall but idk. 

			connectionSocket.send("\r\n".encode()) 
			# I think this is show that it is the end of the header lines. 	

			fileObject.close()
			connectionSocket.close()
		except IOError:

			fileObject = open("404.html") # If we catch an IO error and the file doesn't exist
			outputdata = fileObject.read() # we read the 404.html

			for i in range(0, len(outputdata)): # Python Loop for size of outputData            
				connectionSocket.send(outputdata[i].encode()) # and send back the 404.html page
			connectionSocket.close() # and then close the connection


#############################################################################
# 								Main Code. 
#############################################################################

blank = HTTPServer(80, 1)
