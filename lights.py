import socket
import time

#Hex packet which should be recieved after subscription UDP packet sent if light is on
subscribe_recieve_on = "<Add yours here using hex generator>"

#Hex packet which should be recieved after subscription UDP packet sent if light is off
subscribe_recieve_off = "<Add yours here using hex generator>"

#Hex packet which should be recieved after poweron UDP packet sent
poweron_recieve = "<Add yours here using hex generator>"

#Hex packet which should be recieved after poweroff UDP packet sent
poweroff_recieve = "<Add yours here using hex generator>"

UDP_IP = "<Add yours Orvibo IP address here>"
UDP_SERVER_IP = "Add your Computer IP Address here"
UDP_PORT = 10000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def poweron():
	MESSAGE = '<Add yours here using hex generator>'.decode('hex')
	sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
	print ('Poweron to light sent')



def poweroff():
	MESSAGE = '<Add yours here using hex generator>'.decode('hex')
	sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
	print ('Poweroff to light sent')


def subscribe():
	MESSAGE = '<Add yours here using hex generator>'.decode('hex')
	sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
	recieve_data = recieve()
	print ('Subscribition to light sent')

#Run this at the same time or straight after sending packets. This will catch the return packet. Using subscribe_recieve_on or subscribe_recieve_off
#to determine whether a device is on or off.
def recieve():
	global error_value
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP	
	sock.bind((UDP_SERVER_IP, UDP_PORT))
	data, addr = sock.recvfrom(1024)
	return data.encode('hex')
