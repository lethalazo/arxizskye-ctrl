import RPi.GPIO as GPIO
import time
from flask import Flask, render_template, request
from functools import wraps
from flask import request, Response


def check_auth(username, password):
	#Checks if uname and pass are correct.
    return ()

def authenticate():
	#Authenticates and sends a response if wrong.
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
	#Decorator for all the routes.
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

app = Flask(__name__)

#Initialize the pins
GPIO.setmode(GPIO.BCM)

#Add pins to a dictionary with their respective states.
pins = { 16 : {'name' : 'Switch 1', 'state' : GPIO.LOW},
		 17 : {'name' : 'Switch 2', 'state' : GPIO.LOW},
		 18 : {'name' : 'Switch 3', 'state' : GPIO.LOW},
		 19 : {'name' : 'Switch 4', 'state' : GPIO.LOW},
		 20 : {'name' : 'Switch 5', 'state' : GPIO.LOW},
		 21 : {'name' : 'Switch 6', 'state' : GPIO.LOW},
		 22 : {'name' : 'Switch 7', 'state' : GPIO.LOW},
		 23 : {'name' : 'Switch 8', 'state' : GPIO.LOW} }

for pin in pins:
	#Set each gpio pin to output
	GPIO.setup(pin, GPIO.OUT)

@app.route("/")
#Added the authentication decorator
@requires_auth
def main():
		#Store each pin state to their respective original state
		for pin in pins:
			pins[pin]['state'] = GPIO.input(pin)
			templateData = { 'pins' : pins }
			return render_template('main.html', **templateData)

#Function to turn on/off all switches
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
			GPIO.output(pin, not GPIO.input(changePin))
			message = "Toggled " + deviceName + "."

	for pin in pins:
			pins[pin]['state'] = GPIO.input(pin)
			templateData = { 'pins' : pins }
			return render_template('main.html', **templateData)

#Function to turn on/off a the switch looper
@app.route("/relay/<action>", methods=['POST', 'GET'])
def relay(action):
	timeToSleep = 0.40
	#Loops through all the switches setting them on
	for pin in pins:
		GPIO.output(pin, GPIO.LOW)
		time.sleep(timeToSleep)
		timeToSleep = timeToSleep - 0.04
	time.sleep(0.10)
	#When reaches the last switch, loops through and turns off all the switches.
	for pin in pins:
		GPIO.output(pin, GPIO.HIGH)
		time.sleep(timeToSleep)
		timeToSleep = timeToSleep + 0.04
	#Updates template
	templateData = {"message": "Loop initialized."}
	return render_template('main.html', **templateData)

#Function to turn on/off a single switch
@app.route("/<changePin>/<action>", methods=['POST', 'GET'])
def action(changePin, action):
	changePin = int(changePin)
	deviceName = pins[changePin]['name']
	if action == "off":
		GPIO.output(changePin, GPIO.HIGH) 
		message = "Turned " + deviceName + " off."
	if action == "on":
		GPIO.output(changePin, GPIO.LOW) 
		message = "Turned " + deviceName + " on."
	#Toggles the switch
	if action == "toggle":
		GPIO.output(changePin, not GPIO.input(changePin))
		message = "Toggled " + deviceName + "."
	for pin in pins:
		 pins[pin]['state'] = GPIO.input(pin)

	templateData = { 'message' : message, 'pins' : pins } 
	return render_template('main.html', **templateData)

#Runs the app on localhost port 80
if __name__ == "__main__":
 app.run(host='0.0.0.0', port=80, debug=True)
