import cv2
import numpy as np

# Carregando Imagem
imagem = cv2.imread("frutas.jpg")
azul, verde, vermelho = cv2.split(imagem)

# Exibindo imagens dos canais separados
cv2.imshow("Canal Red", vermelho)
cv2.imshow("Canal Green", verde)
cv2.imshow("Canal Blue", azul)
cv2.waitKey(0)
cv2.destroyAllWindows() 

# Salvando imagens dos canais separados
cv2.imwrite("frutas-de-canal-vermelho.jpg", vermelho)
cv2.imwrite("frutas-de-canal-verde.jpg", verde)
cv2.imwrite("frutas-de-canal-azul.jpg", azul)
