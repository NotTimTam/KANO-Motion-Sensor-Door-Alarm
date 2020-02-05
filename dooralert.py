""" Child of door-alarm.py, go there for more information... """

import datetime  # giving date and time information to the user.

import time

import playsound

dt = datetime.datetime.now()  # setting up the date and time values from datetime.

def door_open_protocol():  # the code run when the door is seen as open in door-alarm
    file = open("alert_hst.txt", "a")
    file.write("\nALERT: The door was opened on " + str(dt.strftime("%Y-%m-%d")) + " at " + str(dt.strftime("%H:%M")))
    file.close()
    print("\n\nAlright door protocol, leg'go...\n\n")  # notify the user that this is running
    if dt.hour <= 12:  # all below code is to write out the alert to let the user know, as well as to
        # add it to the file with the history of door openings.
        print("ALERT: The door was opened on " + dt.strftime("%Y-%m-%d"), "at " + dt.strftime("%H:%M"))
    else:
        print("ALERT: The door was opened on " + dt.strftime("%Y-%m-%d"), "at " + str(dt.hour - 12) + ":" +
              str(dt.minute))
    print("\nAdded above alert to", file.name + ", which can be found in the main folder")
    playsound.run_sound_alarm()
    file.close()
