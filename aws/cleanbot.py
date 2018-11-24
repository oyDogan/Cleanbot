import logging
from socketIO_client import socketIO
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)

ask = Ask(app,"/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

socket = SocketIO('http://alexaev3api.azurewebsites.net')

@ask.intent("HelloIntent")

def hello():
    welcome_message = render_template('hello')
    return question(welcome_message)

@ask.intent("MoveIntent", mapping={'direction':"Direction"})
def move(direction) :
    socket.emit("move",direction)

if __name__ == '__main__':
    app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)
