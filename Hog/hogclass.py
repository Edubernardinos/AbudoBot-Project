import cv2
import numpy as np
from skimage.feature import hog
from skimage import exposure
import os
import matplotlib.pyplot as plt

def extrair_hog(image_path):
    # Carregar a imagem e converter para escala de cinza
    image = cv2.imread(image_path)
    
    # Verificar se a imagem foi carregada corretamente
    if image is None:
        raise FileNotFoundError(f"Imagem não encontrada ou não pode ser carregada: {image_path}")
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Extrair características HOG
    features, hog_image = hog(gray, orientations=9, pixels_per_cell=(8, 8),
                              cells_per_block=(2, 2), visualize=True)
    
    # Melhorar a visualização da imagem HOG
    hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))

    return features, hog_image_rescaled

# Exemplo de uso
try:
    features, hog_image = extrair_hog('C:\\Users\\Edu\\Desktop\\Zeny_Project\\Hog\\Rag_sprites\\pasta_pos\\screen_1.png')
    print("Características HOG extraídas com sucesso.")
    
    # Exibir a imagem HOG usando matplotlib
    plt.figure(figsize=(10, 5))

    # Mostrar a imagem original em escala de cinza
    plt.subplot(1, 2, 1)
    plt.title('Imagem Original')
    plt.imshow(cv2.cvtColor(cv2.imread('C:\\Users\\Edu\\Desktop\\Zeny_Project\\Hog\\Rag_sprites\\pasta_pos\\screen_1.png'), cv2.COLOR_BGR2GRAY), cmap='gray')

    # Mostrar a imagem HOG
    plt.subplot(1, 2, 2)
    plt.title('Imagem HOG')
    plt.imshow(hog_image, cmap='gray')

    plt.show()

except FileNotFoundError as e:
    print(e)


def carregar_e_extrair_caracteristicas(pasta_pos, pasta_neg):
    data = []
    labels = []

    # Carregar e extrair características das imagens "cheias"
    for arquivo in os.listdir(pasta_pos):
        imagem = os.path.join(pasta_pos, arquivo)
        features, _ = extrair_hog(imagem)
        data.append(features)
        labels.append(1)  # 1 para "cheio"

    # Carregar e extrair características das imagens "vazias"
    for arquivo in os.listdir(pasta_neg):
        imagem = os.path.join(pasta_neg, arquivo)
        features, _ = extrair_hog(imagem)
        data.append(features)
        labels.append(0)  # 0 para "vazio"

    return np.array(data), np.array(labels)



