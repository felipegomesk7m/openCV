import cv2
import numpy as np
from matplotlib import pyplot as grafico

# Carregar Imagem BMP pois garante fidelidade das cores dos pixels, o valor 0 é para binário 
# (!!!Imagens em JPG resultam em pixels de cores intermediários)
imagem = cv2.imread("leaf.bmp", 0)
totalPixelsPreto = 0;
totalPixelsBranco = 0;

for x in range(0, 599):
    for y in range(0, 599):
        if imagem[x,y] == 255:
            totalPixelsBranco += 1;
        else:
            totalPixelsPreto += 1;

print(totalPixelsPreto)
print(totalPixelsBranco)

grafico.hist(imagem.ravel(), 256, [0,256])
grafico.show()