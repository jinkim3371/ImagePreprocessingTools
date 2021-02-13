# Author: JaydenK

import cv2
import os
import numpy as np

if __name__ == "__main__":

    #init ImageCropper class
    outPath = "./Output/"
    path = "./Source/"

    #init_path
    fps = 0.1

    # iterate through the names of contents of the folder
    for i, video in enumerate(os.listdir(path)):
        input_path = os.path.join(path, video)
        command = 'cmd /c "'+'ffmpeg -i ' + path + str(video) + ' -vf fps=' + str(fps) + ' ' + outPath + str(video[:-4]) + '_%05d.png"'
        print("\n commnad :::::::::::::: ", command)
        os.system(command)
        print ("Complete: ", round(i/len(os.listdir(path))*100,2), " %", end="\r")
        if i == len(os.listdir(path))-1:
            print("Complete: 100.0 %")
    print("\n ----------------------------------------\n :::: ", len(os.listdir(path)), " Files converted to images.")
    print("fps : ", fps)
    print("output dir : ", outPath)
    print()
    print(" -- Process Completed --")

    pass
