def debug(self, *argv):
    if not isDebug:
        return 
    for arg in argv:
        print(arg, end=" ")
    print()