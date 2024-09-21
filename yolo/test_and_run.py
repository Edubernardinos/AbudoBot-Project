from ultralytics import YOLO
import matplotlib.pyplot as plt
# Carregar o modelo treinado
import cv2
model = YOLO("C:\\Users\\Edu\\Desktop\\Zeny_Project\\yolo\\runs\\detect\\train6\\weights\\best.pt") 

results = model.predict("C:\\Users\\Edu\\Desktop\\Zeny_Project\\data\images\\test\\screenThor325.jpg")

 # Substitua pelo caminho da sua imagem

# O resultado é uma lista de objetos Result
result = results[0]

# Mostrar a imagem com caixas delimitadoras usando Matplotlib
plt.imshow(cv2.cvtColor(result.plot(), cv2.COLOR_BGR2RGB))
plt.axis('off')  # Não exibir os eixos
plt.show()

# Ou salvar a imagem com as previsões
result.save("path_to_save_results/")  # Su



