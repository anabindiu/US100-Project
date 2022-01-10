#Program 3
#Name: Ana Bindiu
#UCID: 30062098

import rp2
from machine import Pin, Timer
import time


# Define the us_100 program. It has one GPIO to bind to on the set instruction, which is an output pin.
@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def us_100():
    #start the loop 
    wrap_target()
    #start the pulse
    set(pins, 1)    
    #stop the pulse
    set(pins, 0)    
    #frequency = 60 ms
    nop()           [31]
    nop()           [31]
    nop()           [31]
    nop()           [31]
    
    nop()           [31]
    nop()           [31]
    nop()           [31]
    nop()           [31]
    
    nop()           [31]
    nop()           [31]
    nop()           [31]
    nop()           [31]
    
    nop()           [31]
    nop()           [31]
    nop()           [31]
    nop()           [31]
    
    nop()           [31]
    nop()           [31]
    nop()           [31]
    nop()           [31]
    
    nop()           [31]
    nop()           [31]
    nop()
    #ends the loop and redirects it to wrap_target
    wrap()

#duration of pulse for this example: 85 us -> 1/11764
# Instantiate a state machine with the us-100 program, at 11764Hz, with set bound to Pin(13) 
#freq = num of cycles/second
#freq = time between pulses -> set (pins, 1) to set(pins, 0)
sm = rp2.StateMachine(0, us_100, freq=11764, set_base=Pin(13))

# Run the state machine for 1 second
#turn on state machine
sm.active(1)
time.sleep(1)

#code taken from us-100-basic file from d2l provided in the assignment
echoPin = 12

#create pin for echo input
echo = Pin( echoPin, Pin.IN )

while True :
    # wait for echo to go high
    while echo.value() == 0 :
        pass
    echo_start = time.ticks_us()
    
    # wait for echo to go low
    while echo.value() == 1 :
        pass
    echo_low = time.ticks_us()
    
    # create difference between echoes
    timeOfEcho = time.ticks_diff( echo_low, echo_start )
    #calculate distance for the difference
    distance = 0.5 * timeOfEcho * 343.0 * 1e-6
    #print the distance
    print( "distance: {:10.2f}m".format( distance ) )