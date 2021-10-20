import cv2

#Carregando Imagem
imagem = cv2.imread("frutas.jpg")

# Convertendo Imagem em Escala de Cinza e Exibindo
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
cv2.imshow("Imagem", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()