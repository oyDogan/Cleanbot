from socketIO_client import socketIO
import ev3dev.ev3 as env3
import time

frontLeftMotor = eve3.largeMotor('C')
frontRightMotor = eve3.largeMotor('B')
backLeftMotor = eve3.largeMotor('D')
backRightMotor = eve3.largeMotor('A')

ev3.Sound.set_volume(100)

socket = SocketIO('http://alexaev3api.azurewebsites.net')


def onConnect():
    print('Connected to Cloud, Dude', socket.transport_name)

def moveCommand(command):
    print("Command move " + command)
    if(command == 'forward'):
        moveForward()
    elif(command == 'backward'):
        moveBackward()
    elif(command == 'left'):
        moveLeft()
    elif(command == 'right'):
        moveRight()
    else:
        stopMoving()

def moveMotor(motor,direction):
    if(motor == 'frontLeft'):
        if(direction == 'forward'):
            frontLeftMotor.run_forever(speed_sp=500)
        elif(direction == 'backward'):
            frontLeftMotor.run_forever(speed_sp=-500)
    elif(motor == 'frontRight'):
        if(direction == 'forward'):
            frontRightMotor.run_forever(speed_sp=500)
        elif(direction == 'backward'):
            frontRightMotor.run_forever(speed_sp=-500)
    elif(motor == 'backLeft'):
        if(direction == 'forward'):
            backLeftMotor.run_forever(speed_sp=-500)
        elif(direction == 'backward'):
            backLeftMotor.run_forever(speed_sp=500)
    elif(motor == 'backRight'):
        if(direction == 'forward'):
            backRightMotor.run_forever(speed_sp=-500)
        elif(direction == 'backward'):
            backRightMotor.run_forever(speed_sp=500)

def moveForward():
    moveMotor('frontLeft','forward')
    moveMotor('frontRight','forward')
    moveMotor('backLeft','forward')
    moveMotor('backRight','forward')

def moveBackward():
    moveMotor('frontLeft','backward')
    moveMotor('frontRight','backward')
    moveMotor('backLeft','backward')
    moveMotor('backRight','backward')

def moveLeft():
    moveMotor('frontLeft','backward')
    moveMotor('frontRight','forward')
    moveMotor('backLeft','backward')
    moveMotor('backRight','forward')


def moveRight():
    moveMotor('frontLeft','forward')
    moveMotor('frontRight','backward')
    moveMotor('backLeft','forward')
    moveMotor('backRight','backward')

def stopMoving():
    frontLeftMotor.stop()
    frontRightMotor.stop()
    backLeftMotor.stop()
    backRightMotor.stop()


socket.on('connect',onConnect)
socket.on('move',moveCommand)

socket.wait()
