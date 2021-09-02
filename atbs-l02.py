def spam(devideby):
    try:
        return 43/devideby
    except ZeroDivisionError:
        print("Greska! Nevaliden argument.")

print(spam(3))
print(spam(43))
print(spam(0))
print(spam(1))
