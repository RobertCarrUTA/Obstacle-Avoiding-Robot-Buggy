*README.md is still under construction*
# Obstacle Avoiding Robot Buggy

## Table of Contents
- Obstacle Avoiding Robot Buggy
  * [About the Project](#about-the-project)
  * [Compile Instructions](#compile-instructions)
  * [Part List](#part-list)

## About the Project
Python was used to create this robotic Raspberry Pi project. Ultra sonic distance senors will allow the robot to avoid obstacles while driving forward. The forward, left, or right motion of the robot is controlled by two DC motors with attached wheels. In order for the robot to detect objects in front of it, it sends a pulse from its ultrasonic distance sensors. As soon as the robot detects an object 20 centimeters ahead of it, it will stop, turn left until no more obstructions are detected, then move forward again.

## Compile Instructions
You need to know how GPIO pins work on the Raspberry Pi 3B, 3B+, or 4 to run this program. I recommend looking up a GPIO reference card for your model.
* After all the connections are made correctly, type **python3 buggy.py** into the terminal where this file is located.

## Part List
*I would reccomend getting good quality parts, my wires ended up breaking and my motor controller board arrived broken. Upon order of the parts online from AliExpress, delivery was expected in 30-50 days.*
* Raspberry Pi 3B, 3B+, or 4
* Motor controller board (Model I used - L298 Dual H-Bridge)
* Two 3V-6V DC motors
* Two wheels that fit the two motors
* Ball caster
* Ultrasonic distance sensor (UDS) (HC-SR04P (3.3V Tolerant) or HC-SR04 (5V))
  * If using a 5V UDS, you will need to split the voltage to output 3.3V using two resistors
* Jumper leads (I would take cable length into consideration, female-to-female and male-to-female)
* Battery holder (if you want it to move freely of a power cable)
* A small chasis for the buggy (I used cardboard)
