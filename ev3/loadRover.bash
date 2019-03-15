#!/bin/bash

scp rover.py robot@ev3dev.local:~
ssh robot@ev3dev.local
maker
python3 rover.py