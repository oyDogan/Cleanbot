import logging
from socketIO_client import SocketIO
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)

ask = Ask(app,"/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

print("LOGIN")

socket = SocketIO('http://localhost',1337)

@ask.intent("HelloIntent")
def hello():
    welcome_message = render_template('hello')
    return question(welcome_message)

@ask.intent("MoveIntent", mapping={'direction':"Direction"})
def move(direction) :
    print("Direction")
    print(direction)
    socket.emit("move",direction)
    move_message = render_template('move',direction=direction)
    return statement(move_message)

@ask.intent("StopIntent")
def stop():
    print("Stop")
    socket.emit("move","stop")
    stop_message = render_template('stop')
    return statement(stop_message)

@ask.intent("GrabIntent")
def grab():
    print("Grab")
    socket.emit("claw","grab")
    grab_message = render_template('grab')
    return statement(grab_message)

@ask.intent("ReleaseIntent")
def release():
    print("Release")
    socket.emit("claw","release")
    release_message = render_template('release')
    return statement(release_message)

@ask.intent("TurnArmIntent", mapping={'direction':'Arm_Direction'})
def turnArm(direction):
    print("Turn arm")
    print(direction)
    socket.emit("arm",direction)
    turn_message = render_template('turn',direction=direction)
    return statement(turn_message)

if __name__ == '__main__':
    app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)


def connected():
    print("Connected")

socket.on('connect',connected)
