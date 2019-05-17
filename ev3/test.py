# This is a script to test the communication from the web socket to the ev3dev

from socketIO_client import SocketIO
import logging

# Connects to the web socket
socket = SocketIO('http://bd9c8794.ngrok.io')

# Sends a move command to the web socket
def moveCommand():
    # Print for testing
    print("Hi")
    # Sets a direction/command
    direction = 'stop'
    # Prints for testing
    print("Hello World")
    # Sends the message to the web socket
    socket.emit('move',direction)

# Alerts if there is an error with the web socket
def onError():
    print("ERROR")

# Connects the functions with messages from the web socket
socket.on('connect',moveCommand)
socket.on('error',onError)

# Makes the socket client wait for the web socket
socket.wait()
