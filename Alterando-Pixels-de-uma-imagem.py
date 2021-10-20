import cv2

imagem = cv2.imread("frutas.jpg")
print(imagem[150, 150]) 
imagem[150,150] = [250,250,250]
print("Alteração das cores em RGB do posicionamento 150x150 da imagem: ", imagem[150,150])