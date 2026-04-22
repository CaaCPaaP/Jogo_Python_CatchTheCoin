import pygame
import random
from sys import exit #função para sair do loop 

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("boat.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=(LARGURA/2, ALTURA))
        self.peso = 0

    def playerInput(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left >= 0:
            self.rect.x -= 5 - self.peso

        if keys[pygame.K_RIGHT] and self.rect.right <= LARGURA:
            self.rect.x += 5 - self.peso

    def colisaoMoeda(self):
        if self.peso < 3:
            if pygame.sprite.spritecollide(jogador.sprite, moedas_grupo, True):
                self.peso += 0.5

    def colisaoPorto(self):
        if jogador.sprite.rect.colliderect(casa_rect):
            self.peso = 0


    def update(self):
        self.playerInput()
        self.colisaoMoeda()
        self.colisaoPorto()

class Moeda(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #self serve para chamar a classe
        moeda_maior = pygame.image.load('png/gold/gold_21.png').convert_alpha()
        moeda_tamanho = (18, 18)
        self.image = pygame.transform.scale(moeda_maior, moeda_tamanho)
        self.rect = self.image.get_rect(midbottom=(random.randint(0, LARGURA), -50))

    def queda(self):
        self.rect.y += 5

    def destruirMoeda(self):
        if self.rect.y >= ALTURA+50:
            self.kill()

    def update(self):
        self.queda()
        self.destruirMoeda()


pygame.init()

# Dimensões da tela
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Catch the coin")
# Cores básicas
AZUL = (137, 207, 240)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)

fonte = pygame.font.SysFont(None, 36)


# Grupo é a lista de todas as sprites
jogador = pygame.sprite.GroupSingle()
jogador.add(Jogador())


moedas_grupo = pygame.sprite.Group()

casa = pygame.image.load('porto.png')
casa_rect = casa.get_rect(bottomright=(LARGURA, ALTURA+38))



#função midbottom serve para centralizar o barco
#/2 dois para que o barco fique no meio e não nas extremidades
#rect é a função para criar um retangulo para mover o barco,fazer colisões 
#serve de superficie da imagem.

fundo = pygame.image.load('1.png').convert()
fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))




moeda_timer_evento = pygame.USEREVENT + 1
pygame.time.set_timer(moeda_timer_evento, 2000)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            #Função para sair da tela no botão de fechar

        if event.type == moeda_timer_evento:
            moedas_grupo.add(Moeda())
                
    tela.blit(fundo, (0,0))

    mensagem = fonte.render('Barco cheio', False, 'BLACK')
    mensagem_rect = mensagem.get_rect(midbottom=(jogador.sprite.rect.x, 550))

    

  

    #tela.fill(AZUL) #preenche o fundo em azul

    if jogador.sprite.peso >= 3:
        tela.blit(mensagem, mensagem_rect)
   






    """tela.blit(moeda, moeda_rect)
    cair_moeda(moeda_rect)"""

    tela.blit(casa, casa_rect)

    moedas_grupo.draw(tela)
    moedas_grupo.update()

    jogador.draw(tela)
    jogador.update()


    pygame.display.update()
    pygame.time.Clock().tick(60)




