def printList(self, l):
    while l != None:
        print(l.val, "->", end =" ")
        l = l.next
    print()
    return 