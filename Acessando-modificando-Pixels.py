import cv2
import numpy as np

imagem = cv2.imread("frutas.jpg")
valorPixel = imagem[150,150]
print("\nValor do Pixel em 150x150: ", valorPixel)
print("\nMostra um vetor com os valores em RGB")
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
valorPixel = imagem[150,150]
print("\nValor do Pixel em 150x150 em Cinza: ", valorPixel)
print("\nRepare que resulta num valor inteiro, pois é referente à intensidade da luz")
print("\nResultado da quantidade de linhas, colunas e canais: ", imagem.size)
print("\nEste valor resulta na multiplicação do tamanho dos pixels")