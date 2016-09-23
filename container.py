#!/usr/bin/python3

#================= Dictionary ================= 
mydict={}
mydict['n1'] = 101  #add
mydict['n2'] = 202
mydict['n5'] = 505
mydict['n3'] = 303
mydict['n2'] = 299  #update
mydict['n7'] =  77  #add
#mydict[3] =  33  #add

print(mydict)
print(mydict.keys())    #arbitrary order 
print(mydict.values())
print(mydict.items())



print("--------- Min of value -----------")

#min of key, not min of value
print(min(mydict))

#min of value
print(min(mydict.values()))

#key of "min of value"
min_value = min(mydict.values())
min_key_list = [k for k,v in mydict.items() if v == min_value]
print(min_key_list)
