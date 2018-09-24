import numpy as np
import cv2


imagen = cv2.imread("puppets.png")
const = 0.3
height = np.size(imagen, 0)
width = np.size(imagen, 1)
porcentualx = int(height * 0.5)
porcentualy = int(width * 0.5)
difh = height - porcentualy
difw = width - porcentualx

print "height      ",height
print "width       ",width
print "porcentualx ",porcentualx
print "porcentualy ",porcentualy
print "diferenciah ",difh
print "diferenciaw ",difw

crop_img = imagen[porcentualx:porcentualy, difh:difw] # Crop from x, y, w, h -> 100, 200, 300, 400
# NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)
