import numpy as np
import cv2 as cv


class Operations:
    def get_grayscale(image):
        return cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # noise removal
    def remove_noise(image):
        return cv.medianBlur(image, 5)

    # thresholding
    def thresholding(image):
        return cv.threshold(image, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]

    # dilation
    def dilate(image):
        # kernel = np.ones((5, 5), np.uint8)
        kernel = cv.getStructuringElement(cv.MORPH_RECT, (18, 18))
        return cv.dilate(image, kernel, iterations=1)

    # erosion
    def erode(image):
        kernel = np.ones((5, 5), np.uint8)
        return cv.erode(image, kernel, iterations=1)

    # opening - erosion followed by dilation
    def opening(image):
        kernel = np.ones((5, 5), np.uint8)
        return cv.morphologyEx(image, cv.MORPH_OPEN, kernel)

    # canny edge detection
    def canny(image):
        return cv.Canny(image, 100, 200)

    # skew correction
    def deskew(image):
        coords = np.column_stack(np.where(image > 0))
        angle = cv.minAreaRect(coords)[-1]
        if angle < -45:
            angle = -(90 + angle)
        else:
            angle = -angle

        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        M = cv.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv.warpAffine(image, M, (w, h), flags=cv.INTER_CUBIC, borderMode=cv.BORDER_REPLICATE)
        return rotated

    # template matching
    def match_template(image, template):
        return cv.matchTemplate(image, template, cv.TM_CCOEFF_NORMED)

    def image_resize(image, width=None, height=None, inter=cv.INTER_AREA):
        # initialize the dimensions of the image to be resized and
        # grab the image size
        dim = None
        (h, w) = image.shape[:2]

        # if both the width and height are None, then return the
        # original image
        if width is None and height is None:
            return image

        # check to see if the width is None
        if width is None:
            # calculate the ratio of the height and construct the
            # dimensions
            r = height / float(h)
            dim = (int(w * r), height)

        # otherwise, the height is None
        else:
            # calculate the ratio of the width and construct the
            # dimensions
            r = width / float(w)
            dim = (width, int(h * r))

        # resize the image
        resized = cv.resize(image, dim, interpolation=inter)

        # return the resized image
        return resized
