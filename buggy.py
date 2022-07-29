# This program makes use of GPIO pins, if you plan to try running this on your own,
# you MUST ENSURE you understand how to use GPIO pins and which ones to use
# Follow this link for more information: https://pi4j.com/1.4/pins/rpi-3bp.html

from gpiozero import Robot, InputDevice, OutputDevice
from time import sleep, time

# (7, 8) and (9, 10) represent GPIO pins
robin = Robot(left = (7, 8), right = (9, 10))
duration = 10
end_time = time() + duration
running = True

# The below code sets up our trig and echo pins
# I picked GPIO pins 4 and 17, if you want to change them you can (know what you are doing)
trig = OutputDevice(4)
echo = InputDevice(17)

sleep(2)

# Sending and receiving ultrasounds
# -----------------------------------------
# The measurement of the time required for the ultrasound to propagate and be received
# i.e. how long it takes to transmit and receive one pulse
def get_pulse_time():
    pulse_start, pulse_end = 0
    
    # To prepare the UDS' internal clock, set the trig pin to high (trig.on()) for 10μs (microseconds)
    # By setting the trig pin low (trig.off()), the emitter produces a burst of ultrasound
    trig.on()
    sleep(0.00001) # 10 microseconds
    trig.off()

    # The pulse_start value should be replaced with the current time until the echo pin becomes active
    # Consequently, pulse_start represents the time when the echo pin is set high.
    while echo.is_active == False:
        pulse_start = time()

    # Until the echo pin is low, keep replacing the end time
    while echo.is_active == True:
        pulse_end = time()

    # Return the time it took the ultrasound pulse to be sent and received
    return pulse_end - pulse_start
