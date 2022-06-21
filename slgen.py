import cv2
import numpy as np
import random


file1 = open(input(""), 'r')
lengths = [len(i) for i in file1.readlines()]
file1.close()
print(lengths)
lmax = max(lengths)
wo = cv2.imread('windowopen.png')
wc = cv2.imread('windowclosed.png')



img = np.zeros((1000, len(lengths)*60,3), dtype=np.uint8)
img[:] = ( 255, 185, 116)

windows = [wo,wc,wc,wc,wc]
startpoint = -20
for i in lengths:
    for iii in range(3):
        startpoint += 20
        numblocks = int( i / (lmax / 40))
        currypos = 0
        if numblocks > 2:
            for ii in range(numblocks):
                print(startpoint)
                img[ (1000-currypos) - 20 : (1000-currypos), startpoint : startpoint+20] = random.choice(windows)
                currypos += 20
                #img = cv2.rectangle(img, (startpoint, 800), (startpoint+20, 800-int( i / (lmax / 40))), (255,0,0), -1)


cv2.imwrite("output.png", img)
