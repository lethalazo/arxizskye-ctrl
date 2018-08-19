
import RPi.GPIO as GPIO
import time
import sklearn as sk

GPIO.setmode(GPIO.BCM)

gpioList = [16, 17, 18, 19, 20 , 21, 22, 23]

for i in gpioList:
	GPIO.setup(i, GPIO.OUT)
	GPIO.output(i, GPIO.HIGH)

	sleepTimeShort = 0.13
	sleepTimeLong = 0.16

try:
	while True:
		for i in gpioList:
				print i
				GPIO.output(i, GPIO.LOW)
				if i >= 23:
					time.sleep(1);
                                        GPIO.output(16, GPIO.HIGH)
					time.sleep(0.13);
                                        GPIO.output(17, GPIO.HIGH)
					time.sleep(0.13);
					GPIO.output(18, GPIO.HIGH)
					time.sleep(0.13);
					GPIO.output(19, GPIO.HIGH)
					time.sleep(0.13);
					GPIO.output(20, GPIO.HIGH)
					time.sleep(0.13);
					GPIO.output(21, GPIO.HIGH)
					time.sleep(0.13);
					GPIO.output(22, GPIO.HIGH)
					time.sleep(0.13);
					GPIO.output(23, GPIO.HIGH)
					time.sleep(0.13);
				else:
					time.sleep(sleepTimeShort);


except KeyboardInterrupt:
	print " Quit"

GPIO.cleanup()
