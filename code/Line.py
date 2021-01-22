#LineSensor test

from gpiozero import LineSensor
from time import sleep
from signal import pause

def lineDetected():
    print('line detected')


def noLineDetected():
    print('no line detected')

sensor = LineSensor(14)

sensor.when_line = lineDetected
sensor.when_no_line = noLineDetected

pause()

sensor.close()
