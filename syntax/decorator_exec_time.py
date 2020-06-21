def measureExecTime(func):
    def wrap():
        import time
        print("----------------------------")
        print("Test running time for '{}'".format(func.__name__))
        t1 = time.time()
        func()
        t2 = time.time()
        elapsed = round(t2 - t1, 3)
        print("Execution time: ", elapsed)
        print("----------------------------")
    return wrap

@measureExecTime
def heavyLoop1():
    loopNumber = 1000000
    ans = 0
    for i in range(loopNumber):
        ans = (ans + i ** 2) % 1000009
    return ans

@measureExecTime
def heavyLoop2():
    loopNumber = 1000000
    ans = 0
    for i in range(loopNumber):
        ans = (ans + i ** 3) % 1000009
    return ans

heavyLoop1()
heavyLoop2()

