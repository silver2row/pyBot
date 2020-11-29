import Adafruit_BBIO.GPIO as GPIO
import time

EnA = "P8_13"
EnB = "P8_16"
ln1 = "P8_14"
ln2 = "P8_15"
ln3 = "P8_17"
ln4 = "P8_18"
Bt  = "P8_8"

GPIO.setup(EnA, GPIO.OUT)
GPIO.setup(ln1, GPIO.OUT)
GPIO.setup(ln2, GPIO.OUT)
GPIO.setup(Bt, GPIO.IN)

GPIO.output(EnA, GPIO.LOW)
GPIO.output(EnB, GPIO.LOW)

print ("Initialize!")

GPIO.output(EnA, GPIO.HIGH)
GPIO.output(EnB, GPIO.HIGH)


def call(unused):
    time.sleep(0.1)
    print ("Button pressed")
    if GPIO.input(Bt):
        #print "start"
        GPIO.output(EnA, GPIO.HIGH)
        GPIO.output(EnB, GPIO.HIGH)
    else:
        #print "stop"
        GPIO.output(EnA, GPIO.LOW)
        GPIO.output(EnB, GPIO.LOW)

GPIO.event_detected(Bt)

def testP():
    GPIO.output(ln1, GPIO.HIGH)
    GPIO.output(ln2, GPIO.LOW)
    GPIO.output(ln3, GPIO.HIGH)
    GPIO.output(ln4, GPIO.LOW)
    for x in range(0, 8):
        GPIO.output(EnA, GPIO.HIGH)
        GPIO.output(EnB, GPIO.HIGH)
        time.sleep(15)


def testH():
    while(1):
        GPIO.output(ln1, GPIO.HIGH)
        GPIO.output(ln2, GPIO.LOW)
        GPIO.output(ln3, GPIO.HIGH)
        GPIO.output(ln4, GPIO.LOW)
        time.sleep(10)

        GPIO.output(ln1, GPIO.HIGH)
        GPIO.output(ln2, GPIO.HIGH)
        GPIO.output(ln3, GPIO.HIGH)
        GPIO.output(ln4, GPIO.HIGH)
        time.sleep(10)

        GPIO.output(ln1, GPIO.LOW)
        GPIO.output(ln2, GPIO.HIGH)
        GPIO.output(ln3, GPIO.LOW)
        GPIO.output(ln4, GPIO.HIGH)
        time.sleep(10)
        print ("Reverse!")

        GPIO.output(ln1, GPIO.LOW)
        GPIO.output(ln2, GPIO.LOW)
        GPIO.output(ln3, GPIO.LOW)
        GPIO.output(ln4, GPIO.LOW)
        time.sleep(10)
call(0)
testP()
testH()
