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
    features, hog_image = hog(gray, orientations=3, pixels_per_cell=(20, 20),
                              cells_per_block=(5, 5), visualize=True)
    
    # Melhorar a visualização da imagem HOG
    hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))

    return features, hog_image_rescaled, gray, image

def detectar_regioes(hog_image_rescaled):
    # Ajustar o limiar para binarização
    _, binary_image = cv2.threshold(hog_image_rescaled, 0.3, 1.0, cv2.THRESH_BINARY)
    binary_image = (binary_image * 255).astype(np.uint8)  # Convertendo para imagem de 8 bits

    # Encontrar contornos
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    return contours

def desenhar_caixas(imagem, contours, area_minima):
    # Desenhar caixas na imagem original apenas se a área for maior que a área mínima
     for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(imagem, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
     return imagem

# Exemplo de uso
try:
    features, hog_image, gray_image, original_image = extrair_hog('C:\\Users\\Edu\\Desktop\\Zeny_Project\\Hog\\Rag_sprites\\pasta_pos\\screen_1.png')
    print("Características HOG extraídas com sucesso.")
    
    # Detectar regiões e desenhar caixas limitadoras
    contours = detectar_regioes(hog_image)
    
    # Definir a área mínima para os contornos a serem desenhados
    area_minima = 15  # Ajuste conforme necessário

    imagem_com_caixas = desenhar_caixas(original_image, contours, area_minima)

    # Exibir as imagens usando matplotlib
    plt.figure(figsize=(15, 10))

    # Mostrar a imagem original
    plt.subplot(1, 3, 1)
    plt.title('Imagem Original')
    plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))

    # Mostrar a imagem HOG
    plt.subplot(1, 3, 2)
    plt.title('Imagem HOG')
    plt.imshow(hog_image, cmap='gray')

    # Mostrar a imagem com caixas
    plt.subplot(1, 3, 3)
    plt.title('Imagem com Caixas Delimitadoras')
    plt.imshow(cv2.cvtColor(imagem_com_caixas, cv2.COLOR_BGR2RGB))

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




