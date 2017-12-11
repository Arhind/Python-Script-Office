# Python script to write the name of folders in a text file

import os
path="/home/vidooly/Data_Processing/ml/vid/nsfw/src/data/brand_safety_vid_frames/list"  
dirList=os.listdir(path)
with open("Arhind3.txt", "w") as f:
    for filename in dirList:
        print (filename+'\n')
        f.write(filename+'\n') 
