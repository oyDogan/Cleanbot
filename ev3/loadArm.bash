#!/bin/bash

scp arm.py robot@ev3dev.local:~
maker
ssh robot@ev3dev.local
maker
python3 arm.py