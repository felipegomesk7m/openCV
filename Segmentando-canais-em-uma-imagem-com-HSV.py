import cv2

# Carregando Imagem e Convertendo para HSV
imagem = cv2.imread("frutas.jpg")
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
matiz, saturacao, valor = cv2.split(imagem)

# Exibindo Imagens em HSV
cv2.imshow("Canal com Matiz", matiz)
cv2.imshow("Canal com Saturação", saturacao)
cv2.imshow("Canal com Valor", valor)

cv2.waitKey(0)
cv2.destroyAllWindows()

