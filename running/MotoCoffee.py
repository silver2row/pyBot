import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time
 
EnA = "P8_13"
EnB = "P8_19"
ln1 = "P8_14"
ln2 = "P8_15"
Bt  = "P8_8"
 
GPIO.setup(EnA, GPIO.OUT)
GPIO.setup(EnB, GPIO.OUT)
GPIO.setup(ln1, GPIO.OUT)
GPIO.setup(ln2, GPIO.OUT)
GPIO.setup(Bt, GPIO.IN)
PWM.start(EnA, 0, 100)
PWM.start(EnB, 0, 100)
PWM.set_duty_cycle(EnA, 0)
PWM.set_duty_cycle(EnB, 0)

print ("Initialize!")
 
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
    for x in range(0,100):
        PWM.set_duty_cycle(EnA, x)
        PWM.set_duty_cycle(EnB, x)
        time.sleep(0.05)
 
 
def testH():
    PWM.set_duty_cycle(EnA, 100)
    PWM.set_duty_cycle(EnB, 100)
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
