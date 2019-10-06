#!/usr/local/bin/python3

print("================= Dec, Hex, Bin =================")
mIntDec = 89
mIntHex = 0x59
mIntBin = 0b1011001

mStrDec = "56"
mStrHex = "0x38"
mStrBin = "0b111000"

print(">> convert int to int")
print(mIntDec, hex(mIntDec), bin(mIntDec))
print(mIntHex, "{0:x}".format(mIntHex) ,"{0:b}".format(mIntHex))

print()
print(">> convert str to int")
print(int(mStrDec)    + 10)
print(int(mStrHex,16) + 10)


print("================= Format =================")
mShortNumber = 56789
mLongNumber  = 12345678901234567890

print()
print(">> Align to right, total 9 digit, padding with space")
print('{:>9}'.format(mShortNumber))
print('{:9d}'.format(mShortNumber))      #not adapt to float

print()
print(">> Align to right, total 9 digit, padding with 0")
print('{:>09}'.format(mShortNumber))

print()
print(">> Align to left, total 12 digit, padding with '+'")
print('{:+<12}'.format(mShortNumber))

print()
print(">> Truncate 8 digit")
print('{:.8}'.format(str(mLongNumber)))  #use string

print()
print(">> Truncate 8 digit")
print(str(mLongNumber)[0:8])             #same effect

print()
print(">> multiple input")
mStr1 = "abc"
mStr2 = "ggg"
print('{}-{}'.format(mStr1, mStr2))

print("================= Format Example =================")

mlist =[350.25, 35.1356, 13.881157, 73.815, 124.3776, 21.8, -2.6, -1931.2]
print(mlist)

print()
print(">> Format 1: total 12 spaces")
for i in mlist:
    print('{:>12}'.format(i))

print()
print(">> Format 2: digits under decimal point fixed at 3 (round up or trailling 0)")
for i in mlist:
    print('{:.3f}'.format(i))

print()
print(">> Format 3: digits under decimal point fixed at 3, total digit is 12")
for i in mlist:
    print('{:12.3f}'.format(i))

