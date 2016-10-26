import RPi.GPIO as GPIO
import time
import random
from multiprocessing import Process

#setup
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False) 
GPIO.setup(2, GPIO.OUT) 
GPIO.setup(3, GPIO.OUT) 
GPIO.setup(4, GPIO.OUT) 
GPIO.setup(17, GPIO.OUT) 
GPIO.setup(27, GPIO.OUT)

#flash single cell
def flashCell( cellNum ):
	flashPeriod = random.uniform(0.05, 0.1)
	holdPeriod = random.uniform(0.1, 0.5)
	flashRepeat = random.randint(1,4)
	for i in range(0, flashRepeat):
		GPIO.output(cellNum, GPIO.HIGH)
		time.sleep(flashPeriod)
		GPIO.output(cellNum, GPIO.LOW)
		time.sleep(flashPeriod)
	GPIO.output(cellNum, GPIO.HIGH)
	time.sleep(holdPeriod)
	GPIO.output(cellNum, GPIO.LOW)
	


length=random.randint(1,5)
for i in range(0,length):
	p1 = Process(target = flashCell(2))
	p2 = Process(target = flashCell(3))
	p3 = Process(target = flashCell(4))
	p4 = Process(target = flashCell(17))
	p5 = Process(target = flashCell(27))
	cell_array = [p1,p2,p3,p4,p5]
	while len(cell_array) > 0:
		cell_array[0].start()
		cell_array.remove(cell_array[0])
