import os
import fnmatch

names = ["" for x in range(0)]

for path,dirs,files in os.walk('.'):
    for f in fnmatch.filter(files,'*.nii'):
        fullname = os.path.abspath(os.path.join(path,f))
        names.append(f)
        string = "med2image -i " + fullname  + " -d " + f + "/ -o input.png -s m -r"
        os.system(string)

import numpy as np
import shutil

from numpy import array as narray
strs = ["" for x in range(0)]

for path,dirs,files in os.walk('.'):
    for f in fnmatch.filter(files,'*.png'):
        fullname = os.path.abspath(os.path.join(path,f))
        if "x" in fullname: 
            strs.append(fullname)
            file = os.path.split(os.path.abspath(fullname))[1]
            directory = os.getcwd()
            name = fullname.split('/')[-3]
            print(name)
            if not os.path.exists(directory + "/" + "ImageProcessed"):
            	os.makedirs(directory + "/" + "ImageProcessed")
            #name = directory.split('/')[-3]
            shutil.move(fullname, directory + "/ImageProcessed/" + name + ".png")

import shutil

for x in os.listdir('.'):
    splits = x.split(".")
    if len(splits) > 1:
    	formt = splits[1]
    	if formt == "nii":
    		directory = os.getcwd()
    		file_path = directory + "/" + x
    		shutil.rmtree(file_path) 