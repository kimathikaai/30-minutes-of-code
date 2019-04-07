'''
You have a record of N students. Each record contains the student's name, and their 
percent marks in Maths, Physics and Chemistry. The marks can be floating values. 
The user enters some integer N followed by the names and marks for N students. 
You are required to save the record in a dictionary data type. The user then enters 
a student's name. Output the average percentage marks obtained by that student, 
correct to two decimal places.

INPUT FORMAT:
    The first line contains the integer N, the number of students. The next N
    lines contains the name and marks obtained by that student seperated by a space.
    The final line contains the name of a particula student previously listed
    EXAMPLE:
        3
        Tom 34 53 23 65
        Hannah 23 65 34 75
        Bob 98 97 96 94 94
        Hannah

CONSTRAINTS:
    2 <= N <= 10
    0 <= MARKS <= 100

OUTPUT:
    56.00

ASSUMPTIONS:
    Students don't have the same names
    query_name exists in the dictionary

'''

if __name__ == '__main__':
    n = int(input('Enter the number of students: '))
    book = {}
    for _ in range(n):
        name, *marks = input(f"Enter Student {_+1}'s marks seperated by spaces: ").split()
        marks = list(map(float, marks))
        average = '{:.2f}'.format( sum(marks)/len(marks), 2 )
        book[name] = average
    query_name = input("Who's average do you want to know?: ")
    print(book[query_name])