import os
import cv2
import numpy as np
import pyautogui
import PIL.ImageGrab as ImageGrab
import imutils
import time
import psutil
from zipfile import ZipFile

box = (174,31,509,736) #Android screen coordinates

try:
	# Create a ZipFile Object and load sample.zip in it
	with ZipFile('scrcpy-win64.zip', 'r') as zipObj:
		# Extract all the contents of zip file in current directory
		zipObj.extractall()
		print('>> "scrcpy-win64" Extraction complete')
except Exception as e:
	pass

def checkIfProcessRunning(processName):
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def convert_time(seconds): 
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)

def tap_once(x,y):
	try:
		os.chdir(adb_dir)
		tap_coordinates = 'adb shell input tap '+str(x)+' '+str(y)
		os.system(tap_coordinates) #x,y
		os.chdir(orig_dir)
	except Exception as e:
		print(e)
		cv2.destroyAllWindows()
		input('>> adb failed, press Enter to continue')

#Excluding from running two mirrors of android screen
if checkIfProcessRunning('scrcpy-noconsole.exe'):
	print('>> Android screen already mirrored')
else:
	print('>> Mirroring android screen')
	os.system('start scrcpy-win64/scrcpy-noconsole.exe')

#initializing program
run_status = 1
st = time.time()

#Reading paths
orig_dir = os.getcwd()
adb_dir = os.path.join(os.getcwd(), "scrcpy-win64")

#getting started
input('>> Press Enter to continue')

while True:
	#Reading frames from screen
	screen = ImageGrab.grab(box)
	screen = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
	screen = imutils.resize(screen, height=600)

	#reading time elapsed
	et = time.time()
	elapsed_time = et-st
	elapsed_time = round(elapsed_time)

	#performing fps calculation, till first 30 seconds to get an idea
	try:
		if elapsed_time < 30:
			fps = run_status/elapsed_time
			fps = round(fps)
	except Exception as e:
		print(e)
		fps = 0

	#printing information
	elapsed_time = convert_time(elapsed_time)
	frame_info = 'FPS: '+str(fps)+' , Time: '+str(elapsed_time)
	cv2.putText(screen, "{}".format(frame_info), (5, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
	os.system('cls')
	print(frame_info)

	#Showing frames
	#cv2.imwrite('temp/game_screen'+str(run_status)+'.png',screen)
	cv2.imshow('Screen', screen)

	#tapping somewhere on screen
	if run_status == 5:
		x,y = (360,360) #coordinate according to your android phone screen
		tap_once(x,y)

	#Program End Handling Block
	run_status +=1
	key = cv2.waitKey(1)
	if key == ord("q"):
		cv2.destroyAllWindows()
		break
