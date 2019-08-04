m = 4
n = 6 

arr1 = [0 for i in range(m)]
print(arr1)   

arr2 = [i for i in range(m)]
print(arr2)

arr3 = [i for i in range(2, m)]
print(arr3)


brr1 = [[0 for j in range(n)] for i in range(m)]
print(brr1)

brr2 = [[j for j in range(n)] for i in range(m)]
print(brr2)

brr3 = [[0 for j in range(i)] for i in range(m)]
print(brr3)

brr4 = [[0 for j in range(i+1)] for i in range(m)]
print(brr4)

brr4_loop = []
for i in range(m):
    brr4_loop.append([])
    for j in range(i+1):
        brr4_loop[i].append(0) 
print(brr4_loop)