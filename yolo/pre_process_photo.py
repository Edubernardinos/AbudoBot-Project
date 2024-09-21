import os 

file = 'C:\\Users\\Edu\\Desktop\\Zeny_Project\\data\images\\train'


fotos = os.listdir(file)

imagens = [imagem for imagem in fotos]

for i, imagem in enumerate(imagens):
    novo_nome = f'print_train{i}.jpg'
    file_antigo = os.path.join(file,imagem)
    file_novo = os.path.join(file,novo_nome)
    os.rename(file_antigo,file_novo)







file_test= 'C:\\Users\\Edu\\Desktop\\Zeny_Project\\data\images\\test'


fotos = os.listdir(file_test)

imagens = [imagem for imagem in fotos]

for i, imagem in enumerate(imagens):
    novo_nome = f'print_teste{i}.jpg'
    file_antigo = os.path.join(file_test,imagem)
    file_novo = os.path.join(file_test,novo_nome)
    os.rename(file_antigo,file_novo)