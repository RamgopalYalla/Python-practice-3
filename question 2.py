"""
Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
"""


# def factorial(num):


num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("Not possible to find factorial for this number")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial*i
    print(factorial)
