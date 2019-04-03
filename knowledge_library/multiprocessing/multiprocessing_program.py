'''
Monte Carlo Method of estimating the value of Pi
Visual: https://academo.org/demos/estimating-pi-monte-carlo/

'''

from random import random
from multiprocessing import Pool
import timeit
import sys

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
	N = int(sys.argv[1]) 	# total_iterations
	P = int(sys.argv[2])	# number_of_processes

	'''
	p = Pool(P)
	# Make 10 executions of the lambda
	# The lambda function prints out the average value of pi from the different processes
	# [1000//5]*5 = [200,200,200,200,200]
	print(timeit.timeit(lambda: print(f'{sum(p.map(find_pi, [N//P]*P))/P:.7f}'), number=10))
	p.close()
	p.join()
	print(f'{N} total iterations with {P} processes')
	'''

	# Using a 'Context Manager' to shrink the code above
	with Pool(P) as p:
		print(timeit.timeit(lambda: print(f'{sum(p.map(find_pi, [N//P]*P))/P:0.7f}'), number=10))
	print(f'{N} total iterations with {P} processes')
	
if __name__ == "__main__":
	main()