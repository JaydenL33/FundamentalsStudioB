"""
Last Updated : 30/08/19
Purpose: Socket Programming Assignment for Network Fundamentals. 

Authors: Jayden Lee, Vivian Huynh, Albert Ferguson
"""

# imports
import socket as sc
from datetime import datetime as dt

def HTTPServer(Port, *args, **kwargs):
	"""
	Take a given port to bind to an existing IP address. Default ip 
	address is set to LocalHost, a kwarg option over-rides this.
	This will create a simple HTTP web server to send html page files
	as requested to the client.

	-- Parameters --
	
	Port    the port to bind to __default__ or given ip address

	

	-- Args --

	-D      debug flag, if passed in arg list then verbose level set to max.

	
	-- KwArgs --

	IP      over-ride the default LocalHost definition with a user defined 
			IP address.

	"""

	# Creating a socket object and temp binding variable
	with sc.socket(sc.AF_INET, sc.SOCK_STREAM, 0) as server_socket:
		
		# this must be a tuple
		if 'IP' in kwargs:
			_IP = kwargs.get("IP")
		else:
			_IP = "127.0.0.1" # LocalHost is default

		toBind = (_IP, int(Port))
		server_socket.bind(toBind) 
		# bind the server details so clients have a constant address to contact
		# Then, ennable listening for a defined queue length of clients
		# addition of any integer > 0 will define a backlog limit of 
		# unaccepted connex's, must be at least 1 to accept any init connex's!!
		# further info see docs at: https://docs.python.org/3/library/socket.html
		server_socket.listen(10) 

		while True:
			# now that the server is ready....await a connex'
			print("\t\t#### Ready to serve! ####\n")
			# accept a new handshake connex'
			connection_socket, addr = server_socket.accept()
			print("Acquired Connection at {}:\t{}\n".format(dt.now(), addr))
			# Create a new connex, use to recieve/send http info client <-> server
			# addr is the host IP requesting the document.  

			# In the case that the client requests a non-existant file, except and
			# send them to the 404 error page. But first 'try' to connect them to 
			# the file they req'd
			
			try:
				# now redirect client to their own dedicated socket, pipeline further
				# comms to this socket port.
				GET_req = connection_socket.recv(1024)
				# Recieves 1024 bytes from the client GET req. This is broken down
				# with string manip's to retreive the req'd file name
				if '-D' in args:
					print(GET_req,'\n')

				# file name is second elem of GET list val's
				fn = GET_req.split()[1].decode()

				# set protocol and response message for our new pipeline response
				header = "HTTP/1.1 200 OK\n"				
				return_data = header.encode('utf-8')

				if '-D' in args:
					print(str(fn),'\n', header, '\n')
				else:
					pass

				# now open the file, remove the extraneous '/' with
				# string manip, [1:] means all to end from index = 1
				# with open performs auto close of file on indentation break
				with open(fn[1:], 'rb') as file:
					file_data = file.read() # read the file into memory
					return_data += file_data
					if '-D' in args:
						# verbose mode high, print all arg values for debug check
						print(GET_req, '\n', file_data, '\n')
					else:
						pass

					connection_socket.send(return_data)
					# send EOF vals
					connection_socket.send("\r\n".encode())
					connection_socket.close()
			
			# except IOError is a standard except for file handling errors
			except IOError:
				with open("404.html", 'rb') as file:
					# If we catch an IO error and the file doesn't exist
					return_data = file.read()
					connection_socket.send(return_data)
					# send EOF vals
					connection_socket.send("\r\n".encode())
					connection_socket.close()

HTTPServer(80, IP="134.122.104.123", '-D')