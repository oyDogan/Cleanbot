#!/bin/bash

scp rover.py robot@ev3dev.local:~
maker
ssh robot@ev3dev.local
maker
python3 rover.py