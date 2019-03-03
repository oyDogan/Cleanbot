from socketIO_client import SocketIO
import ev3dev.ev3 as ev3
from time import sleep

backLeftMotor = ev3.LargeMotor('outC')
backRightMotor = ev3.LargeMotor('outB')
frontLeftMotor = ev3.LargeMotor('outD')
frontRightMotor = ev3.LargeMotor('outA')

leftFrontSensor = ev3.UltrasonicSensor('in1')
leftSideSensor = ev3.UltrasonicSensor('in2')
rightSideSensor = ev3.UltrasonicSensor('in3')
rightFrontSensor = ev3.UltrasonicSensor('in4')

assert leftFrontSensor.connected, "Connect a single ultrasonic sensor to any sensor port"
assert rightFrontSensor.connected, "Connect a single ultrasonic sensor to any sensor port"

leftFrontSensor.mode = 'US-DIST-CM'
rightFrontSensor.mode = 'US-DIST-CM'

ev3.Sound.set_volume(100)
print("WORKING")
# socket = SocketIO('http://alexaev3api.azurewebsites.net')
# socket = SocketIO('http://bd8d4020.ngrok.io')
print("LINE 15")

leftTurns = 0
rightTurns = 0
leftProportion = 0.5
rightProportion = 0.5

def onConnect():
    print('Connected to Cloud, Dude', socket.transport_name)

def moveAround():
    global leftTurns
    global rightTurns
    turningDistance = 250
    leftTurns
    rightTurns
    print("Move around")
    running = True

    while(running):
        distance1 = leftFrontSensor.value()
        distance4 = rightFrontSensor.value()
        print("Distance 1 : " + str(distance1) + " Distance 4 : " + str(distance4))
        if(distance1 <= turningDistance and distance4 <= turningDistance):
            # stopMoving()
            if(leftProportion > rightProportion):
                moveRight()
                if(leftFrontSensor.value() <= turningDistance and rightFrontSensor.value() <= turningDistance):
                    moveLeft()
                    moveLeft()
                    if(leftFrontSensor.value() <= turningDistance and rightFrontSensor.value() <= turningDistance):
                        moveLeft()
                    else :
                        leftTurns = leftTurns + 1
                        changeProportions()
                else :
                    rightTurns = rightTurns + 1
                    changeProportions()
            else :
                moveLeft()
                if(leftFrontSensor.value() <= turningDistance and rightFrontSensor.value() <= turningDistance):
                    moveRight()
                    moveRight()
                    if(leftFrontSensor.value() <= turningDistance and rightFrontSensor.value() <= turningDistance):
                        moveRight()
                    else :
                        rightTurns = rightTurns + 1
                        changeProportions()
                else :
                    leftTurns = leftTurns + 1
                    changeProportions()
        elif(distance1 <= turningDistance - 25):
            shiftRight()
        elif(distance4 <= turningDistance - 25):
            shiftLeft()
        else :
            moveForward()






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
    elif(command == "stop"):
        stopMoving()
    else :
        stopMoving()

def moveMotor(motor,direction,time):
    if(motor == 'frontLeft'):
        if(direction == 'forward'):
            if(time == 0):
                frontLeftMotor.run_forever(speed_sp=1000)
            elif(time > 0):
                frontLeftMotor.run_timed(time_sp=time,speed_sp=1000)
        elif(direction == 'backward'):
            if(time == 0):
                frontLeftMotor.run_forever(speed_sp=-1000)
            elif(time > 0):
                frontLeftMotor.run_timed(time_sp=time,speed_sp=-1000)
    elif(motor == 'frontRight'):
        if(direction == 'forward'):
            if(time == 0):
                frontRightMotor.run_forever(speed_sp=1000)
            elif(time > 0):
                frontRightMotor.run_timed(time_sp=time,speed_sp=1000)
        elif(direction == 'backward'):
            if(time == 0):
                frontRightMotor.run_forever(speed_sp=-1000)
            elif(time > 0):
                frontRightMotor.run_timed(time_sp=time,speed_sp=-1000)
    elif(motor == 'backLeft'):
        if(direction == 'forward'):
            if(time == 0):
                backLeftMotor.run_forever(speed_sp=-1000)
            elif(time > 0):
                backLeftMotor.run_timed(time_sp=time,speed_sp=-1000)
        elif(direction == 'backward'):
            if(time == 0):
                backLeftMotor.run_forever(speed_sp=1000)
            elif(time > 0):
                backLeftMotor.run_timed(time_sp=time,speed_sp=1000)
    elif(motor == 'backRight'):
        if(direction == 'forward'):
            if(time == 0):
                backRightMotor.run_forever(speed_sp=-1000)
            elif(time > 0):
                backRightMotor.run_timed(time_sp=time,speed_sp=-1000)
        elif(direction == 'backward'):
            if(time == 0):
                backRightMotor.run_forever(speed_sp=1000)
            elif(time > 0):
                backRightMotor.run_timed(time_sp=time,speed_sp=1000)

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
    frontLeftMotor.run_to_rel_pos(position_sp=-720, speed_sp=1000, stop_action="hold")
    frontRightMotor.run_to_rel_pos(position_sp=720, speed_sp=1000, stop_action="hold")
    backLeftMotor.run_to_rel_pos(position_sp=720, speed_sp=1000, stop_action="hold")
    backRightMotor.run_to_rel_pos(position_sp=-720, speed_sp=1000, stop_action="hold")
    sleep(1.5)


def moveRight():
    print("Move right")
    frontLeftMotor.run_to_rel_pos(position_sp=720, speed_sp=1000, stop_action="hold")
    frontRightMotor.run_to_rel_pos(position_sp=-720, speed_sp=1000, stop_action="hold")
    backLeftMotor.run_to_rel_pos(position_sp=-720, speed_sp=1000, stop_action="hold")
    backRightMotor.run_to_rel_pos(position_sp=720, speed_sp=1000, stop_action="hold")
    sleep(1.5)
    
def shiftRight():
    moveMotor('frontLeft','forward',0)
    moveMotor('frontRight','backward',0)
    moveMotor('backLeft','forward',0)
    moveMotor('backRight','backward',0)

def shiftLeft():
    moveMotor('frontLeft','backward',0)
    moveMotor('frontRight','forward',0)
    moveMotor('backLeft','backward',0)
    moveMotor('backRight','forward',0)

def changeProportions():
    global leftProportion
    global rightProportion
    totalTurns = leftTurns + rightTurns
    leftProportion = leftTurns/totalTurns
    rightProportion = rightTurns/totalTurns

def stopMoving():
    frontLeftMotor.stop()
    frontRightMotor.stop()
    backLeftMotor.stop()
    backRightMotor.stop()

moveAround()

# socket.on('connect',onConnect)
# socket.on('move',moveCommand)

# socket.wait()
