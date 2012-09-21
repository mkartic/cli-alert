#!/usr/bin/python

# Just a timer for now. Will expand to include a proper alarm later on.
# AppleScript docs: http://developer.apple.com/library/mac/#documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html

from datetime import datetime, timedelta
import time
import os

def create_timer():
    hours = int(raw_input("Hours: "))
    minutes = int(raw_input("Minutes: "))
    seconds = int(raw_input("Seconds: "))
    event_name = raw_input("Event name: ")

    alert = """
        osascript -e 'tell application "Finder" to display dialog "%s" buttons "OK" default button 1 with title "PyAlert"'
            """ %(event_name, )

    target_time = datetime.now() + timedelta(hours=hours, minutes=minutes, seconds=seconds)

    seconds_to_target = (target_time - datetime.now()).total_seconds()
    time.sleep(seconds_to_target)

    button_return = os.system(alert) # returns 0 for OK button

if __name__=="__main__":
    create_timer()
