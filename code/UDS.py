# UDS test
from gpiozero import InputDevice, OutputDevice
from time import sleep, time

trig = OutputDevice(4)
echo = InputDevice(17)

sleep(2)

def get_pulse_time():
    pulse_start, pulse_end = 0, 0

    trig.on()
    sleep(0.00001)
    trig.off()

    while echo.is_active == False:
        pulse_start = time()
        #print(pulse_start)

    while echo.is_active == True:
        pulse_end = time()

    return pulse_end - pulse_start

def calculate_distance(duration):
    speed = 343
    distance = speed * duration / 2
    return distance

while True:
    print('running')
    duration = get_pulse_time()
    distance = calculate_distance(duration)

    sleep(0.06)
    print(distance)




