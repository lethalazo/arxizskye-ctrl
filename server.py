import RPi.GPIO as GPIO
import time
import sklearn as sk

from flask import Flask, render_template, request 
app = Flask(__name__) 
GPIO.setmode(GPIO.BCM) 
# Create a dictionary called pins to store the pin number, name, and pin state: 
pins = { 16 : {'name' : 'Switch 1', 'state' : GPIO.LOW},
		 17 : {'name' : 'Switch 2', 'state' : GPIO.LOW},
		 18 : {'name' : 'Switch 3', 'state' : GPIO.LOW},
		 19 : {'name' : 'Switch 4', 'state' : GPIO.LOW},
         20 : {'name' : 'Switch 5', 'state' : GPIO.LOW},
         21 : {'name' : 'Switch 6', 'state' : GPIO.LOW},
         22 : {'name' : 'Switch 7', 'state' : GPIO.LOW}, 
         23 : {'name' : 'Switch 8', 'state' : GPIO.LOW} } 
        
# Set each pin as an output and make it low: 
for pin in pins:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.HIGH)

@app.route("/")
def main():
	 # For each pin, read the pin state and store it in the pins dictionary0: 
        for pin in pins:
                pins[pin]['state'] = GPIO.input(pin)
        templateData = { 'pins' : pins }
		# Pass the template data into the template main.html and return it to the user
        return render_template('main.html', **templateData)
		# The function below is executed when someone requests a URL with the pin number and action in it: 

@app.route("/allswitch/<action>", methods=['POST', 'GET'])
def allswitch(action):
	if action == "off":
		for pin in pins:
			GPIO.output(pin, GPIO.HIGH)
			
	if action == "on":
		for pin in pins:
			GPIO.output(pin, GPIO.LOW)
		  
	if action == "toggle":
		for pin in pins: 
			   # Read the pin and set it to whatever it isn't (that is, toggle it):
			GPIO.output(pin, not GPIO.input(changePin)) 
			message = "Toggled " + deviceName + "." 
			  # For each pin, read the pin state and store it in the pins dictionary: 
	for pin in pins:
			pins[pin]['state'] = GPIO.input(pin)
			templateData = { 'pins' : pins }
			# Pass the template data into the template main.html and return it to the user
			return render_template('main.html', **templateData)


@app.route("/relay/<action>", methods=['POST', 'GET'])
def relay(action):
  gpioList = [16, 17, 18, 19, 20 , 21, 22, 23]
  if action == "on":
    for i in gpioList:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.HIGH)

    sleepTimeShort = 0.13
    sleepTimeLong = 0.16
    loop = "saveMe"

    try:
            while i <= 23:
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
					break
					return
				elif i == 23:
					break
				else:
					time.sleep(sleepTimeShort);
		if i == 23:
		  break

    except action == "off":
		loop = "notToday"
		return
		
  if action == "off":
        print " Quit"
        loop = "notToday"
  
  templateData = {'loop': loop} 
  return render_template('main.html', **templateData)

@app.route("/<changePin>/<action>", methods=['POST', 'GET']) 
def action(changePin, action): 
	  # Convert the pin from the URL into an integer: 
      changePin = int(changePin) 
	  # Get the device name for the pin being changed: 
      deviceName = pins[changePin]['name'] 
	  # If the action part of the URL is "on," execute the code indented below: 
      if action == "off":
		   # Set the pin high: 
          GPIO.output(changePin, GPIO.HIGH) 
		   # Save the status message to be passed into the template: 
          message = "Turned " + deviceName + " off." 
      if action == "on":
		  GPIO.output(changePin, GPIO.LOW) 
		  message = "Turned " + deviceName + " on." 
	  
      if action == "toggle": 
		   # Read the pin and set it to whatever it isn't (that is, toggle it): 
		  GPIO.output(changePin, not GPIO.input(changePin)) 
		  message = "Toggled " + deviceName + "." 
		  # For each pin, read the pin state and store it in the pins dictionary: 
      for pin in pins: 
           pins[pin]['state'] = GPIO.input(pin) 
		   # Along with the pin dictionary, put the message into the template data dictionary: 
           
      templateData = { 'message' : message, 'pins' : pins } 
     
      return render_template('main.html', **templateData)
		 
if __name__ == "__main__": 
 app.run(host='0.0.0.0', port=80, debug=True)
