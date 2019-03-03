import logging
from socketIO_client import SocketIO
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)

ask = Ask(app,"/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

print("LOGIN")

socket = SocketIO('http://bd8d4020.ngrok.io')

@ask.intent("HelloIntent")
def hello():
    welcome_message = render_template('hello')
    return question(welcome_message)

@ask.intent("MoveIntent", mapping={'direction':"Direction"})
def move(direction) :
    print("Direction")
    print(direction)
    socket.emit("move",direction)
    move_message = render_template('move')
    return statement(move_message)

if __name__ == '__main__':
    app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)


def connected():
    print("Connected")

socket.on('connect',connected)
