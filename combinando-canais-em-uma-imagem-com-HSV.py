import cv2

# Carregando Imagem e Convertendo em HSV
imagem = cv2.imread("frutas.jpg")
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
matiz, saturacao, valor = cv2.split(imagem)

# Exibindo Imagens em HSV
cv2.imshow("Canal com Matiz", matiz)
cv2.imshow("Canal com Saturação", saturacao)
cv2.imshow("Canal com Valor", valor)

# Unindo imagens e Convertendo para RGB
imagem = cv2.merge((matiz, saturacao, valor))
imagem = cv2.cvtColor(imagem, cv2.COLOR_HSV2BGR)

# Exibindo Imagem após o merge
cv2.imshow("Imagem Final", imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()