import cv2
import numpy as np

# Carregando Imagem
imagem = cv2.imread("frutas.jpg")
azul, verde, vermelho = cv2.split(imagem)

imagem = cv2.merge((azul, verde, vermelho))
cv2.imshow("Imagem", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows
