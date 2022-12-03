import math
print()
print("===============================================")
print("| Hello, Welcome to Fibonacci Number Checker! |")
print("|       Created By Yasharth Bajpai            |")
print("|      Of Lovely Professional University      |")
print("|     Section: K22FG  Roll No.: RK22FGA36     |")
print("===============================================")
print()
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x

def isFibonacci(n):
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

while True:
    x=int(input("Press 1 to Check and 2 to exit: "))
    print()
    if x==1:
        n=int(input("How many numbers do you want to input? "))
        print()
        for i in range(n):
            i=int(input("Enter the number: "))
            if (isFibonacci(i) == True):
                print(i,"is a valid Fibonacci Number \n")
            else:
                print(i,"is not a valid Fibonacci Number \n")
    elif x==2:
        print("Thank You for using Fibonacci Number Checker")
        print()
        break

    else:
        print("Invalid Input Try Again \n")
        continue
