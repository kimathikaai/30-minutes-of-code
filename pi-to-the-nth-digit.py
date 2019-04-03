'''

Enter a number and the program will generate pi up to that
many decimal places
'''

from math import pi

def print_pi(n):
	digits = n if n <= 20 else 20
	print(f'{pi:.{digits}f}')


n = int(input('Specify the number of decimal places: '))
print_pi(n)
