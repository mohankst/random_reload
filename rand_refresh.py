from pynput.keyboard import Key, Controller
import time, random



keyboard = Controller()

#Pressing ctrl + f5 key 
def reload():
	keyboard.press(Key.ctrl.value)
	keyboard.press(Key.f5)
	keyboard.release(Key.f5)
	keyboard.release(Key.ctrl.value)

reload()


#Randomly press betwin 3 - 5 seconds
while True:
	time.sleep(random.randrange(180, 300))
	reload()