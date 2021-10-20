import cv2
import numpy as np

# Carregando Imagem
imagem = cv2.imread("frutas.jpg")
azul, verde, vermelho = cv2.split(imagem)

# Exibindo imagens dos canais separados
cv2.imshow("Canal Red", vermelho)
cv2.imshow("Canal Green", verde)
cv2.imshow("Canal Blue", azul)

# Salvando imagens dos canais separados
cv2.imwrite("frutas-de-canal-vermelho", vermelho)
cv2.imwrite("frutas-de-canal-verde", verde)
cv2.imwrite("frutas-de-canal-azul", azul)

cv2.waitKey(0)
cv2.destroyAllWindows() 
