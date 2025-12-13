from colorama import Fore, Back, Style
import Intro
from time import sleep
Intro.intro()

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
input(Style.BRIGHT+Fore.RED + "Você acorda em uma sala pequena e estranha, sem memória de como chegou aqui.")
input(Style.BRIGHT+Fore.RED + "Ao que tudo indica você está em um prédio.")
input(Style.BRIGHT+Fore.RED + "Do que se lembra?")

print(Style.RESET_ALL+"Seu nome: ")
jogador_nome = input("> ").strip()

input(Back.WHITE+ jogador_nome + Style.RESET_ALL)

input(Back.WHITE+"Meu nome deve ser "+jogador_nome+Style.RESET_ALL)
input("...")
input(Back.WHITE+"Oxi, que lugar é esse?"+Style.RESET_ALL)
input(Style.BRIGHT+Fore.RED+"Ao seu redor, você pode ver um espelho empoeirado e uma porta trancada."+Style.RESET_ALL)
input(Style.BRIGHT+Fore.RED+"O que você faz?"+Style.RESET_ALL)

def cena1():
    print(Style.BRIGHT+Fore.RED+"1 - Olhar o espelho\n2 - Examinar a porta\n3 - Ficar parado"+Style.RESET_ALL)
    escolha1 = input("> ").strip()

    if escolha1 == "1":
        input(Style.BRIGHT+Fore.RED+"O reflexo se move tarde demais."+Style.RESET_ALL)
        input(Style.BRIGHT+Fore.RED+"Uma sensação de instabilidade toma conta de você."+Style.RESET_ALL)
        input(Back.WHITE+"Quem é aquele no espelho? Que atraso é esse no reflexo?"+Style.RESET_ALL)
        input("Quem é você?")
        input("...")
        input("... wtf?")
        return cena1()
    elif escolha1 == "2":
        input(Style.BRIGHT+Fore.RED+"A porta não abre."+Style.RESET_ALL)
        input(Style.BRIGHT+Fore.RED+"Sua mente se sente um pouco mais clara."+Style.RESET_ALL)
        return cena1()
    elif escolha1 == "3":
        input(Style.BRIGHT+Fore.RED+"O silêncio pesa mais do que deveria."+Style.RESET_ALL)
        return cena1()
    else:
        input(Style.BRIGHT+Fore.RED+"Escolha inválida. Tente novamente."+Style.RESET_ALL)
        return cena1()      

cena1()




#Caminho secreto:
jogador_nome_natela = jogador_nome.upper().replace(" ", "").strip()
if jogador_nome_natela.strip().upper() == "SKY":
    input(Fore.RED + "Um arrepio percorre sua espinha ao pronunciar esse nome.")
    input(Fore.MAGENTA + "VOCÊ NÃO DEVERIA TER LEMBRADO DISSO...")
    input(Fore.RED + "Algo dentro de você se agita, uma presença desconhecida.")
    input(Fore.MAGENTA + "COMO VOCÊ SABE DISSO?")

#reseta as cores no final
print(Style.RESET_ALL)



