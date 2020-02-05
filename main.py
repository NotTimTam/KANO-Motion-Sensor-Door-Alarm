"""A python project to alert you if you door is open using the KANO Motion Sensor Kit.
Install the motion sensor behind the door, as it reads how close the door is to it backwards..

THIS PROJECT REQUIRES THE KANO MOTION SENSOR KIT. IT WILL NOT WORK WITHOUT IT."""

root = "./"  # the root folder for imports

import serial, json  # importing stuff to interact with the motion sensor.
import time
import dooralert

s = serial.Serial('COM4')  # opening up serial port four, check what your serial port is in CMD using "mode."

print("Starting up!")  # prints this when the program starts...

#-#-# Defining Variables #-#-#
proximity = 0  # object proximity to sensor.
proximity_opp = 0  # to be used as a percentage of the proximity. (out of 100)
last_proximity_check = 0  # a simple checker to stop the console from being overloaded.
run = True

print("Reading data from:", str(s.port), "\n\n")  # this will be printed showing what port is being read
# from (line above) when

# the program has finished loading in the information.


def wait(countdown_time=10):
    countdown_time += 1
    for i in range(countdown_time):
        countdown_time -= 1
        time.sleep(1)  # set a trap for your friends.
        print("Alarm will be set in", countdown_time, "seconds!\n")


wait(0)  # SET ME UP!!!

while run:  # this code constantly checks the value of the sensor.
    data = json.loads(s.readline())  # reading in the proximity data from the sensor.
    proximity = (data["detail"]["proximity"])  # setting a variable to that data.
    proximity_opp = round((proximity / 255) * 100)  # turning that data into a percent. This is how open the door is.
    if proximity != last_proximity_check:  # printing out the proximity_opp value if the proximity value has changed.
        last_proximity_check = proximity
        # print("Door is", str(proximity_opp) + "% open...")  # A value for debugging to show how open the door is...
    if proximity_opp > 2:  # setting door_open to true if the proximity is greater than five (little bit 'o' leeway)
        print("Egad! It's open.")
        dooralert.door_open_protocol()
        run = False
    else:  # setting door_open to false otherwise...
        print("Nothing to report.")
        print(str(proximity_opp) + "%")
