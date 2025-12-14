from colorama import Fore, Back, Style
import Intro
from time import sleep
import pygame

            # INTRO DESATIVADA PARA TESTES
#Intro.intro()

pygame.init()

def tocar_musica_fundo():
    try:
        # Carrega o arquivo de música
        pygame.mixer.music.load("assets/skyscraper_ambience.wav")
        
        # O argumento -1 diz para o pygame repetir infinitamente
        # O argumento 0.5 define o volume (opcional, vai de 0.0 a 1.0)
        pygame.mixer.music.set_volume(1.0) 
        pygame.mixer.music.play(-1) 
    except pygame.error as e:
        print(Fore.RED + f"Erro ao carregar música: {e}" + Style.RESET_ALL)

def trocar_musica(arquivo, volume=0.5):
    """
    Função para trocar a música de fundo suavemente.
    """
    try:
        # Se já tiver música tocando, faz um fadeout de 1 segundo (1000ms)
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(500)
            sleep(0.5) # Espera o fadeout terminar
            
        pygame.mixer.music.load(arquivo)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1) # -1 significa loop infinito
    except pygame.error as e:
        print(Fore.RED + f"[Erro de Áudio]: Não foi possível tocar {arquivo}. Detalhes: {e}" + Style.RESET_ALL)



                    #   INICIO DO JOGO
#Use as constantes Fore, Back (fundo) e Style para mudar a aparência:
#Fore (Texto): BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Back (Fundo): BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Style (Estilo): DIM, NORMAL, BRIGHT, RESET_ALL. 

TRANSICAO_INICIAL = "=-=-=-=-=-=-=-=-=-=-\n"
print(TRANSICAO_INICIAL)
#Falas vermelhas são do narrador | Falas brancas são do jogador | Fala magenta é da SKY |
#Falas com fundo branco são reflexões do jogador
sleep(1)
            #teste para musica ambiente
tocar_musica_fundo()


                                                     
input(Style.BRIGHT+Fore.RED + "Você acorda em uma sala pequena e estranha, sem memória de como chegou aqui.")
input(Style.BRIGHT+Fore.RED + "Ao que tudo indica você está em um prédio.")
input(Style.BRIGHT+Fore.RED + "Do que se lembra?")

print(Style.RESET_ALL+"Seu nome: ")
jogador_nome = input("> ").strip()

input(Back.WHITE+ jogador_nome + Style.RESET_ALL)

input(Back.WHITE+"Meu nome deve ser "+jogador_nome+Style.RESET_ALL)
input("...")
#Caminho secreto:
caminho_secreto = False
jogador_nome_natela = jogador_nome.upper().replace(" ", "").strip()
if jogador_nome_natela.strip().upper() == "SKY":
    trocar_musica("assets/skyscraper_clean_loop.wav", volume=0.5)
    caminho_secreto = True
    input(Fore.RED + "Um arrepio percorre sua espinha ao pronunciar esse nome.")
    input(Fore.MAGENTA + "VOCÊ NÃO DEVERIA TER LEMBRADO DISSO...")
    input(""+
"┓┏┏┓┏┓┏┓  ┳┓┏┓┏┓  ┳┓┏┓┓┏┏┓┳┓┳┏┓  ┏┓┏┓┏┳┓┏┓┳┓  ┏┓┏┓┳┳┳\n"+
"┃┃┃┃┃ ┣   ┃┃┣┫┃┃  ┃┃┣ ┃┃┣ ┣┫┃┣┫  ┣ ┗┓ ┃ ┣┫┣┫  ┣┫┃┃┃┃┃\n"+
"┗┛┗┛┗┛┗┛  ┛┗┛┗┗┛  ┻┛┗┛┗┛┗┛┛┗┻┛┗  ┗┛┗┛ ┻ ┛┗┛┗  ┛┗┗┻┗┛┻\n")
    input(Fore.RED + "Algo dentro de você se agita, uma presença desconhecida.")
    input(""+
"┓┏┏┓┏┓┏┓  ┳┓┏┓┏┓  ┳┓┏┓┓┏┏┓┳┓┳┏┓  ┏┓┏┓┏┳┓┏┓┳┓  ┏┓┏┓┳┳┳\n"+
"┃┃┃┃┃ ┣   ┃┃┣┫┃┃  ┃┃┣ ┃┃┣ ┣┫┃┣┫  ┣ ┗┓ ┃ ┣┫┣┫  ┣┫┃┃┃┃┃\n"+
"┗┛┗┛┗┛┗┛  ┛┗┛┗┗┛  ┻┛┗┛┗┛┗┛┛┗┻┛┗  ┗┛┗┛ ┻ ┛┗┛┗  ┛┗┗┻┗┛┻\n")
    input(Fore.MAGENTA + "COMO VOCÊ SABE DISSO?")
def apresentacao():
    input(Back.WHITE+"Oxi, que lugar é esse?"+Style.RESET_ALL)
    input(Style.BRIGHT+Fore.RED+"Ao seu redor, você pode ver um espelho empoeirado e uma porta trancada."+Style.RESET_ALL)
    input(Style.BRIGHT+Fore.RED+"O que você faz?"+Style.RESET_ALL)

