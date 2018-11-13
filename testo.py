from random import randint
import time,sys

def spam():
	
	start, x = time.time(),0
	while x < 10:
		print ('YOU\'VE BEEN GNOMED', end="  ",flush=True)
		sys.stdout.flush()
		time.sleep(0.01)
		x = time.time() - start