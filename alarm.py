import winsound
import time

# This method takes in a positive integer as number of seconds, waits and then plays a sound
def alarm(n):
	time.sleep(n)
	winsound.PlaySound("testSound.wav", winsound.SND_FILENAME)	
	
	
## -- Start of alarm.py --
## -- Assuming input in seconds --

print("-- Start of alarm.py --")
print("-- Assuming input in seconds --")

# Getting input
n = int(input("Enter amount of seconds:" ))

# Calling alarm method
alarm(n)

print("Done.")
