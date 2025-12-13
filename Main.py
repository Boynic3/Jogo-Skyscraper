import pygame
import sys

# --- Configurações Iniciais ---
pygame.init()

# Resolução solicitada
LARGURA, ALTURA = 1000, 650
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Text Adventure - Converter")

# Fontes
FONTE_TAMANHO = 28
# Usa uma fonte monoespaçada padrão do sistema
FONTE = pygame.font.SysFont("Consolas", FONTE_TAMANHO) 

# Cores (R, G, B) baseadas no Colorama
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 50, 50)
MAGENTA = (255, 0, 255)
CINZA_ESCURO = (20, 20, 20)

# Estados do Jogo
ESTADO_INTRO = 0
ESTADO_NOME = 1
ESTADO_REFLEXAO = 2
ESTADO_ESCOLHA = 3
ESTADO_FIM = 4

# --- Classe para Gerenciar o Texto ---
class LinhaTexto:
    def __init__(self, texto, cor_texto, cor_fundo=None):
        self.texto = texto
        self.cor_texto = cor_texto
        self.cor_fundo = cor_fundo

class Jogo:
    def __init__(self):
        self.historico = [] # Lista de objetos LinhaTexto
        self.estado = ESTADO_INTRO
        self.input_atual = ""
        self.jogador_nome = ""
        
        # Variável para controlar o fluxo da intro e reflexão (passo a passo)
        self.passo_narrativa = 0
        
        # Iniciar primeira mensagem
        self.adicionar_texto("=-=-=-=-=-=-=-=-=-=-", BRANCO)
        self.adicionar_texto("Você acorda em uma sala pequena e estranha...", VERMELHO)
        self.adicionar_texto("Pressione ENTER para continuar...", (100, 100, 100))

    def adicionar_texto(self, texto, cor_texto, cor_fundo=None):
        # Quebra de linha simples para não sair da tela
        palavras = texto.split(' ')
        linha_atual = ""
        
        for palavra in palavras:
            test_line = linha_atual + palavra + " "
            # Se a linha ficar muito larga, salva e começa outra
            if FONTE.size(test_line)[0] > LARGURA - 40:
                self.historico.append(LinhaTexto(linha_atual, cor_texto, cor_fundo))
                linha_atual = palavra + " "
            else:
                linha_atual = test_line
        
        if linha_atual:
            self.historico.append(LinhaTexto(linha_atual, cor_texto, cor_fundo))

    def processar_input(self, evento):
        if evento.key == pygame.K_RETURN:
            if self.estado == ESTADO_INTRO:
                self.avancar_intro()
            elif self.estado == ESTADO_NOME:
                self.finalizar_nome()
            elif self.estado == ESTADO_REFLEXAO:
                self.avancar_reflexao()
            elif self.estado == ESTADO_ESCOLHA:
                self.finalizar_escolha()
        
        elif evento.key == pygame.K_BACKSPACE:
            self.input_atual = self.input_atual[:-1]
        
        else:
            # Captura digitação para Nome e Escolha
            if self.estado in [ESTADO_NOME, ESTADO_ESCOLHA]:
                # Limita caracteres para não bugar
                if len(self.input_atual) < 20: 
                    self.input_atual += evento.unicode

    def avancar_intro(self):
        self.passo_narrativa += 1
        if self.passo_narrativa == 1:
            self.adicionar_texto("Do que se lembra?", VERMELHO)
        elif self.passo_narrativa == 2:
            self.adicionar_texto("Seu nome: ", BRANCO)
            self.estado = ESTADO_NOME
            self.input_atual = ""

    def finalizar_nome(self):
        nome = self.input_atual.strip()
        if not nome: return # Não aceita vazio
        
        self.jogador_nome = nome
        self.historico.append(LinhaTexto(f"> {self.jogador_nome}", BRANCO)) # Mostra o que digitou
        
        # Adiciona a primeira reflexão
        self.adicionar_texto(self.jogador_nome, PRETO, BRANCO)
        self.input_atual = ""
        self.passo_narrativa = 0 # Reseta contador para nova fase
        self.estado = ESTADO_REFLEXAO

    def avancar_reflexao(self):
        self.passo_narrativa += 1
        if self.passo_narrativa == 1:
            self.adicionar_texto("Meu nome deve ser " + self.jogador_nome, PRETO, BRANCO)
        elif self.passo_narrativa == 2:
            self.adicionar_texto("...", BRANCO)
        elif self.passo_narrativa == 3:
            self.adicionar_texto("Oxi, que lugar é esse?", PRETO, BRANCO)
        elif self.passo_narrativa == 4:
            self.adicionar_texto("Ao seu redor, você vê um espelho e uma porta trancada.", VERMELHO)
            self.adicionar_texto("O que você faz?", VERMELHO)
            self.adicionar_texto("1 - Olhar espelho | 2 - Examinar porta | 3 - Ficar parado", VERMELHO)
            self.estado = ESTADO_ESCOLHA

    def finalizar_escolha(self):
        escolha = self.input_atual.strip()
        self.historico.append(LinhaTexto(f"> {escolha}", BRANCO))
        
        # Lógica Secreta do SKY
        nome_upper = self.jogador_nome.upper().replace(" ", "").strip()
        if nome_upper == "SKY":
            self.adicionar_texto("Um arrepio percorre sua espinha...", VERMELHO)
            self.adicionar_texto("VOCÊ NÃO DEVERIA TER LEMBRADO DISSO...", MAGENTA)
            self.adicionar_texto("Algo dentro de você se agita.", VERMELHO)
            self.adicionar_texto("COMO VOCÊ SABE DISSO?", MAGENTA)
        else:
            self.adicionar_texto("Você tomou sua decisão...", BRANCO)
        
        self.adicionar_texto("--- FIM DA DEMO ---", BRANCO)
        self.estado = ESTADO_FIM

    def desenhar(self):
        TELA.fill(CINZA_ESCURO)
        
        y_offset = 20
        espacamento = 35
        
        # Lógica de "Rolagem": Se tiver muitas linhas, desenha apenas as últimas que cabem
        max_linhas = (ALTURA - 100) // espacamento
        linhas_visiveis = self.historico[-max_linhas:]
        
        for linha in linhas_visiveis:
            # Renderiza o texto
            superficie_texto = FONTE.render(linha.texto, True, linha.cor_texto)
            
            # Se tiver cor de fundo (Back.WHITE logic)
            if linha.cor_fundo:
                rect_fundo = superficie_texto.get_rect(topleft=(20, y_offset))
                pygame.draw.rect(TELA, linha.cor_fundo, rect_fundo)
                # Renderiza de novo sobre o fundo, garantindo contraste (Preto no Branco)
                superficie_texto = FONTE.render(linha.texto, True, PRETO) 
            
            TELA.blit(superficie_texto, (20, y_offset))
            y_offset += espacamento

        # Desenhar caixa de input se estiver esperando digitação
        if self.estado in [ESTADO_NOME, ESTADO_ESCOLHA]:
            txt_input = FONTE.render(f"> {self.input_atual}_", True, (0, 255, 0))
            TELA.blit(txt_input, (20, ALTURA - 50))

# --- Loop Principal ---
jogo = Jogo()
relogio = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if evento.type == pygame.KEYDOWN:
            jogo.processar_input(evento)

    jogo.desenhar()
    pygame.display.flip()
    relogio.tick(60)