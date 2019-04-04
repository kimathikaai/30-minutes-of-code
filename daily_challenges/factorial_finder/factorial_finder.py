'''
Description:
    Find the factorial of a positive integer

Executing the Main Program:
    python <filename.py> <integer>
'''
import sys

def factorial(n):
    assert n >= 0
    if n == 0:
        return 1

    return n * factorial(n-1)

def main():
    n = int(sys.argv[1])
    print(f'Factorial: {factorial(n)}')

if __name__ == "__main__":
    main()