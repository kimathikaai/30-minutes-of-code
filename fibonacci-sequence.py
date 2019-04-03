'''
Enter a number and have the program generate the Fibonacci sequence 
to that number or to the Nth number.
'''

def fibonacci(n):
	series = []
	presentNum = 1
	previousNum = 0
	nextNum = 1

	for num in range(n):
		# Append current value to the list to be returned
		series.append(str(presentNum))

		# Update positions
		previousNum = presentNum
		presentNum = nextNum
		nextNum = presentNum + previousNum

	return ', '.join(series)
	

def main():
	n = int(input('Enter an integer less than 30: '))
	assert n < 30
	print(fibonacci(n))

if __name__ == '__main__':
		main()



# 1+1+2+3+5+8+13