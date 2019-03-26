'''
Task:
	Read an integer N For all non-negative integers i < N, print i^2. 

Input Format:
	The first and only line contains the integer, .

CONSTRAINTS:
	1 <= N <= 20

Output Format:
	Print N lines, one corresponding to each i.

Sample Input 0:
	5

Sample Output:
	0
	1
	4
	9
	16

'''

if __name__ == '__main__':
    n = int(input())
    print(*[num**2 for num in range(0,n)], sep='\n')