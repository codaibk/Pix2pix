import os
import sys

input = sys.argv[1]
addstring = sys.argv[2]
# 000022323.jpg -> 00002232_A
path = os.getcwd()
j = 0
for filename in os.listdir(input):
    new_filename = "{}{}.jpg".format(filename[:-4],addstring)
    j+=1
    os.rename("{}/{}/{}".format(path,input,filename), "{}/{}/{}".format(path,input,new_filename))
    print("rename {} id {} to {}".format(filename,j,new_filename))
