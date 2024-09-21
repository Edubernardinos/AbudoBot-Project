import pyautogui
import pytesseract
import time
import pygetwindow as gw
from pywinauto import Application
from PIL import Image, ImageDraw
import tkinter as tk
from tkinter import messagebox
import io
import keyboard 
import threading
import schedule # Usando a biblioteca keyboard para simular teclas

# Configurar o caminho do Tesseract OCR se necessário
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def show_popup(message, title):
    """
    Exibe uma janela pop-up com a mensagem e título especificados.
    """
    root = tk.Tk()
    root.withdraw()  # Ocultar a janela principal
    messagebox.showinfo(title, message)
    root.destroy()

def titulos_janelas_abertos():
    windows = gw.getWindowsWithTitle('')
    lista_tarefas = [window.title.strip() for window in windows if window.title.strip()]
    return lista_tarefas

def verifica_janelas_abertas(lista):
    target_title = 'Ragnarok'
    found = False
    for window_title in lista:
        if window_title == target_title:
            found = True
            break
    return found

def foca_janela(window_title):
    try:
        app = Application().connect(title=window_title)
        window = app.window(title=window_title)
        window.restore()
        window.maximize()
        window.set_focus()
        time.sleep(1)
    except Exception as e:
        show_popup(f'Erro ao tentar focar a janela: {e}', 'Erro')

def capturar_tela_em_memoria():
    """
    Captura a tela e retorna a imagem como um objeto PIL Image em memória.
    """
    imagem = pyautogui.screenshot()
    return imagem

def desenhar_retagulos(imagem):
    """
    Desenha retângulos nas áreas de HP e Mana e exibe a imagem com os retângulos.
    :param imagem: Imagem PIL da tela.
    """
    draw = ImageDraw.Draw(imagem)
    
    # Definir áreas de interesse onde HP e Mana são exibidos
    area_hp = (160, 70, 205, 84)  # (left, top, right, bottom) para HP
    area_mana = (170,85, 210, 100)  # (left, top, right, bottom) para Mana
    
    # Desenhar retângulos nas áreas de HP e Mana
    draw.rectangle(area_hp, outline="red", width=3)
    draw.rectangle(area_mana, outline="blue", width=3)

    # Exibir a imagem com os retângulos desenhados
    imagem.show()

def identificar_hp_e_mana(imagem):
    """
    Identifica e retorna as porcentagens de HP e Mana da tela.
    :param imagem: Imagem PIL da tela.
    :return: Tupla contendo HP e Mana.
    """
    area_hp = (160, 70, 205, 84)  # Área de HP
    area_mana = (170,85, 210, 100)  # Área de Mana

    imagem_hp = imagem.crop(area_hp)
    imagem_mana = imagem.crop(area_mana)

    texto_hp = extrair_texto_da_imagem(imagem_hp)
    texto_mana = extrair_texto_da_imagem(imagem_mana)

    try:
        hp = int(''.join(filter(str.isdigit, texto_hp)))
    except ValueError:
        hp = None

    try:
        mana = int(''.join(filter(str.isdigit, texto_mana)))
    except ValueError:
        mana = None

    
    return hp, mana

def centralizar_janela(window_title):
    try:
        app = Application().connect(title=window_title)
        window = app.window(title=window_title)
        
        # Restaurar a janela se estiver minimizada
        window.restore()

        # Obter tamanho da tela
        screen_width, screen_height = pyautogui.size()

        # Obter dimensões atuais da janela
        rect = window.rectangle()
        janela_largura = rect.width()
        janela_altura = rect.height()

        # Calcular coordenadas para centralizar a janela
        pos_x = (screen_width - janela_largura) // 2
        pos_y = (screen_height - janela_altura) // 2
        
        # Mover a janela para o centro da tela sem alterar o tamanho
        window.move_window(pos_x, pos_y)

    except Exception as e:
        print(f"Erro ao centralizar a janela: {e}")

def extrair_texto_da_imagem(imagem):
    """
    Extrai texto de uma imagem usando pytesseract.
    :param imagem: Imagem PIL para processamento.
    :return: Texto extraído da imagem.
    """
    texto = pytesseract.image_to_string(imagem, config='--psm 6')
    return texto



def inimigos_por_perto():

    #algoritmo
    

    resposta_algoritmo = 10

    if resposta_algoritmo> 1 and resposta_algoritmo<=10:
        return True
    
    else:
        return False
    




def clicar_mana():
    """
    Simula cliques nos ícones das habilidades no jogo Ragnarok.
    Usa mouseDown e mouseUp para garantir que o clique seja registrado.
    """
    print("Clicando na potion de mana")
    pyautogui.moveTo(230,36)  
    pyautogui.mouseDown()  
    pyautogui.mouseUp()  
    pyautogui.mouseDown()  
    pyautogui.mouseUp()   

def clicar_hp():
    #f2
    """
    Simula cliques nos ícones das habilidades no jogo Ragnarok.
    Usa mouseDown e mouseUp para garantir que o clique seja registrado.
    """
    print("Clicando na potion de mana")
    pyautogui.moveTo(260,33)  
    pyautogui.mouseDown()  
    pyautogui.mouseUp()  
    pyautogui.mouseDown()  
    pyautogui.mouseUp()   


