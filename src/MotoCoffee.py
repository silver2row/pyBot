#!/usr/bin/ python3

from flask import Flask, render_template
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
from time import sleep

EnA = "P8_13"
I1A = "P8_9"
I2A = "P8_10"

EnB = "P8_19"
I1B = "P8_11"
I2B = "P8_12"

Bt  = "P8_8"

GPIO.setup(I1A, GPIO.OUT)
GPIO.setup(I2A, GPIO.OUT)
GPIO.setup(I1B, GPIO.OUT)
GPIO.setup(I2B, GPIO.OUT)

GPIO.setup(Bt, GPIO.IN)

PWM.start(EnA, 0, 100)
PWM.start(EnB, 0, 100)
PWM.set_duty_cycle(EnA, 0)
PWM.set_duty_cycle(EnB, 0)

print ("Initialize!")

app = Flask(__name__)
@app.route("/hello/")
@app.route("/hello/<state>")

def b_callback(unused):
    sleep(0.1)
    if GPIO.input(Bt):
        #print "start"
        PWM.set_duty_cycle(EnA, 100) #100 only for testing
        PWM.set_duty_cycle(EnB, 100)
    else:
        #print "stop"
        PWM.set_duty_cycle(EnA, 0)
        PWM.set_duty_cycle(EnB, 0)


GPIO.add_event_detect(Bt, GPIO.BOTH, callback=b_callback, bouncetime=300)

def testPWM(state=None):
    #Direction depends on wiring
    if state == "LEDS":
        GPIO.output(I1A, GPIO.HIGH)
        GPIO.output(I2A, GPIO.LOW)

        GPIO.output(I1B, GPIO.HIGH)
        GPIO.output(I2B, GPIO.LOW)

        for x in range(0, 100):
            PWM.set_duty_cycle(EnA, x)
            PWM.set_duty_cycle(EnB, x)
            sleep(0.05)


def testH(state=None):
    PWM.set_duty_cycle(EnA, 100)
    PWM.set_duty_cycle(EnB, 100)
    if state == "F":
        #Forward or Reverse?
        GPIO.output(I1A, GPIO.HIGH)
        GPIO.output(I2A, GPIO.LOW)
        GPIO.output(I1B, GPIO.HIGH)
        GPIO.output(I2B, GPIO.LOW)
        sleep(1)

    if state == "L":
        #Rotate One Way!
        GPIO.output(I1B, GPIO.LOW)
        GPIO.output(I2B, GPIO.LOW)
        sleep(1)

    if state == "R":
        #Invert(Forward or Reverse)?
        GPIO.output(I1A, GPIO.LOW)
        GPIO.output(I2A, GPIO.HIGH)
        GPIO.output(I1B, GPIO.LOW)
        GPIO.output(I2B, GPIO.HIGH)
        sleep(1)

    if state == "Rev":
        #Rotate the other way!
        GPIO.output(I1A, GPIO.LOW)
        GPIO.output(I2A, GPIO.LOW)
        sleep(1)

    template_data = {
        "title" : state,
    }
    return render_template("fortune.html", **template_data)

#testPWM()
#testH()

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
