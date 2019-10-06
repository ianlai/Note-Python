#!/usr/local/bin/python3

#================= Output ================= 

print("\n----- 1. Print out diffent types.")

mint = 999
mstr = "Hello "
print(mstr + str(mint)) #need to convert to string
print(mstr, mint)       #not need to convert to string 

print("\n----- 2. Print out without new line.")
print(mstr)
print(mstr, end="")
print(mstr)

#================= String ================= 
mstr = "abcdefg"

print("\n----- 3. String")

print(mstr)                                  # string
print("First char: " + mstr[0])         # first component
print("Last char:  " + mstr[len(mstr)-1])    # last component (length)
print("Last char:  " + mstr[-1])             # last component (negative index)

print("\n----- 4. Check substring")
if "de" in mstr:
    print ("de is in " + mstr)
if "eee" in mstr:
    print ("eee is in " + mstr)
else:
    print ("eee is NOT in " + mstr)

print("\n----- 5. String slicing")
print("Slicing:    " + mstr[1:3])            # index=1 (included) to index=3-1 (excluded)
print("Slicing:    " + mstr[:4])             # index=0 to index=3
print("Slicing:    " + mstr[4:])             # index=4 to last
print("Slicing:    " + mstr[:2] + mstr[2:])  # whole string

mint = 35
mhex = hex(mint)
print(mint, mhex, mhex[2:])  #remove the "0x"

#================= List ================= 

print("\n----- 6. List")
#(1) List can contains different types
#(2) Add, delete, insert element 
#(3) Access element 

print()
print(">> CLRU")

mlist = [5,6,6,6,7,8,9,"a","b","c"]
mlist.append(10)
mlist.append(20)
mlist.append(5)
mlist.append("third")
mlist.append(True)
mlist.append("last")

print(mlist)                               # whole list
print("[0]:      :" + str(mlist[0]))         # first 
print("[-1] last :" + mlist[len(mlist)-1])   # last (length)
print("[-1] last :" + mlist[-1])             # last (negative index)
print("[1:3]     :" + str(mlist[1:3]))       # list slicing returns a list

mlist.insert(3,"kkk")   #add at index 3
mlist.pop()             #remove the last

newlist = ['n','e','w']
mlist.extend(newlist)   #append a list to another list
print(mlist)

print()
print(">> Check list contains the item or not")
print(mlist)                                       # whole list
if 9 in mlist:
    print("9 at " + str(mlist.index(9)))
if 3 not in mlist:
    print("3 not in mlist")

print()
print(">> List comprehension")
list1 = [i for i in mlist if isinstance(i,int)]
print("Int only:\n" + str(list1))  #filtered only int (True is equally to 1 so it is included)

list1.remove(6)  #delete the first 6 only
print("Delete only the first 6: \n" + str(list1))

list1 = [i for i in list1 if i != 5 and i!= 6]
print("Delete all 5 and 6: \n" + str(list1))

list1 = [i+3 for i in list1]
print("All elements +3 :\n" + str(list1))


