import cv2 as cv
import matplotlib.pyplot as plt


imagem_path = "C:\\Users\\alex\\PycharmProjects\\python_visao_computacional\\imagens\\larva_alfinete\\imagem_3.jpg"
imagem = cv.imread(imagem_path)
azul, verde, vermelho = cv.split(imagem)



plt.hist(imagem.ravel(), 256, [0,256])
plt.figure()


plt.hist(azul.ravel(), 256, [0,256])
plt.figure()
plt.hist(verde.ravel(), 256, [0,256])
plt.figure()
plt.hist(vermelho.ravel(), 256, [0,256])
plt.figure()

plt.show()

print('FIM')