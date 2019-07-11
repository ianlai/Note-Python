#!/usr/local/bin/python3

print("================= List Comprehension =================")

print(">> single list comprehension")
mlist = [i for i in range(10)]
print(mlist)


print(">> double list comprehension")
mlist1 = [str(i)+"-"+str(j) for i in range(1,7) for j in range(2,4)]
print(mlist1)


print(">> double parallel list comprehension")
mlist2 = [str(i)+"-"+str(j) for i,j in zip(range(1,7), range(2,4))]
print(mlist2)


print(">> double parallel list comprehension application (adding vector)")
vector1=[1,2,3,4,5]
vector2=[3,5,7,9,11]
vector3 = [ i+j for i,j in zip(vector1, vector2)]
print(str(vector1) + " + " + str(vector2) + " = " + str(vector3))

print("================= Dictionary Comprehension =================")

print(">> dictionary comprehension")
dict1 = {i: i*i for i in range(1,11)}
print(dict1)
