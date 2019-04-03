'''
Description:
	Prime Factorization - Have the user enter an integer (integer>1) and find all 
	Prime Factors (if there are any) and display them.

Executing the Main Program:
	python prime_factorization.py <number>

Executing the Test Program:
	python prime_factorization_test.py
'''

import sys

def prime_factor(number):
	prime_factors = []

	#Find the number of 2's divide into the number
	while number % 2 == 0:
		prime_factors.append(str(2))
		number = number//2

	#We are only left with odd numbers hence incrementing by 2
	old_number = number
	for divider in range(3, old_number+1, 2):
		while number % divider == 0:
			prime_factors.append(str(divider))
			number = number//divider

	return prime_factors


def main():
	number = int(sys.argv[1])
	assert number > 1
	prime_factors = ', '.join(prime_factor(number))
	print(prime_factors)

if __name__ == "__main__":
		main()