import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time
 
EnA = "P8_13"
ln1 = "P8_14"
ln2 = "P8_15"
Bt  = "P9_36"
 
GPIO.setup(EnA, GPIO.OUT)
GPIO.setup(ln1, GPIO.OUT)
GPIO.setup(ln2, GPIO.OUT)
GPIO.setup(Bt, GPIO.IN)
PWM.start(EnA, 0, 100)
PWM.set_duty_cycle(EnA, 50)
 
GPIO.output(EnA, GPIO.LOW)
 
print ("Initialize!")
 
GPIO.output(EnA, GPIO.HIGH)
 
 
def b_callback(unused):
    time.sleep(0.1)
    if GPIO.input(Bt):
        #print "start"
        PWM.set_duty_cycle(EnA, 100) #100 only for testing
    else:
        #print "stop"
        PWM.set_duty_cycle(EnA, 0)
 
 
GPIO.add_event_detect(Bt, GPIO.BOTH, callback=b_callback, bouncetime=300)
 
def testPWM():
    GPIO.output(ln1, GPIO.HIGH)
    GPIO.output(ln2, GPIO.HIGH)
    PWM.start(EnA, 0, 100)
    for x in range(0, 100):
        PWM.set_duty_cycle(EnA, x)
        time.sleep(0.05)
 
 
def testH():
    while(1):
        GPIO.output(ln1, GPIO.HIGH)
        GPIO.output(ln2, GPIO.LOW)
        time.sleep(1)
 
        GPIO.output(ln1, GPIO.HIGH)
        GPIO.output(ln2, GPIO.HIGH)
        time.sleep(1)
 
        GPIO.output(ln1, GPIO.LOW)
        GPIO.output(ln2, GPIO.HIGH)
        time.sleep(1)
        print ("Reverse!")
        GPIO.output(ln1, GPIO.LOW)
        GPIO.output(ln2, GPIO.LOW)
        time.sleep(1)
 
testPWM()
testH()
