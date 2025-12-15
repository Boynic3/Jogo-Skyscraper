from colorama import Fore, Back, Style
import Intro
from time import sleep
import pygame

            # INTRO DESATIVADA PARA TESTES
#Intro.intro()

pygame.init()

            # funcoes auxiliares para musica
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

            #funcoes auxiliares para texto e falas

def narrar(texto):
    input(Style.BRIGHT+Fore.RED+ texto + Style.RESET_ALL)
def reflexao(texto):
    input(Back.WHITE + "\033[3m" + texto + Style.RESET_ALL)
def npc_fala(npc_nome,texto):
    input(Style.BRIGHT+Fore.LIGHTCYAN_EX + npc_nome + "- "+ texto + Style.RESET_ALL)
def sky_fala(texto):
    input(Style.BRIGHT+Fore.MAGENTA + "- "+ texto + Style.RESET_ALL)
def jogador_fala(jogador_nome,texto):
    input(jogador_nome + "- " + texto)
                    #   INICIO DO JOGO
#Use as constantes Fore, Back (fundo) e Style para mudar a aparência:
#Fore (Texto): BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Back (Fundo): BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Style (Estilo): DIM, NORMAL, BRIGHT, RESET_ALL. 

TRANSICAO_INICIAL = "=-=-=-=-=-=-=-=-=-=-\n"
print(TRANSICAO_INICIAL)
#Falas vermelhas são do narrador | Falas brancas são do jogador | Fala magenta é da SKY |
#Falas com fundo branco são reflexões do jogador | Fala em verde é de PERMITIDO ou qq coisa assim
sleep(1)
            #teste para musica ambiente
tocar_musica_fundo()


                      #inicio e nome do jogador                               
narrar("Você acorda em uma sala pequena e estranha, sem memória de como chegou aqui.")
narrar("Ao que tudo indica você está em um prédio.")
narrar("Do que se lembra?")

print(Style.RESET_ALL+"Seu nome: ")
jogador_nome = input("> ").strip()

reflexao(jogador_nome)
reflexao("Meu nome deve ser "+jogador_nome)
input("...")
#Caminho secreto:
caminho_secreto = False
jogador_nome_natela = jogador_nome.upper().replace(" ", "").strip()
if jogador_nome_natela.strip().upper() == "SKY":
    trocar_musica("assets/skyscraper_clean_loop.wav", volume=0.5)
    caminho_secreto = True
    narrar("Um arrepio percorre sua espinha ao pronunciar esse nome.")
    sky_fala("VOCÊ NÃO DEVERIA TER LEMBRADO DISSO...")
    input(""+
"┓┏┏┓┏┓┏┓  ┳┓┏┓┏┓  ┳┓┏┓┓┏┏┓┳┓┳┏┓  ┏┓┏┓┏┳┓┏┓┳┓  ┏┓┏┓┳┳┳\n"+
"┃┃┃┃┃ ┣   ┃┃┣┫┃┃  ┃┃┣ ┃┃┣ ┣┫┃┣┫  ┣ ┗┓ ┃ ┣┫┣┫  ┣┫┃┃┃┃┃\n"+
"┗┛┗┛┗┛┗┛  ┛┗┛┗┗┛  ┻┛┗┛┗┛┗┛┛┗┻┛┗  ┗┛┗┛ ┻ ┛┗┛┗  ┛┗┗┻┗┛┻\n")
    narrar("Algo dentro de você se agita, uma presença desconhecida.")
    input(""+
"┓┏┏┓┏┓┏┓  ┳┓┏┓┏┓  ┳┓┏┓┓┏┏┓┳┓┳┏┓  ┏┓┏┓┏┳┓┏┓┳┓  ┏┓┏┓┳┳┳\n"+
"┃┃┃┃┃ ┣   ┃┃┣┫┃┃  ┃┃┣ ┃┃┣ ┣┫┃┣┫  ┣ ┗┓ ┃ ┣┫┣┫  ┣┫┃┃┃┃┃\n"+
"┗┛┗┛┗┛┗┛  ┛┗┛┗┗┛  ┻┛┗┛┗┛┗┛┛┗┻┛┗  ┗┛┗┛ ┻ ┛┗┛┗  ┛┗┗┻┗┛┻\n")
    sky_fala("COMO VOCÊ SABE DISSO?")
