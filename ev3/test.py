from socketIO_client import SocketIO
import logging


socket = SocketIO('http://bd9c8794.ngrok.io')

def moveCommand():
    print("HIHI")
    direction = 'stop'
    print("Hello World")
    socket.emit('move',direction)

def onError():
    print("ERROR")

socket.on('connect',moveCommand)
socket.on('error',onError)

socket.wait()