def cena1():
    tested = set()
    while True:
        print("")
        print(Style.BRIGHT+"1 - Olhar o espelho\n2 - Examinar a porta\n3 - Ficar parado"+Style.RESET_ALL)
        if len(tested) >= 3:
            print(Style.BRIGHT+Fore.GREEN+"4 - Prosseguir"+Style.RESET_ALL)
        else:
            print(Style.DIM+"4 - Prosseguir"+Style.RESET_ALL)

        escolha1 = input("> ").strip()


        if escolha1 == "1":
            print("")
            tested.add("1")
            input(Style.BRIGHT+Fore.RED+"O reflexo se move tarde demais."+Style.RESET_ALL)
            input(Style.BRIGHT+Fore.RED+"Uma sensação de instabilidade toma conta de você."+Style.RESET_ALL)
            input(Back.WHITE+"Quem é aquele no espelho? Que atraso é esse no reflexo?"+Style.RESET_ALL)
            input("Quem é você?")
            input("...")
            input("... wtf?")
        elif escolha1 == "2":
            print("")
            tested.add("2")
            input(Style.BRIGHT+Fore.RED+"A porta não abre."+Style.RESET_ALL)
            input(Style.BRIGHT+Fore.RED+"Mas sua mente se sente um pouco mais clara."+Style.RESET_ALL)
        elif escolha1 == "3":
            print("")
            tested.add("3")
            input(Style.BRIGHT+Fore.RED+"O silêncio pesa mais do que deveria."+Style.RESET_ALL)
        elif escolha1 == "4":
            if len(tested) >= 3:
                print("")
                input(Style.BRIGHT+Fore.RED+"Agora olhando bem"+Style.RESET_ALL)
                input(Style.BRIGHT+Fore.RED+"Você percebe que há uma janela e uma passagem rachada na parede da sala."+Style.RESET_ALL)
                input(Style.BRIGHT+Fore.RED+"Onde você quer verificar primeiro?"+Style.RESET_ALL)
                break
            else:
                print("")
                input(Style.BRIGHT+Fore.YELLOW+"Ainda há coisas para investigar aqui antes de prosseguir."+Style.RESET_ALL)
        else:
            print("")
            input(Style.BRIGHT+Fore.RED+"Escolha inválida. Tente novamente."+Style.RESET_ALL)

def cena2():
    tested = set()
    while True:
        print("")
        
        if len(tested) >= 1:
            print(Style.BRIGHT+"1 - Espreitar a rachadura\n2 - Ver o que há atrás da janela\n3 - Verificar novamente a porta"+Style.RESET_ALL)
        else:
            print(Style.BRIGHT+"1 - Espreitar a rachadura\n2 - Ver o que há atrás da janela"+Style.RESET_ALL)

        escolha2 = input("> ").strip()

        if escolha2 == "1":
            print("")
            tested.add("1")   # Libera a porta trancada
            input(Style.BRIGHT+Fore.RED+"Quando você se aproxima da fenda, percebe algo se movimentando ligeiramente do outro lado."+Style.RESET_ALL)
            input(Style.BRIGHT+Fore.RED+"Quase que simultaneamente, você escuta um tilintar de metal na direção da porta."+Style.RESET_ALL)
            input(Style.BRIGHT+Fore.RED+"E se retira após o susto."+Style.RESET_ALL)
            
        elif escolha2 == "2":
            print("")
            input(Style.BRIGHT+Fore.RED+"Quando você chega na janela, se inclina para olhar melhor."+Style.RESET_ALL)
            input(Style.BRIGHT+Fore.RED+"A única coisa que enxerga é outra sala."+Style.RESET_ALL)
            input(Style.BRIGHT+Fore.RED+"Na verdade é só o reflexo da sala em que está agora."+Style.RESET_ALL)
            input(Style.BRIGHT+Fore.RED+"Sem novas pistas..."+Style.RESET_ALL)
        elif escolha2 == "3" and "1" in tested:   #garante q so qnd tiver testado a 1 libera a opcao 3
            print("")
            input(Style.BRIGHT+Fore.RED+"A porta agora está destrancada."+Style.RESET_ALL)
            input(Style.BRIGHT+Fore.RED+"Você a abre lentamente e sai da sala."+Style.RESET_ALL)
            input(Style.BRIGHT+Fore.RED+"Um corredor mal iluminado te acompanha pela direita e pela esquerda."+Style.RESET_ALL)
            print(Style.BRIGHT+"1 - Ir para a direita\n2 - Ir para a esquerda"+Style.RESET_ALL)
            break
        else:
            print("")
            input(Style.BRIGHT+Fore.RED+"Escolha inválida. Tente novamente."+Style.RESET_ALL)



if caminho_secreto:
    input("Em desenvolvimento...")
else:
    apresentacao()
    cena1()
    cena2()



#reseta as cores no final
print(Style.RESET_ALL)




