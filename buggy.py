from gpiozero import Robot, InputDevice, OutputDevice
from time import sleep, time

# (7, 8) and (9, 10) represent GPIO pins
robin = Robot(left = (7, 8), right = (9, 10))
duration = 10
end_time = time() + duration
running = True

# To move the robot forward
robin.forward()
sleep(1)
robin.stop()