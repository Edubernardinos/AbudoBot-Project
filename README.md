# AbudoBot-Project
# ONLINE AUTO-GAME BOT WITH A.I AND COMPUTER VISION


Metodologia e Estratégia
O bot segue uma lógica de decisão baseada em regras fixas, mas também explora técnicas de aprendizado por reforço para melhorar a eficiência de certas decisões. A priorização de teleporte sobre outras ações é feita com base na detecção de áreas livres de inimigos, garantindo a sobrevivência do personagem. Todo o sistema é projetado para trabalhar com imagens pixeladas, exigindo uma abordagem robusta de processamento de imagens para lidar com as variações visuais no jogo.

Bibliotecas e Ferramentas:


OpenCV: Utilizada para manipulação e análise das imagens do jogo, permitindo a detecção de inimigos e itens no cenário através de técnicas de detecção de bordas, segmentação e matching de templates.

Pytesseract: Implementada para extrair informações textuais da tela, como as porcentagens de HP e Mana, que estão localizadas no canto superior direito da interface do jogo.

PyAutoGUI: Biblioteca utilizada para realizar a interação com o jogo, como simulação de cliques, teclas de atalho e outras entradas.

PIL (Pillow): Auxilia na manipulação de imagens e no pré-processamento antes da aplicação de algoritmos de visão computacional.

Pygetwindow e pywinauto: Usadas para controlar e manipular janelas do jogo, além de monitorar o estado da aplicação durante a execução do bot.
