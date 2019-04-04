'''
Task:
	Read an integer N. Without using any string methods, try to print the following:
	123...N (Note that "..." represents the values in between)

Input Format:
	The first line contains an integer N

Output Format:
	Output the answer as explained in the task

Sample Input 0:
	3
Sample Output 0:
	123
'''

if __name__ == '__main__': #C hecks if this module is being run as the main program
    n = int(input()) # Recieve user input and conver it to an integer data type
    print(*range(1,n+1), sep = '') # Unpacking the generator 