import cv2

img = cv2.imread("imagenes/frutas.jpg")
b, g, r = cv2.split(img)

cv2.imwrite("canal_R.png", r)
cv2.imwrite("canal_G.png", g)
cv2.imwrite("canal_B.png", b)
cv2.imwrite("imagen_RGB.png", img)
