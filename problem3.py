def first_last6(niza):
    n=len(niza)
    return niza[0]==6 or niza[n-1]==6

niza=[5,6,7,8,9,2]
print(niza)
if first_last6(niza):
    print("YASSS")
else:
    print("NOOO")
    
# whether or not the first or last element of the list is 6

def first_last(niza):
    return niza[0]==6 or niza[-1]==6

niza2=[6,6,7,8,9,2]
print(niza2)
if first_last(niza2):
    print("YASSS")
else:
    print("NOOO")
