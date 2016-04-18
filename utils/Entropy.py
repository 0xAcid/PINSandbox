#!/usr/bin/python2.7
import os
import math
def FileEntropy(FILE):
	Array = [0]*256
	FileSize = 0
	f = open(FILE, "rb")
	f.seek(0, os.SEEK_END)
	FileSize = f.tell()	
	f.seek(0, os.SEEK_SET)
	
	for i in range(0, FileSize):
		Array[ ord(f.read(1)) ] +=1
	
	for i in range(0,256):
		Array[i] = float(Array[i]) / float(FileSize)
	H = 0
	for i in range(0,256):
		if (Array[i] != 0):
			H -=  Array[i] * math.log(Array[i], 2)
	return H
	
	
if __name__ == '__main__':
	print("DEbug purpose")
	print(FileEntropy("/home/squall/Bureau/INFECTED.exe"))
