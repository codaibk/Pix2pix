import shutil
import os
source = os.listdir("sketch2clothes/train")
destination = "sketch2clothes/test"
path = os.getcwd()
i = 0
for files in source:
    if files.endswith(".jpg") and i < 3000:
        shutil.move("{}/sketch2clothes/train/{}".format(path,files),"{}/{}".format(path,destination))
        i = i + 1
