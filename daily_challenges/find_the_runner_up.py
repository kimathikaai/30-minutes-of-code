'''
Details:
    Given a score sheet you are required to find the runner-up score

Input:
    First line = number of scores
    Second line = list of n integers seperated by a space
    E.g
        5
        2 3 6 6 5

Constraints:
    2 <= n <= 10
    -100 <= score values <= 100

Output:
    Value of runner up

What I should think about:
    Duplicates -> set
'''

if __name__ == "__main__":
    # Recieve appropriate inputs
    n = int(input('Enter the score sheet size: '))
    scores = input('Enter the scores seperated by spaces: ')

    # Store the scores as a set to remove duplicates
    scores = set(map(int, scores.split()))
    # Convert scores to a list for sorting and indexing
    scores = list(scores)
    scores.sort(reverse=True)
    print(f'Runner Up: {scores[1]}')
