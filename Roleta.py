import random, sys, time, os
from PIL import Image

# Cores simples para o terminal
VERMELHO = '\033[31m'
VERDE = '\033[32m'
AMARELO = '\033[33m'
AZUL = '\033[34m'
RESET = '\033[0m'

play = ""
coins = 100
emotes = ["\U0001F352", "\U0001F34C", "\U0001F34E", "\U0001F347", "\U0001F351", "\U0001F353"]

def mostrar_perdedor():
    print(f"{VERMELHO}Fine looser \U0001F44E{RESET}")
    caminho = os.path.join("imagem", "perdeu.png") 
    try:
        imagem = Image.open(caminho)
        imagem.show()
    except:
        print("Arquivo de imagem não encontrado na pasta 'imagem'.")

while play == "":
    print(f"\n{AZUL}Saldo atual: {coins} moedas{RESET} \U0001FA99")
    play = input("Aperte Enter para jogar ou Q para sair: ").upper()
    
    if play == "Q":
        confirma = input(f"{AMARELO}Are you sure? (Q para sim): {RESET}").upper()
        if confirma == "Q":
            realmente = input(f"{AMARELO}Really? (Q para sim): {RESET}").upper()
            if realmente == "Q":
                mostrar_perdedor()
                break
            else:
                play = ""
                continue
        else:
            play = ""
            continue

    coins -= 2
    sorteios = random.randint(30, 50)
    
    for i in range(sorteios):
        indices = []
        for _ in range(3):
            sorteado = random.randint(0, 9)
            if sorteado > 5:
                sorteado = random.randint(1, 5)
            indices.append(sorteado)
        
        pos1 = emotes[indices[0]]
        pos2 = emotes[indices[1]]
        pos3 = emotes[indices[2]]
        
        sys.stdout.write(f"\r  {pos1} | {pos2} | {pos3}  ")
        sys.stdout.flush()
        time.sleep(0.05)
    
    print()

    if pos1 == pos2 == pos3:
        print(f"{VERDE}\U0001F31F JACKPOT! +50 moedas \U0001F31F{RESET}")
        coins += 50
    elif (pos1 == emotes[0] and pos2 == emotes[0]) or (pos1 == emotes[0] and pos3 == emotes[0]) or (pos2 == emotes[0] and pos3 == emotes[0]):
        print(f"{VERDE}\U0001F4B0 WON! (Duas Cerejas) +20 moedas{RESET}")
        coins += 20
    else:
        print(f"{VERMELHO}WHAT A SHAME! -2 moedas{RESET}")

    if coins <= 0:
        print(f"{VERMELHO}Game Over! Você faliu.{RESET}")
        break
    
    play = ""