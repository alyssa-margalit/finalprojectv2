import time
import sys
import grovepi
from grove_rgb_lcd import *
from grovepi import *
import math
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)

def scroll(the_text):
	str_pad = " "*16
	scroll_string = str_pad+the_text
	for i in range (0,len(scroll_string)):
		lcd_text = scroll_string[i:(i+15)]
		time.sleep(0.1)
		setText(lcd_text)
	setText(str_pad)


#scroll("how dare you disturb my slumber")


def trivia_question_callback(client,userdata,message):
	print(str(message.payload, "utf-8"))
	global question 
	question = str(message.payload, "utf-8")
	#scroll(str(message.payload, "utf-8"))


def trivia_answer_callback(client,userdata,message):
	print(str(message.payload, "utf-8"))
	global answer
	answer = str(message.payload, "utf-8")
	#print(answer)
	



def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
#subscribe tp all the different topics
    client.subscribe("alyssasrpi/trivia_question")
    client.message_callback_add("alyssasrpi/trivia_question", trivia_question_callback)
    client.subscribe("alyssasrpi/trivia_answer")
    client.message_callback_add("alyssasrpi/trivia_answer", trivia_answer_callback)
    global counter
    counter = 1
    print("connected")
    #global story
    #story = 5
    #client.subscribe("alyssasrpi/button")
    #client.message_callback_add("alyssasrpi/button", button_callback)


#Default message callback. Please use custom callbacks.
def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))


print("things")


if __name__ == '__main__':
    #this section is covered in publisher_and_subscriber_example.py
	client = mqtt.Client()
	client.on_message = on_message
	client.on_connect = on_connect
	client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
	#print("completed connection")
	client.loop_start()


	red_led = 8
	green_led = 7
	button = 4
	ranger = 3
	buzzer = 2
	potentiometer = 2

	#grovepi.pinMode(red_led, "OUTPUT")
	#grovepi.pinMode(green_led, "OUTPUT")
	#grovepi.pinMode(buzzer, "OUTPUT")
	grovepi.pinMode(button, "INPUT")
	story = 0
	pot = analogRead(potentiometer)
	oldPot1 = pot
	oldPot2 = pot
	newPot = pot
	averagePot = pot
	deltaPot = 0
	print("no")
	while True: 
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(17,GPIO.OUT)
		GPIO.output(17,1)
		GPIO.setup(27,GPIO.OUT)
		GPIO.output(27,1)
		GPIO.setup(22,GPIO.OUT)
		GPIO.output(22,1)
		GPIO.setup(10, GPIO.OUT)
		GPIO.output(10,1)
		#print(story)
		#begin the sequence
		print("hello")
		distance = ultrasonicRead(ranger)
		print(distance)
		distance = int(distance)
		#if story != 400:
		story = 0
		if story == 0:
			newPot = analogRead(potentiometer)
			averagePot = (oldPot1+oldPot2)/2
			deltaPot = newPot-averagePot
			print(deltaPot)
			time.sleep(1)
			oldPot1 = oldPot2
			oldPot2 = newPot
			if abs(deltaPot)>10:
				print("begin")
				story = 1
			#if int(pot) >500:
				#print("begin")
				#story= 1
			#if distance>10:
				#print("begin")
				#story = 1

		if story ==1:
			print("red")
			setRGB(255,0,0)
			setText("who dares disturb my slumber")
			time.sleep(5)
			while True:
				pot = grovepi.analogRead(potentiometer)
				#print(pot)
				pressed = digitalRead(button)
				if pressed:
					if 0<pot<250:
						response = "Wizard"
						break
					elif 250<pot<500:
						response = "Hero"
						break
					elif 500<pot<750:
						response = "Villain"
						break
					else:
						response = "Peasant"
						break
			print(response)
			client.publish("alyssasrpi/newAdventurer", response)
			scroll("have you come for my precious treasure?")
			#time.sleep(5)
			while True:
				pot = grovepi.analogRead(potentiometer)
				#print(pot)
				pressed = digitalRead(button)
				if pressed:
					if pot>500:
						response = "yes"
						break
					else:
						response = "no"
						break
			print(response)
			if response == "no":
				setRGB(0,255,0)
				scroll("then replace the key and go away")
				#time.sleep(5)
				story = 0
			if response =="yes":
				setRGB(0,0,255)
				
				scroll("then you must answer my trivia")
				time.sleep(5)

				client.publish("alyssasrpi/trivia_request", "ready")
				
				
				time.sleep(2)
				print(answer)
				count = 0
				#scroll(question)
				while True:
					pot = grovepi.analogRead(potentiometer)
					#print(pot)
					pressed = digitalRead(button)
					if count == 0:
						scroll(question)
						count = 1

					if pressed:
						if pot>500:
							response1 = "True"
							break
						else:
							response1 = "False"
							break
				print(response1)
				
				if response1 == str(answer):
					setRGB(0,255,0)
					#GPIO.output(4, 0)       # set port/pin value to 0/GPIO.LOW/False  
					setText("You are worthy!")
					scroll("Psych!! The treasure was the inside you all along, now go away!!")
					GPIO.output(17,0)
					GPIO.output(27,1)
					GPIO.output(22,0)
					GPIO.output(10,0)
					time.sleep(3)
					client.publish("alyssasrpi/showGraph","show")
					#scroll("Enter password 123 to unlock ")
					#time.sleep(3)
					#state = 0
					story = 400
				else: 
					scroll("Fail! I hereby curse you with eternal syntax errors!!!")
					#time.sleep(5)
					#dist = ultrasonicRead(ranger)
					#print(dist)
					#if dist <10:
						#scroll("better luck next time!")
						#time.sleep(5)
					#else:
						#scroll("I hereby curse you with eternal syntax errors!!!")
						#time.sleep(5)
						#story = 400
