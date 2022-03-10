import cv2
import os
import time
import uuid

ImagePath = "Code\Tensorflow\workspace\images\CollectedImages\\"

labels = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]

NumberOfImages = 20  # 15 for training 5 for testing

## ! Images Collection code

for label in labels:
    os.mkdir
    {"Code\Tensorflow\workspace\images\CollectedImages\\" + label}
    cam = cv2.VideoCapture(0)

    print("Collecting images for {}".format(label))
    time.sleep(5)

    for imgNum in range(NumberOfImages):
        ret, frame = cam.read()