def potar_hp_e_mana(hp, mana):
    """
    Verifica as porcentagens de HP e Mana e realiza as ações correspondentes.
    :param hp: Porcentagem de HP.
    :param mana: Porcentagem de Mana.
    """
    if hp is not None and hp < 50:
        print("HP está abaixo de 50%. Usando poção de HP.")
        clicar_hp()
          # Simula um clique duplo na tecla F4 para usar poção de HP

        
    if mana is not None and mana < 20:
        print("Mana está abaixo de 15%. Usando poção de Mana.")
        clicar_mana()  # Simula um clique duplo na tecla F5 para usar poção de Mana


def usar_ganância():
    #f2
    """
    Simula cliques nos ícones das habilidades no jogo Ragnarok.
    Usa mouseDown e mouseUp para garantir que o clique seja registrado.
    """
    print("Clicando ganância")
    pyautogui.moveTo(316,35)   
    pyautogui.mouseDown()  
    pyautogui.mouseUp()  
    pyautogui.mouseDown()  
    pyautogui.mouseUp()   
    pyautogui.mouseDown()  
    pyautogui.mouseUp()   
       

def usar_teleporte():
    #f2
    """
    Simula cliques nos ícones das habilidades no jogo Ragnarok.
    Usa mouseDown e mouseUp para garantir que o clique seja registrado.
    """
    print("Clicando teleporte")
    pyautogui.moveTo(348,29) 
    pyautogui.mouseDown()  
    pyautogui.mouseUp()  
    pyautogui.mouseDown()  
    pyautogui.mouseUp()
    time.sleep(0.2)   
    pyautogui.moveTo(1048,788) 
    pyautogui.mouseDown()  
    pyautogui.mouseUp()   
    pyautogui.mouseDown()  
    pyautogui.mouseUp()   

    

def potar_hp_e_mana(hp, mana):
    """
    Verifica as porcentagens de HP e Mana e realiza as ações correspondentes.
    Se o HP estiver abaixo de 25%, prioriza o teleporte.
    :param hp: Porcentagem de HP.
    :param mana: Porcentagem de Mana.
    """
    if hp is not None and hp <= 25:
        print("HP está abaixo de 25%. Usando teleporte como prioridade.")
        usar_teleporte()  # Prioriza o uso do teleporte
        time.sleep(1)  # Pausa breve após o teleporte
        clicar_hp()  # Usa poção de HP logo após o teleporte

        return True  # Indica que o teleporte foi utilizado e outras ações devem ser suspensas
    
    if mana is not None and mana <= 20:
        print("Mana está abaixo de 20%. Usando poção de Mana.")
        clicar_mana()  # Simula um clique duplo na tecla F5 para usar poção de Mana

def clicar_habilidade_dano():
  
    #if monstros nearby // parâmetro algoritmo de visão computaciona
        # Simula um clique duplo na tecla F3 para usar habilidade principal
        pyautogui.moveTo(293,33)  
        pyautogui.mouseDown()  
        pyautogui.mouseUp()  
        pyautogui.mouseDown()  
        pyautogui.mouseUp()  
        pyautogui.moveTo(961,551)  
        pyautogui.mouseDown() 
        pyautogui.mouseUp() 



        delay = 10 #POR DELAY DA SKILL   


def usar_item_periodico():
        

        
        
        pyautogui.moveTo(230, 100)
        pyautogui.mouseDown()  
        pyautogui.mouseUp()  
        pyautogui.mouseDown()  
        pyautogui.mouseUp()  
        time.sleep(0.2)
        pyautogui.moveTo(261, 106)
        pyautogui.mouseDown()  
        pyautogui.mouseUp()  
        pyautogui.mouseDown()  
        pyautogui.mouseUp()  


        
         # Exemplo de ação



        
def timer_usar_item(intervalo):
    """
    Função que executa a ação de usar um item a cada intervalo especificado.
    """
    while True:
        usar_item_periodico()
        




def main():
    lista_tarefas = titulos_janelas_abertos()
    if verifica_janelas_abertas(lista_tarefas):
        print("Continuando com o script...")
        show_popup('Janela do jogo "Ragnarok" encontrada. Continuando com o script.', 'Sucesso')
        foca_janela('Ragnarok')
        centralizar_janela('Ragnarok')
    else:
        show_popup('A janela do jogo "Ragnarok" não foi encontrada. O script não pode continuar.', 'Erro')
        return  # Se a janela não for encontrada, o script para por aqui

    schedule.every(2500).seconds.do(usar_item_periodico)

    while True:
        # Atalho para dar break no loop: Shift + K
        if keyboard.is_pressed('shift') and keyboard.is_pressed('k'):
            print("Script interrompido pelo usuário.")
            show_popup('Script interrompido.', 'Interrupção')
            break

        imagem = capturar_tela_em_memoria()
        hp, mana = identificar_hp_e_mana(imagem)
        teleporte_usado = potar_hp_e_mana(hp, mana)  # Verifica se o teleporte foi usado

        # Se o teleporte não foi necessário, continuar com as ações normais
        if not teleporte_usado:
            clicar_habilidade_dano()  # Usa habilidade de dano se não houver necessidade de teleporte
            time.sleep(2)
            usar_ganância()
            time.sleep(1)
            usar_teleporte()  # Usa teleporte normalmente se não for emergencial
            time.sleep(3)

        schedule.run_pending()  # Executa tarefas agendadas

        # Pausa de 0.1 segundos entre as iterações para não sobrecarregar
        time.sleep(0.1)

if __name__ == "__main__":
    main()




