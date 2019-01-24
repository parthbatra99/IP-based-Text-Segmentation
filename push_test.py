# Testing for the segment
import cv2
from push import segment

### Test the push directory ###
img = cv2.imread("c:/users/dell/desktop/sanskritocr/source/image_text.jpg")
ori = img
tt = segment(img)
tt.image_para_calc(img)
img = tt.bg_filter(img)
binary = tt.img2binary(img)
skew_fix = tt.skew_fix(binary)
result = tt.img2line(binary, ori)