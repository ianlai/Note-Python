#!/usr/local/bin/python3
from functools import reduce
print("================= List Comprehension =================")

mlist = [2, 4, 7, 9, 14, 3, 5, 1, 8, 35 ,24]


print(">> single list comprehension")
list1 = [i%5 for i in mlist]
print(list1)

print(">> map (change original list)")  #very similar to list comprehension
list2 = list(map(lambda x: x%5, mlist))
print(list2)

print(">> filter (get the items matching the condition) ")
list3 = list(filter(lambda x: x%5==0, mlist))
print(list3)

print(">> reduce (n1 & n2, and then & n3, and then & n4 ...) ")
list4 = reduce(lambda x,y: x+y, mlist)
print(list4)

