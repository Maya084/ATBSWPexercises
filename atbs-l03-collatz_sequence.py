import math


def collatz(brojpom):
    broj = int(brojpom)
    if (broj % 2 == 0):
        return broj // 2
    else:
        return broj * 3 + 1


print("Enter number:")
while True:
    try:
        a = input()
        print(collatz(a))
        if(int(collatz(a)) == 1):
            break
    except ValueError:
        print("You must enter an integer.")
