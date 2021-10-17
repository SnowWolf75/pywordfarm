import re
import numpy as np
from PIL import ImageGrab
import pygetwindow
import cv2 as cv


class WindowCapture:

    def __init__(self, win_match):
        win_list = pygetwindow.getAllTitles()
        win_matches = []
        for win in win_list:
            if re.match(win_match, win):
                win_matches.append(win)

        if len(win_matches)>1:
            self.fatal("Too many windows named similarly.")
        elif len(win_matches)==0:
            self.fatal("Unable to find window in list.")
        else:
            print("Win_hook success")
            self.window_name = win_matches[0]

    def get_screen(self):
        try:
            x1, y1, x2, y2 = pygetwindow.getWindowGeometry(self.window_name)
        except TypeError:
            print("!" * 27)
            print("!! Unable to open stream !!")
            print("!" * 27)
            exit(1)
        #x2 = x1 + w
        #y2 = y1 + h
        bbox = [x1, y1, x2, y2]
        self.warning(bbox.__str__())
        height = int(abs(y2-y1))
        width = int(abs(x2-x1))

        img = np.array(ImageGrab.grab(bbox=[x1,y1,x2,y2]))
        img.shape = (height, width, 4)
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        return img

    def fatal(self, arg):
        l = len(arg) + 6
        print("!" * l)
        print("!! %s !!" % arg)
        print("!" * l)
        exit(1)

    def warning(self, arg):
        l = len(arg) + 6
        print("*" * l)
        print("** %s **" % arg)
        print("*" * l)
