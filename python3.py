#Question:
#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.

lower = int(input("Enter the lower ranger: "))
upper = int(input("Enter the upper ranger: "))
n = int(input("Enter the divident: "))
for i in range(lower, upper + 1):
    if i % n == 0:
        print(i)
    elif i % n != 0:
        print("No numbers can be divisible") and exit
