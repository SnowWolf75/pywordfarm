import cv2
import numpy as np
import pytesseract
from time import time
from operations import Operations as OP
from windowcapture import WindowCapture

def_config="--psm 12 --dpi 72"

######
# Blocked until I figure out why it's being resized weirdly
######
# loop_time = time()
# window = WindowCapture("scrcpy")
# while True:
#
#     img = window.get_screen()
#     # debug the loop rate
#     print('FPS {}'.format(1 / (time() - loop_time)))
#     loop_time = time()
#
#     cv2.imshow("Live", img)
#
#     if cv2.waitKey(25) == 32:
#         print("boop")
#         cv2.destroyAllWindows()
#         cv2.waitKey(1)
#         break

file = "/Users/charles.wheeler/mygit/pywordfarm/Samples/nuted.png"

root = cv2.imread(file)
#root = cv2.cv2Color(root, cv2.COLOR_BGR2GRAY)

cv2.imshow("root", root)
img = cv2.cvtColor(root, cv2.COLOR_BGR2GRAY)
ret, thresh2 = cv2.threshold(img, 250, 255, cv2.THRESH_BINARY_INV)
preview = OP.image_resize(image=thresh2, width=240)
#preview = OP.canny( image=preview)
#preview = OP.dilate(preview)
cv2.imshow("preview", preview)

#hImg,wImg,_ = img.shape
boxes = pytesseract.image_to_boxes(preview)
for b in boxes.splitlines():
    b = b.split(" ")
    print(b)
    x, y, w, h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(preview, (x,y), (w, h), (0, 0, 0), 1)

cv2.imshow("boxes", preview)

im2 = preview.copy()
cropped = im2[ 115:144, 75:101 ]
print(cropped)
text = pytesseract.image_to_string(cropped)
print("Cropped: -%s-" % text)

cv2.waitKey()
cv2.destroyAllWindows()

print("Exited")