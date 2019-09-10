
print("================ 1 Dimention ================")
# original arr
arr = [6, 2, 5, 1, 9, 4, 3, 7] 
print(arr)

# sort by list's sort function
arr.sort()
print(arr)          # sorted 
#print(arr.sort())  # wrong!  

# sort by built-in sorted function (assign a new arr)
sortedarr = sorted(arr)
print(sortedarr)    # sorted 

# sort by built-in sorted function, reversed
sortedarr = sorted(arr, reverse=True)
print(sortedarr)    # sorted 

print("================ 2 Dimention ================")

brr = [[2,'E'],[3,'B'],[3,'A'],[2,'A'],[1,'D'],[7,'B'],[2,'C'],[1,'B'],[2,'B']]
 
print(sorted(brr))                              #sort by x[0] then by x[1]
print(sorted(brr, key=lambda x: x[1]))          #sort by x[1] only; x[0] remains the same (stability)
print(sorted(brr, key=lambda x: [x[1], x[0]]))  #sort by x[1] then by x[0]
print(sorted(brr, key=lambda x: [x[1], -x[0]])) #sort by x[1] then by x[0] decending