lower = int(input("Enter the lower ranger: "))
upper = int(input("Enter the upper ranger: "))
n = int(input("Enter the divident: "))
for i in range(lower, upper + 1):
    if i % n == 0:
        print(i)
    elif i % n != 0:
        print("No numbers can be divisible") and exit
