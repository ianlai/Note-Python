# (4) needs to be after (1) (2) (3)
# (2) doesn't need to be after (1) even (1) uses (2)
# Order of (1) (2) (3) can be arbitrary

def A(arg):     # define function A (1)
    return B()
def B():        # deifne function B (2)
    return 10000

var = 10        # define var        (3)
 
print(A(var))   # call function     (4)


