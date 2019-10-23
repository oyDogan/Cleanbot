# This script should be run on the Ev3 P-brick on the Rover brick
# It is designed to connect to a web socket and move based on incoming messages
from socketIO_client import SocketIO
import ev3dev.ev3 as ev3
from time import sleep

# Assigns the back left motor to a variable
backLeftMotor = ev3.LargeMotor('outD')
# Assigns the back right motor to a variable
backRightMotor = ev3.LargeMotor('outB')
# Assigns the front left motor to a variable
frontLeftMotor = ev3.LargeMotor('outC')
# Assigns the front right motor to a variable
frontRightMotor = ev3.LargeMotor('outA')
# Assigns the front left ultrasonic sensor to a variable
leftFrontSensor = ev3.UltrasonicSensor('in3')
# Assigns the side left ultrasonic sensor to a variable
leftSideSensor = ev3.UltrasonicSensor('in2')
# Assigns the side right ultrasonic sensor to a variable
rightSideSensor = ev3.UltrasonicSensor('in3')
# Assigns the front right ultrasonic sensor to a variable
rightFrontSensor = ev3.UltrasonicSensor('in4')

# As use of the side sensors is still temporamental, only check the front sensors

# Sets the distance measurement for the front left sensor
# leftFrontSensor.mode = 'US-DIST-CM'
# # Sets the distance measurement for the front right sensor
# rightFrontSensor.mode = 'US-DIST-CM'

# Sets the volume of the Ev3 to 100%
ev3.Sound.set_volume(100)
# For testing purposes
print("WORKING")
# Connects to the web socket
socket = SocketIO('https://4768359b.ngrok.io')
# For testing, prints once the SocketIO begins to connection with the web socket
print("SocketIO started")

# Temporamental values used for the moveAround function
leftTurns = 0
rightTurns = 0
leftProportion = 0.5
rightProportion = 0.5

# Called when the web socket has been connected to
def onConnect():
    print('Connected to Cloud, Dude', socket.transport_name)

# The intention for moveAround was to be able to have the ev3 able to drive around and avoid objects
# However this code is temporamental and does not always work, attempts were made to make this code 
# self-learning about a specific room
def moveAround():
    # Attempts to hold values for the amount of left and right turns
    global leftTurns
    global rightTurns
    # The CM value for how close the rover should be before it needs to move and turn
    turningDistance = 250
    leftTurns
    rightTurns
    # Printed for testing
    print("Move around")
    # This function constantly runs until a new function is called
    running = True
    while(running):
        # Getting the distance for the front sensors
        distance1 = leftFrontSensor.value()
        distance4 = rightFrontSensor.value()
        # Printing out the values for distance for testing
        print("Distance 1 : " + str(distance1) + " Distance 4 : " + str(distance4))
        # Checks if both sensors are too close to an object
        if(distance1 <= turningDistance and distance4 <= turningDistance):
            # stopMoving()
            # Used as part of the temporamental approach, turning more to one side if there was a higher change that turning to one side will lead to a object free way
            # The code inside this if else statement is effectively the same, however the first statement
            # Moves to the right, because there is less of a chance of less turn moving to a open space
            if(leftProportion < rightProportion):
                # Moving right
                moveRight()
                # Check if the rover still has an obstacle in the way after turning right
                if(leftFrontSensor.value() <= turningDistance and rightFrontSensor.value() <= turningDistance):
                    # Move left, moving twice to go back to the original centering of rover and then moving left
                    moveLeft()
                    moveLeft()
                    # Check if rover still has an obstacle in the way after turning left
                    if(leftFrontSensor.value() <= turningDistance and rightFrontSensor.value() <= turningDistance):
                        # Turn back on itself
                        moveLeft()
                    else :
                        # Since there is no obstacle in the way add to left turns, and change the proportions of chance
                        leftTurns = leftTurns + 1
                        changeProportions()
                else :
                    # If no obstacle in the way, add to right turns and change the proportions of chance
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
        # Check if the turning distance of the left sensor is shorter than the turning distance
        # Hence the obstacle is on the left side of the robot
        elif(distance1 <= turningDistance - 25):
            # Move slightly to the right
            shiftRight()
        # Checks if the turning distance is shorter on the right sensor
        # Hence the obstacle is on the right side
        elif(distance4 <= turningDistance - 25):
            # Move slightly to the left
            shiftLeft()
        else :
            moveForward()

# Used to delegate the moveIntent direction to a function
def moveCommand(command):
    # Prints the call can command for testing
    print("Command move " + command)
    # Delegate the command
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
    elif(command == "around"):
        moveAround()
    else :
        stopMoving()

