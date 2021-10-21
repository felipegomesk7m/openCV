import cv2
import numpy as np
from matplotlib import pyplot as grafico

imagemOriginal = cv2.imread("frutas.jpg", 0)
imagemEqualizada = cv2.equalizeHist(imagemOriginal)

cv2.imshow("Imagem Original", imagemOriginal)
cv2.imshow("Imagem Equalizada", imagemEqualizada)

grafico.hist(imagemOriginal.ravel(), 256, [0,256])

grafico.figure();
grafico.hist(imagemEqualizada.ravel(), 256, [0,256])

grafico.show()

cv2.waitKey(0)
cv2.destroyAllWindows