def apresentacao():
    reflexao("Oxi, que lugar é esse?")
    narrar("Ao seu redor, você pode ver um espelho empoeirado e uma porta trancada."+Style.RESET_ALL)
    narrar("O que você faz?"+Style.RESET_ALL)

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
            narrar("O reflexo se move tarde demais."+Style.RESET_ALL)
            narrar("Uma sensação de instabilidade toma conta de você."+Style.RESET_ALL)
            reflexao("Quem é aquele no espelho? Que atraso é esse no reflexo?")
            jogador_fala(jogador_nome,"Quem é você?")
            input("...")
            jogador_fala(jogador_nome,"... wtf?")
        elif escolha1 == "2":
            print("")
            tested.add("2")
            narrar("A porta não abre."+Style.RESET_ALL)
            narrar("Mas sua mente se sente um pouco mais clara."+Style.RESET_ALL)
        elif escolha1 == "3":
            print("")
            tested.add("3")
            narrar("O silêncio pesa mais do que deveria."+Style.RESET_ALL)
        elif escolha1 == "4":
            if len(tested) >= 3:
                print("")
                narrar("Agora olhando bem"+Style.RESET_ALL)
                narrar("Você percebe que há uma janela e uma passagem rachada na parede da sala."+Style.RESET_ALL)
                narrar("Onde você quer verificar primeiro?"+Style.RESET_ALL)
                break
            else:
                print("")
                input(Style.BRIGHT+Fore.YELLOW+"Ainda há coisas para investigar aqui antes de prosseguir."+Style.RESET_ALL)
        else:
            print("")
            narrar("Escolha inválida. Tente novamente."+Style.RESET_ALL)

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
            narrar("Quando você se aproxima da fenda, percebe algo se movimentando ligeiramente do outro lado."+Style.RESET_ALL)
            narrar("Quase que simultaneamente, você escuta um tilintar de metal na direção da porta."+Style.RESET_ALL)
            narrar("E se retira após o susto."+Style.RESET_ALL)
            
        elif escolha2 == "2":
            print("")
            narrar("Quando você chega na janela, se inclina para olhar melhor."+Style.RESET_ALL)
            narrar("A única coisa que enxerga é outra sala."+Style.RESET_ALL)
            narrar("Na verdade é só o reflexo da sala em que está agora."+Style.RESET_ALL)
            narrar("Sem novas pistas..."+Style.RESET_ALL)
        elif escolha2 == "3" and "1" in tested:   #garante q so qnd tiver testado a 1 libera a opcao 3
            print("")
            narrar("A porta agora está destrancada."+Style.RESET_ALL)
            narrar("Você a abre lentamente e sai da sala."+Style.RESET_ALL)
            narrar("Um corredor mal iluminado te acompanha pela direita e pela esquerda."+Style.RESET_ALL)
            while True:
                print(Style.BRIGHT+"1 - Ir para a direita\n2 - Ir para a esquerda"+Style.RESET_ALL)
                direcao = input("> ").strip()
                if direcao == "1":
                    return "direita"
                elif direcao == "2":
                    return "esquerda"
                else:
                    print("")
                    narrar("Escolha inválida. Tente novamente."+Style.RESET_ALL)

        else:
            print("")
            narrar("Escolha inválida. Tente novamente."+Style.RESET_ALL)

def cena3(direcao):
    while True:
        if direcao == "direita":
            narrar("Você escolhe o corredor da direita."+Style.RESET_ALL)
            narrar("Após caminhar por alguns minutos, você chega a uma escada que desce para um andar inferior."+Style.RESET_ALL)
            narrar("Ao descer, você encontra uma sala iluminada por luzes fluorescentes, cheia de computadores antigos."+Style.RESET_ALL)
            narrar("No centro da sala, há uma figura encapuzada digitando freneticamente em um teclado."+Style.RESET_ALL)
            narrar("A figura se vira lentamente na sua direção, e você não consegue ver o corpo ou rosto dela..."+Style.RESET_ALL)
            jogador_fala(jogador_nome,"Quem é você?")
            npc_fala("???","...")#fala da figura
            jogador_fala(jogador_nome,"Você é o cara do espelho??")
            npc_fala("???","eU SoU O QUe SoBRoU")
            jogador_fala(jogador_nome,"Como assim? Sobrou de q-")
            npc_fala("???","sanidadE, UniverSO, Urd, cronoS, Karma, stYx")
            jogador_fala(jogador_nome,"Quê? Isso não é coisa de religião e tal?")
            narrar(Style.BRIGHT+Fore.RED+"Antes que você terminasse, sua visão escurece imediatamente e a figura simplesmente desapareceu."+Style.RESET_ALL)
            narrar(Style.BRIGHT+Fore.RED+"Como se tivesse sido sua imaginação."+Style.RESET_ALL)
            break
        elif direcao == "esquerda":
            narrar("Você escolhe o corredor da esquerda."+Style.RESET_ALL)
            break
        else:
            input(Style.BRIGHT+Fore.YELLOW+"Nenhuma direção escolhida."+Style.RESET_ALL)



if caminho_secreto:
    input("Em desenvolvimento...")
        # fluxo normal do jogo
else:
   apresentacao()
   cena1()
   direcao_escolhida = cena2() # DIREITA OU ESQUERDA
   cena3(direcao_escolhida)



#reseta as cores no final
print(Style.RESET_ALL)




