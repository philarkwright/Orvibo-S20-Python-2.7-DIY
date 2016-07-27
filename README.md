# Orvibo S20 Python DIY

After recieving the Orvibo S20 I wanted to incorperate it within my home automation kit however at the time there was little documentation online which was light weight and simple to implement. 

This script will not work straight out the box and requires you to have a resonable understanding of Python and Hex.

# Understanding Hex

The Orvibo S20 can be controlled by simple UDP packets listening on port 10000.
To use this script you must generate your own Hex packets using the hex generator. 2 scripts files were created to give you an understanding of how the system works. This can be combined easily if desired.
It is recommended that you give your Orvibo S20 device a static IP Address.

# Usage

Before anything can be done you must Subscribe to the device by sending a subscribe packet.
This can be done by running the subscribe function in the lights.py file.
After a couple minutes you will need to re-subscribe.
Use the other functions to recieve, poweron, poweroff.

