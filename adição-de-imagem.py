import cv2
import numpy as np

imagemOriginal = cv2.imread("frutas.jpg", 0)
totalLinhas, totalColunas = imagemOriginal.shape

matriz = cv2.getRotationMatrix2D((totalLinhas / 2, totalColunas / 2), 90, 1)

imagemRotacionada = cv2.warpAffine(
    imagemOriginal,
    matriz,
    (totalColunas, totalLinhas)
)

imagemNova = cv2.add(imagemRotacionada, imagemOriginal)
cv2.imshow("Resultado", imagemNova)

cv2.waitKey(0)
cv2.destroyAllWindows
