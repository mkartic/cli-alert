#!/usr/bin/python

# Just a timer for now. Will expand to include a proper alarm later on.
# AppleScript docs: http://developer.apple.com/library/mac/#documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html

from datetime import datetime, timedelta
import time
import os

def accept_int(q): 
    raw_a = raw_input(q)
    acc = False

    while not acc: 
        try: 
            a = int(raw_a)
            acc = True

        except (ValueError, NameError): 
            print "That is not a valid input. Please enter an integer."
            raw_a = raw_input(q)

    return a

def create_timer():
    hours = accept_int("Hours: ")
    minutes = accept_int("Minutes: ")
    seconds = accept_int("Seconds: ")

    event_name = raw_input("Event name: ")

    alert = """
        osascript -e 'tell application "Finder" to display dialog "%s" buttons "OK" default button 1 with title "PyAlert"'
            """ %(event_name, )

    target_time = datetime.now() + timedelta(hours=hours, minutes=minutes, seconds=seconds)

    print "Timer to go off at: " + datetime.strftime(target_time, "%I:%M%p")

    seconds_to_target = (target_time - datetime.now()).total_seconds()
    time.sleep(seconds_to_target)

    button_return = os.system(alert) # returns 0 for OK button

if __name__=="__main__":
    create_timer()
