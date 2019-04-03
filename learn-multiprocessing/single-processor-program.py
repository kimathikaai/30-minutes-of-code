'''
Monte Carlo Method of estimating the value of Pi
Visual: https://academo.org/demos/estimating-pi-monte-carlo/

'''

from random import random

def find_pi(numberOfPoints):
	'''
	Function to estimate the value of Pi
	'''
	inside = 0

	for _ in range(numberOfPoints):
		x = random()
		y = random()
		if (x**2+y**2)**(0.5) <= 1: # if the point falls within the circle
			inside += 1

	pi = (4*inside)/numberOfPoints
	return pi

def main():
	numberOfPoints = int(input('Number of Points: '))
	pi = find_pi(numberOfPoints)
	print(pi)

if __name__ == "__main__":
	while True:
		main()
