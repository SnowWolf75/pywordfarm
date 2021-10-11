import cv2
import pytesseract

sample_image = "Samples/Screenshot_20211010-203756.png"

img_orig = cv2.imread(sample_image)
img_small = img_orig.copy()
# img_small = cv2.resize(img_orig, dsize=(250, 574))
cv2.imshow("Small", img_small)

thresh1 = cv2.cvtColor(img_small, cv2.COLOR_BGR2GRAY)
ret, thresh2 = cv2.threshold(thresh1, 250, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold", thresh2)

img_boxes = thresh2.copy()
img_boxes = cv2.cvtColor(img_boxes, cv2.IMREAD_COLOR)
boxes = pytesseract.image_to_data(img_boxes)
# print(boxes)
box_lines = boxes.splitlines()
print(box_lines[0])
for b in box_lines[1:]:
    b = b.split()
    if len(b) == 12:
        print(b)
        x, y, w, h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
        cv2.rectangle(img_boxes, (x,y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(img_boxes, b[11], (x+w,y+h), cv2.FONT_HERSHEY_PLAIN, 1.5, (0,128,0), 3)

cv2.imshow("boxes", img_boxes)
cv2.imwrite("boxes.png", img_boxes)

cv2.waitKey()
cv2.destroyAllWindows()

print("Exited")