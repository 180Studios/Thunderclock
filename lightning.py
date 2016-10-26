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
def flashCell(cellNum):
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

#specific cell functions
def flashCell1():
	flashCell(2)
def flashCell2():	
	flashCell(3)
def flashCell3():
	flashCell(4)
def flashCell4():
	flashCell(17)
def flashCell5():
	flashCell(27)


#main loop
length=random.randint(1,7)
for i in range(0,length):
	p1 = Process(target=flashCell1)
	p2 = Process(target=flashCell2)
	p3 = Process(target=flashCell3)
	p4 = Process(target=flashCell4)
	p5 = Process(target=flashCell5)
	cell_array = [p1,p2,p3,p4,p5]
	
	while len(cell_array) > 0:
		randindex = random.randint(0, len(cell_array) - 1)
		process = cell_array[randindex]
		if random.randint(0,1) > 0:
			process.start()
		cell_array.remove(process)
		time.sleep(random.uniform(0, 0.4))
	time.sleep(random.uniform(0.5,2))
