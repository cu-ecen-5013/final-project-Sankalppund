# FileName: Client-Publisher.py
# Auther: Sankalp Pund
# Description: This python script runs as mqtt client
# Reference: https://github.com/eclipse/paho.mqtt.python

#Importing Modules
try:
	import paho
	import sys
	import paho.mqtt.client as mqtt
#Error checking for module import
except Exception as e:
	print(e)

#port is the network port of the server host to connect to.
Port=1883
# Maximum period in seconds between communications with the broker.
Keepalive=60
try:
	print("Client 2 Sending Humidity data")
	# Client Constructor
	# Function Defination: https://github.com/eclipse/paho.mqtt.python#client-1
	client = mqtt.Client()

	#IP address of the remote broker accepting 
	#from command line argument.
	String = sys.argv[-1]
	Humidity_Data="H"+String
	IP_Address = "10.0.0.20"
	#Connect to a remote broker.
	#Function defination:https://github.com/eclipse/paho.mqtt.python/blob/1eec03edf39128e461e6729694cf5d7c1959e5e4/src/paho/mqtt/client.py#L908
	try:
		client.connect(IP_Address,Port,Keepalive)

	#Publish a message on a topic.
	#This causes a message to be sent to the broker and subsequently from
    #the broker to any clients subscribing to matching topics.
    #Function defination:https://github.com/eclipse/paho.mqtt.python/blob/1eec03edf39128e461e6729694cf5d7c1959e5e4/src/paho/mqtt/client.py#L1199
		client.publish("topic/test",Humidity_Data);
	
	#If network goes down, sensor data appended locally and saved into txt file on client-side.
	except Exception as e:
		print (e)
		backup = open('/usr/humidity_backup.txt', 'a')
	 	backup.write(String)
  	 	backup.write("\n")
  	 	backup.close()

#Error Checking for script. 
except Exception as e:
	print(e)

