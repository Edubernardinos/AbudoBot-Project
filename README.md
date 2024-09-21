# ONLINE AUTO-GAME BOT WITH A.I AND COMPUTER VISION 
# BOT ONLINE UTILIZANDO I.A E VISÃO COMPUTACIONAL

BOT FOR GAME : RAGNAROK (2002) 

Methodology and Strategy:
The bot follows a decision-making logic based on fixed rules but also explores reinforcement learning techniques to improve the efficiency of certain decisions. Prioritization of teleportation over other actions is done by detecting enemy-free areas, ensuring the character's survival. The entire system is designed to work with pixelated images, requiring a robust image processing approach to handle visual variations in the game.

Libraries and Tools:

OpenCV: Used for image manipulation and analysis in the game, enabling the detection of enemies and items through edge detection, segmentation, and template matching techniques.

Pytesseract: Implemented to extract textual information from the screen, such as HP and Mana percentages, which are located in the upper right corner of the game's interface.

PyAutoGUI: This library is used to interact with the game by simulating clicks, keyboard shortcuts, and other input commands.

PIL (Pillow): Assists in image manipulation and preprocessing before applying computer vision algorithms.

Pygetwindow and pywinauto: Used to control and manipulate the game windows, as well as to monitor the application's state during the bot's execution.




Metodologia e Estratégia
O bot segue uma lógica de decisão baseada em regras fixas, mas também explora técnicas de aprendizado por reforço para melhorar a eficiência de certas decisões. A priorização de teleporte sobre outras ações é feita com base na detecção de áreas livres de inimigos, garantindo a sobrevivência do personagem. Todo o sistema é projetado para trabalhar com imagens pixeladas, exigindo uma abordagem robusta de processamento de imagens para lidar com as variações visuais no jogo.

Bibliotecas e Ferramentas:


OpenCV: Utilizada para manipulação e análise das imagens do jogo, permitindo a detecção de inimigos e itens no cenário através de técnicas de detecção de bordas, segmentação e matching de templates.

Pytesseract: Implementada para extrair informações textuais da tela, como as porcentagens de HP e Mana, que estão localizadas no canto superior direito da interface do jogo.

PyAutoGUI: Biblioteca utilizada para realizar a interação com o jogo, como simulação de cliques, teclas de atalho e outras entradas.

PIL (Pillow): Auxilia na manipulação de imagens e no pré-processamento antes da aplicação de algoritmos de visão computacional.

Pygetwindow e pywinauto: Usadas para controlar e manipular janelas do jogo, além de monitorar o estado da aplicação durante a execução do bot.
