#!/usr/local/bin/python3
from os import listdir
from os import walk
import re

path = 'algo'

def appendFiles(path, dirList, fileList):
    for (dirpath, dirnames, filenames) in walk(path):
        fileList.extend(filenames)
        dirList.extend(dirnames)
        break

fileList    = []
dirList     = []

appendFiles(path, dirList, fileList)
#print("File List:", fileList)
#print("Dir List :", dirList)

for d in dirList:
    appendFiles(path+"/"+d, [], fileList)

filtered = []
for f in fileList:
    found = re.search("_{1}\d+_{1}\w+\.py", f)
    if found:
        filtered.append(found.string)

filtered.sort()

print("=====================================")
for e in filtered:
    print(e)
print("=====================================")
print("Num of Python Practice: " + str(len(filtered)))
