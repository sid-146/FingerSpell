import cv2
import os
import time
import uuid

ImagePath = "E:/GHClones/FingerSpell/Code/Tensorflow/workspace/images/CollectedImages"

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
    os.mkdir("Code\Tensorflow\workspace\images\CollectedImages\\" + label)
    cam = cv2.VideoCapture(0)

    print("Collecting images for {}".format(label))

    time.sleep(3)
    for imgNum in range(NumberOfImages):
        ret, frame = cam.read()
        imageName = os.path.join(
            ImagePath, label, label + "." + "{}.jpg".format(str(uuid.uuid1()))
        )
        cv2.imwrite(imageName, frame)
        cv2.imshow("frame", frame)
        time.sleep(4)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cam.release()