# Used to move a specific motor in one direction
def moveMotor(motor,direction,time):
    # All the code inside each if statement is essentially the same
    # However they are for different motors
    if(motor == 'frontLeft'):
        # These if statements are also different in the direction the motor is being turned
        if(direction == 'forward'):
            # This if statement checks if the time argument is set 
            # If not the motor should continually run
            if(time == 0):
                frontLeftMotor.run_forever(speed_sp=300)
            elif(time > 0):
                # If the time argument is set, the motor runs for that amount of time
                frontLeftMotor.run_timed(time_sp=time,speed_sp=300)
        elif(direction == 'backward'):
            if(time == 0):
                frontLeftMotor.run_forever(speed_sp=-300)
            elif(time > 0):
                frontLeftMotor.run_timed(time_sp=time,speed_sp=-300)
    elif(motor == 'frontRight'):
        if(direction == 'forward'):
            if(time == 0):
                frontRightMotor.run_forever(speed_sp=300)
            elif(time > 0):
                frontRightMotor.run_timed(time_sp=time,speed_sp=300)
        elif(direction == 'backward'):
            if(time == 0):
                frontRightMotor.run_forever(speed_sp=-300)
            elif(time > 0):
                frontRightMotor.run_timed(time_sp=time,speed_sp=-300)
    elif(motor == 'backLeft'):
        if(direction == 'forward'):
            if(time == 0):
                backLeftMotor.run_forever(speed_sp=-300)
            elif(time > 0):
                backLeftMotor.run_timed(time_sp=time,speed_sp=-300)
        elif(direction == 'backward'):
            if(time == 0):
                backLeftMotor.run_forever(speed_sp=300)
            elif(time > 0):
                backLeftMotor.run_timed(time_sp=time,speed_sp=300)
    elif(motor == 'backRight'):
        if(direction == 'forward'):
            if(time == 0):
                backRightMotor.run_forever(speed_sp=-300)
            elif(time > 0):
                backRightMotor.run_timed(time_sp=time,speed_sp=-300)
        elif(direction == 'backward'):
            if(time == 0):
                backRightMotor.run_forever(speed_sp=300)
            elif(time > 0):
                backRightMotor.run_timed(time_sp=time,speed_sp=300)

# moveForward calls move motor methods to move the rover forward
def moveForward():
    moveMotor('frontLeft','forward',0)
    moveMotor('frontRight','forward',0)
    moveMotor('backLeft','forward',0)
    moveMotor('backRight','forward',0)

# moveBackward moves the rover backwards
def moveBackward():
    moveMotor('frontLeft','backward',0)
    moveMotor('frontRight','backward',0)
    moveMotor('backLeft','backward',0)
    moveMotor('backRight','backward',0)

# moveLeft turns the rover -90 degrees
def moveLeft():
    frontLeftMotor.run_to_rel_pos(position_sp=-720, speed_sp=300, stop_action="hold")
    frontRightMotor.run_to_rel_pos(position_sp=720, speed_sp=300, stop_action="hold")
    backLeftMotor.run_to_rel_pos(position_sp=720, speed_sp=300, stop_action="hold")
    backRightMotor.run_to_rel_pos(position_sp=-720, speed_sp=300, stop_action="hold")
    # The sleep statement is needed otherwise the rover will only move left slowly then move forwards
    sleep(1.5)

# moveRight turns the rover 90 degrees
def moveRight():
    frontLeftMotor.run_to_rel_pos(position_sp=720, speed_sp=300, stop_action="hold")
    frontRightMotor.run_to_rel_pos(position_sp=-720, speed_sp=300, stop_action="hold")
    backLeftMotor.run_to_rel_pos(position_sp=-720, speed_sp=300, stop_action="hold")
    backRightMotor.run_to_rel_pos(position_sp=720, speed_sp=300, stop_action="hold")
    # The sleep statement is needed because the rover needed to move until the rover has turned fully
    sleep(1.5)
    
# This shifts the rover slightly to the right
def shiftRight():
    moveMotor('frontLeft','forward',0)
    moveMotor('frontRight','backward',0)
    moveMotor('backLeft','forward',0)
    moveMotor('backRight','backward',0)

# This shifts the rover slightly to the left
def shiftLeft():
    moveMotor('frontLeft','backward',0)
    moveMotor('frontRight','forward',0)
    moveMotor('backLeft','backward',0)
    moveMotor('backRight','forward',0)

# This changes the proportions or 'chance' that turning left or right would lead to a space
# with no obstacles
def changeProportions():
    global leftProportion
    global rightProportion
    totalTurns = leftTurns + rightTurns
    leftProportion = leftTurns/totalTurns
    rightProportion = rightTurns/totalTurns

# This stops the rover moving
def stopMoving():
    frontLeftMotor.stop()
    frontRightMotor.stop()
    backLeftMotor.stop()
    backRightMotor.stop()

# This links the connect and move messages to functions that can delegate the action
socket.on('connect',onConnect)
socket.on('move',moveCommand)

# Makes the socket wait for responses
socket.wait()
