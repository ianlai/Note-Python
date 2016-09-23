#!/usr/bin/python3

#================= Output ================= 

print("\n----- 1. Print out diffent types.")

mint = 999
mstr = "Hello "
print(mstr + str(mint))

print("\n----- 2. Print out without new line.")
print(mstr)
print(mstr, end="")
print(mstr)

#================= String ================= 
mstr = "abcdefg"

print("\n----- 3. String")

print(mstr)                                  # string
print("First char: " + str(mstr[0]))         # first component
print("Last char:  " + mstr[len(mstr)-1])    # last component (length)
print("Last char:  " + mstr[-1])             # last component (negative index)

print("\n----- 4. String slicing")
print("Slicing:    " + mstr[1:3])            # index=1 (included) to index=3-1 (excluded)
print("Slicing:    " + mstr[:4])             # index=0 to index=3
print("Slicing:    " + mstr[4:])             # index=4 to last
print("Slicing:    " + mstr[:2] + mstr[2:])  # whole string

#================= List ================= 

print("\n----- 5. List")
#(1) List can contains different types
#(2) Add, delete, insert element 
#(3) Access element 

mlist = []
mlist.append(10)
mlist.append(20)
mlist.append("third")
mlist.append(True)
mlist.append("last")

print(mlist)                                       # whole list
print("First component: " + str(mlist[0]))         # first component
print("Last component:  " + mlist[len(mlist)-1])   # last component (length)
print("Last component:  " + mlist[-1])             # last component (negative index)
print("Slicing:  "        + str(mlist[1:3]))       # list supports slicing too (return a list)

#================= List Expression ================= 

#================= Flow Control ================= 
#================= Class ================= 

