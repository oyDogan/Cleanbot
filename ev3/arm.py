import ev3dev.ev3 as ev3
from time import sleep

claw  = ev3.Motor('outA')
joint = ev3.LargeMotor('outB')
rotor = ev3.LargeMotor('outD')

def demo():
    print("Demo")
    grab()
    raiseJoint()
    rotateRight()
    sleep(2)
    rotateLeft()
    sleep(2)
    rotateLeft()
    sleep(2)
    rotateRight()
    sleep(5)
    lowerJoint()
    grab()

def raiseJoint():
    print("Open joint")
    joint.run_timed(time_sp=1000,speed_sp=-1000,stop_action="hold")

def lowerJoint():
    print("Lower joint")
    joint.run_timed(time_sp=1000,speed_sp=1000,stop_action="hold")

def releaseJoint():
    print("Release joint")
    joint.run_timed(time_sp=100,speed_sp=100,stop_action="coast")

def openClaw():
    print("Open claw")
    claw.run_timed(time_sp=500,speed_sp=150,stop_action="hold")

def closeClaw():
    print("Close claw")
    claw.run_timed(time_sp=500,speed_sp=-150,stop_action="hold")

def grab() :
    print("Grab")
    openClaw()
    sleep(5)
    closeClaw()

def rotateLeft() :
    print("Rotate left")
    rotor.run_to_rel_pos(position_sp=700*4, speed_sp=-200, stop_action="hold")

def rotateRight() :
    print("Rotate right")
    rotor.run_to_rel_pos(position_sp=-700*4, speed_sp=200, stop_action="hold")

joint.run_timed(time_sp=300,speed_sp=-1000,stop_action="hold")
