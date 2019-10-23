# This script is used as the initial end-point for the Alexa skill
# This script listens on port 5000 for incoming requests
import logging
from socketIO_client import SocketIO
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)

ask = Ask(app,"/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

# print("LOGIN")

# Using SocketIo library to link to the local web socket
socket = SocketIO('https://4768359b.ngrok.io')
print("Working")

# Assigning the Hello intent to a function that returns a message
@ask.intent("HelloIntent")
def hello():
    welcome_message = render_template('hello')
    return question(welcome_message)

# Assigns a the Move intent to a function that can send the direction to the web socket
@ask.intent("MoveIntent", mapping={'direction':"Direction"})
def move(direction) :
    # Printing out the direction for testing
    print("Direction")
    print(direction)
    # Emitting to the web socket
    socket.emit("move",direction)
    move_message = render_template('move',direction=direction)
    return statement(move_message)

# Assigns the Stop intent to a function that can send the command to the web socket
@ask.intent("StopIntent")
def stop():
    # Prints out the call for testing
    print("Stop")
    # Emits the command to the socket
    socket.emit("move","stop")
    stop_message = render_template('stop')
    return statement(stop_message)

# Assigns the Grab intent to a function that sends the command to the web socket
@ask.intent("GrabIntent")
def grab():
    # Prints the call for testing
    print("Grab")
    # Emits the command to the socket
    socket.emit("claw","grab")
    grab_message = render_template('grab')
    return statement(grab_message)

# Assigns the release intent to a function that sends the command to the websocket
@ask.intent("ReleaseIntent")
def release():
    # Prints the call for testing
    print("Release")
    # Emits the command to the socket
    socket.emit("claw","release")
    release_message = render_template('release')
    return statement(release_message)

# Assigns the Turn Arm intent to a function that sends the command and direction to the websocket
@ask.intent("TurnArmIntent", mapping={'direction':'Arm_Direction'})
def turnArm(direction):
    # Prints the call and arm direction for testing
    print("Turn arm")
    print(direction)
    # Emits the command to the socket
    socket.emit("arm",direction)
    turn_message = render_template('turn',direction=direction)
    return statement(turn_message)

if __name__ == '__main__':
    # Stops requests being verified to ensure they were sent from Amazon Alexa Service
    # This should not be used during production as it is not safe and could lead to requests 
    # that have been tampered with
    # This is used because NGrok causes requests to not be verified
    app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)

# Method to print for testing
def connected():
    print("Connected to web socket")

# Link method to ensure that socket is connecting properly
socket.on('connect',connected)
