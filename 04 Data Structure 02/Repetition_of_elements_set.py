# Assignment 2
l = [i for i in input("Enter elements separated by comma ").split(',')]
s = set(l)
print(s)
d = {i:0 for i in s}
for i in l:
    d[i] += 1    # here d[i] is used to finding value at the i th key and then we are increamenting the value by 1

print(d)

#----------------------------------------------------------------

l = [i for i in input("Enter elements separated by comma ").split(',')]
s = set(l)
d = {i: l.count(i) for i in s}
print(d)

