#! usr/bin/python

print("-------------------------------------------------------")
print("------------------POCETOK NA PROGRAMA------------------")
print("-------------------------------------------------------")

a=["apple", "banana", "republic"]
for each in a:
    print(each)
    
for i in range(len(a)):
    for j in range(i+1):
        print(a[i])
