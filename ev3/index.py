from socketIO_client import SocketIO
import ev3dev.ev3 as ev3
import time

backLeftMotor = ev3.LargeMotor('outC')
backRightMotor = ev3.LargeMotor('outB')
frontLeftMotor = ev3.LargeMotor('outD')
frontRightMotor = ev3.LargeMotor('outA')

ir = ev3.UltrasonicSensor()
assert ir.connected, "Connect a single infrared sensor to any sensor port"

ir.mode = 'US-DIST-CM'

ev3.Sound.set_volume(100)
print("WORKING")
socket = SocketIO('http://alexaev3api.azurewebsites.net')
# socket = SocketIO('http://bd9c8794.ngrok.io')
print("LINE 15")

def onConnect():
    print('Connected to Cloud, Dude', socket.transport_name)

def moveAround():
    print("Move around")
    running = True
    turning = False

    while(running):
        moveForward()
        distance = ir.value()

        if(distance <= 175):
            turning = True
            while(turning):
                if(frontLeftMotor.is_running == false):
                    moveLeft()
                    turnDistance = ir.value()
                    if(turnDistance >= 200):
                        turning = False






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

def moveMotor(motor,direction,time):
    if(motor == 'frontLeft'):
        if(direction == 'forward'):
            if(time == 0):
                frontLeftMotor.run_forever(speed_sp=500)
            elif(time > 0):
                frontLeftMotor.run_timed(time_sp=time,speed_sp=500)
        elif(direction == 'backward'):
            if(time == 0):
                frontLeftMotor.run_forever(speed_sp=-500)
            elif(time > 0):
                frontLeftMotor.run_timed(time_sp=time,speed_sp=-500)
    elif(motor == 'frontRight'):
        if(direction == 'forward'):
            if(time == 0):
                frontRightMotor.run_forever(speed_sp=500)
            elif(time > 0):
                frontRightMotor.run_timed(time_sp=time,speed_sp=500)
        elif(direction == 'backward'):
            if(time == 0):
                frontRightMotor.run_forever(speed_sp=-500)
            elif(time > 0):
                frontRightMotor.run_timed(time_sp=time,speed_sp=-500)
    elif(motor == 'backLeft'):
        if(direction == 'forward'):
            if(time == 0):
                backLeftMotor.run_forever(speed_sp=-500)
            elif(time > 0):
                backLeftMotor.run_timed(time_sp=time,speed_sp=-500)
        elif(direction == 'backward'):
            if(time == 0):
                backLeftMotor.run_forever(speed_sp=500)
            elif(time > 0):
                backLeftMotor.run_timed(time_sp=time,speed_sp=500)
    elif(motor == 'backRight'):
        if(direction == 'forward'):
            if(time == 0):
                backRightMotor.run_forever(speed_sp=-500)
            elif(time > 0):
                backRightMotor.run_timed(time_sp=time,speed_sp=-500)
        elif(direction == 'backward'):
            if(time == 0):
                backRightMotor.run_forever(speed_sp=500)
            elif(time > 0):
                backRightMotor.run_timed(time_sp=time,speed_sp=500)

def moveForward():
    moveMotor('frontLeft','forward',0)
    moveMotor('frontRight','forward',0)
    moveMotor('backLeft','forward',0)
    moveMotor('backRight','forward',0)

def moveBackward():
    moveMotor('frontLeft','backward',0)
    moveMotor('frontRight','backward',0)
    moveMotor('backLeft','backward',0)
    moveMotor('backRight','backward',0)

def moveLeft():
    moveMotor('frontLeft','backward',2500)
    moveMotor('frontRight','forward',2500)
    moveMotor('backLeft','backward',2500)
    moveMotor('backRight','forward',2500)


def moveRight():
    moveMotor('frontLeft','forward',2500)
    moveMotor('frontRight','backward',2500)
    moveMotor('backLeft','forward',2500)
    moveMotor('backRight','backward',2500)

def stopMoving():
    frontLeftMotor.stop()
    frontRightMotor.stop()
    backLeftMotor.stop()
    backRightMotor.stop()

moveAround()

socket.on('connect',onConnect)
socket.on('move',moveCommand)

socket.wait()
