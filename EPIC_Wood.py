from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

import time




def getWood(device):
	#scrypt: 
	print 'start single fight'
	device.touch(640, 360, 'MonkeyDevice.DOWN_AND_UP')
	time.sleep(5)
	print 'click fight'
	#start fight
	device.touch(1200, 600, 'MonkeyDevice.DOWN_AND_UP')
	time.sleep(11)
	print 'click auto fight button'
	#begin auto fight
	device.touch(1250, 700, 'MonkeyDevice.DOWN_AND_UP')
	#if is wood time = 30 else time = 20
	time.sleep(35)
	print 'click reward'
	#start get reward
	device.touch(640, 400, 'MonkeyDevice.DOWN_AND_UP')
	time.sleep(4)
	print 'click get reward'
	#start get reward
	device.touch(780, 700, 'MonkeyDevice.DOWN_AND_UP')
	time.sleep(14)
	return;

print 'waiting for device connect ...'
device = MonkeyRunner.waitForConnection()

while 1:
	getWood(device)
	continue

