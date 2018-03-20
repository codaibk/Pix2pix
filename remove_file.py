import os
import sys

input = sys.argv[1]
filelimit = sys.argv[2]
# last file is img_00001560.jpg
path = os.getcwd()
j = 0
for filename in os.listdir(input):
    x = filename[4:-4]
    if(int(x) <= int(filelimit)):
        j+=1
        print("removing {} . . .".format(filename))
        os.remove("{}/{}/{}".format(path,input,filename))
print("removed {} files".format(j))
