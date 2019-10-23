# This script should be run on the Ev3 P-brick on the Arm brick
# It is designed to connect to a web socket and move based on incoming messages
from socketIO_client import SocketIO
import ev3dev.ev3 as ev3
from time import sleep

# Assigns a variable for the claw motor
claw  = ev3.Motor('outD')
# Assigns a variable for the joint motor
joint = ev3.LargeMotor('outC')
# Assigns a variable for the rotor joint motor
rotor = ev3.LargeMotor('outB')

# Uses the SocketIO library to connect to the web socket 
socket = SocketIO("https://5bae97fe.ngrok.io")

# Called when a GrabIntent or ReleaseIntent is sent from the web socket
# This function delegates and calls which function should act on the command
def clawCommand(action):
    # Prints out the call and action for testing
    print('Claw command : ' + action)
    # Delegating function based on action variable
    if(action == "grab"):
        closeClaw()
    else :
        openClaw()

# Called when the TurnArmIntent is sent from the web socket
def armCommand(direction):
    # Prints out the call and direction
    print("Arm command : " + direction)
    # Delegates the function based on the direction variable
    if(direction == "up"):
        raiseJoint()
    elif(direction == "down"):
        lowerJoint()
    elif(direction == "left"):
        rotateLeft()
    elif(direction == "right"):
        rotateRight()
    else :
        releaseJoint()

# Raises the arm joint and holds it in place
def raiseJoint():
    # Printed call for testing
    print("Open joint")
    # Tells the motor to run for a second at the highest speed recommended
    joint.run_timed(time_sp=1000,speed_sp=-1000,stop_action="hold")

# Lowers the arm joint and holds it in place
def lowerJoint():
    # Printed call for testing
    print("Lower joint")
    # Tells the motor to move forwards for 1 second at the highest speed recommened
    joint.run_timed(time_sp=1000,speed_sp=1000,stop_action="hold")

# Releases the arm joint, lowereing it fully
def releaseJoint():
    # Printed call for testing
    print("Release joint")
    # Tells the motor to run for 0.1 seconds, the stop_action of coast removes power from the motor
    joint.run_timed(time_sp=100,speed_sp=100,stop_action="coast")

# Opens the claw
def openClaw():
    # Printed call for testing
    print("Open claw")
    # Tells the motor to spin forwards at a slow speed for 0.5 seconds
    # This is because the claw has a very small motion it requires to open
    claw.run_timed(time_sp=500,speed_sp=150,stop_action="hold")

# Closes the claw
def closeClaw():
    # Printed call for testing
    print("Close claw")
    # Tells the motor to spin backwards with a very small motion for 0.5 seconds
    claw.run_timed(time_sp=500,speed_sp=-150,stop_action="hold")

# Used to grab an item, opens and closes the claw
def grab() :
    # Printed call for testing
    print("Grab")
    # Call to open the claw
    openClaw()
    # Stops for a 5 seconds
    sleep(5)
    # Call to close the claw
    closeClaw()

# Rotates the arm left
def rotateLeft() :
    # Printed call for testing
    print("Rotate left")
    # Tells the motor to rotate the arm as close to -90 degrees as possible
    rotor.run_to_rel_pos(position_sp=700*4, speed_sp=-200, stop_action="hold")

# Rotates the arm right
def rotateRight() :
    # Printed call for testing
    print("Rotate right")
    # Tells the motor to rotate the arm as close to 90 degrees as possible
    rotor.run_to_rel_pos(position_sp=-700*4, speed_sp=200, stop_action="hold")

# Links any claw messages to the function to delegate the action
socket.on('claw',clawCommand)

# Links any arm messages to the function to delegate the action
socket.on('arm',armCommand)

# Makes the socket client wait for messages
socket.wait()