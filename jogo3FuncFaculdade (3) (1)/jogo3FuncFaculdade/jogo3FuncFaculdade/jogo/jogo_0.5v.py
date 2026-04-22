import pygame
import random
from sys import exit  # função para sair do loop


class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("boat.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=(LARGURA / 2, ALTURA))
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
        global tempo_restante  # reinicia tempo se descarregou
        if jogador.sprite.rect.colliderect(casa_rect):
            self.peso = 0
            tempo_restante = None  # reseta contagem
            global piscar_vermelho
            piscar_vermelho = False  # para o efeito de piscar vermelho

    def update(self):
        self.playerInput()
        self.colisaoMoeda()
        self.colisaoPorto()


class Moeda(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.valor = 10  # valor da moeda ouro
        moeda_maior = pygame.image.load('png/gold/gold_21.png').convert_alpha()
        moeda_tamanho = (18, 18)
        self.image = pygame.transform.scale(moeda_maior, moeda_tamanho)
        self.rect = self.image.get_rect(midbottom=(random.randint(0, LARGURA), -50))

    def queda(self):
        self.rect.y += 2  # OURO = queda mais lenta

    def destruirMoeda(self):
        if self.rect.y >= ALTURA + 50:
            self.kill()

    def update(self):
        self.queda()
        self.destruirMoeda()


class MoedaPrata(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.valor = 5
        moeda_maior = pygame.image.load('png/silver/silver_20.png').convert_alpha()
        moeda_tamanho = (18, 18)
        self.image = pygame.transform.scale(moeda_maior, moeda_tamanho)
        self.rect = self.image.get_rect(midbottom=(random.randint(0, LARGURA), -50))

    def queda(self):
        self.rect.y += 3  # PRATA = queda média

    def destruirMoeda(self):
        if self.rect.y >= ALTURA + 50:
            self.kill()

    def update(self):
        self.queda()
        self.destruirMoeda()


class MoedaBronze(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.valor = 1
        moeda_maior = pygame.image.load('png/bronze/bronze_10.png').convert_alpha()
        moeda_tamanho = (18, 18)
        self.image = pygame.transform.scale(moeda_maior, moeda_tamanho)
        self.rect = self.image.get_rect(midbottom=(random.randint(0, LARGURA), -50))

    def queda(self):
        self.rect.y += 5  # BRONZE = queda mais rápida

    def destruirMoeda(self):
        if self.rect.y >= ALTURA + 50:
            self.kill()

    def update(self):
        self.queda()
        self.destruirMoeda()


pygame.init()

# Dimensões da tela
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Catch the coin")
AZUL = (137, 207, 240)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)

fonte = pygame.font.SysFont(None, 36)

# Variáveis de tempo
tempo_limite = 5  # segundos para voltar ao porto
tempo_restante = None
game_over = False

# Controle do efeito piscar vermelho
piscar_vermelho = False
contador_piscar = 0

jogador = pygame.sprite.GroupSingle()
jogador.add(Jogador())

moedas_grupo = pygame.sprite.Group()

casa = pygame.image.load('porto.png')
casa_rect = casa.get_rect(bottomright=(LARGURA, ALTURA + 38))

fundo = pygame.image.load('1.png').convert()
fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))

moeda_timer_evento = pygame.USEREVENT + 1
pygame.time.set_timer(moeda_timer_evento, 2000)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == moeda_timer_evento:
            MAX_MOEDAS = 5
            if len(moedas_grupo) < MAX_MOEDAS:
                tipos_moeda = ['ouro', 'prata', 'bronze']
                quantidade = random.randint(1, min(3, MAX_MOEDAS - len(moedas_grupo)))
                moedas_selecionadas = random.sample(tipos_moeda, quantidade)
                for moeda in moedas_selecionadas:
                    if moeda == 'ouro':
                        moedas_grupo.add(Moeda())
                    elif moeda == 'prata':
                        moedas_grupo.add(MoedaPrata())
                    else:
                        moedas_grupo.add(MoedaBronze())

    tela.blit(fundo, (0, 0))

    # ⬇️ Lógica para piscar vermelho se o barco estiver cheio
    if jogador.sprite.peso >= 3:
        piscar_vermelho = True
        contador_piscar += 1
        if contador_piscar % 20 < 10:
            tela.fill(VERMELHO)
        else:
            tela.blit(fundo, (0, 0))  # volta ao fundo normal para piscar
    else:
        piscar_vermelho = False
        contador_piscar = 0
        tela.blit(fundo, (0, 0))  # fundo normal

    moedas_grupo.draw(tela)
    moedas_grupo.update()

    jogador.draw(tela)
    jogador.update()

    # Mostra mensagem se barco estiver cheio
    if jogador.sprite.peso >= 3:
        mensagem = fonte.render('Barco cheio', False, PRETO)
        mensagem_rect = mensagem.get_rect(midbottom=(jogador.sprite.rect.x, 550))
        tela.blit(mensagem, mensagem_rect)

    tela.blit(casa, casa_rect)

    # ⏱ Cronômetro e verificação de tempo
    if jogador.sprite.peso >= 3:
        if tempo_restante is None:
            tempo_restante = pygame.time.get_ticks()
        tempo_atual = pygame.time.get_ticks()
        segundos_passados = (tempo_atual - tempo_restante) / 1000
        if segundos_passados >= tempo_limite:
            game_over = True

        tempo_texto = fonte.render(f'Tempo: {max(0, int(tempo_limite - segundos_passados))}', True, PRETO)
        tela.blit(tempo_texto, (10, 40))

    # 🛑 GAME OVER
    if game_over:
        # Tela escurecida (overlay preto com transparência)
        overlay = pygame.Surface((LARGURA, ALTURA))
        overlay.set_alpha(180)  # Transparência
        overlay.fill(PRETO)
        tela.blit(overlay, (0, 0))

        gameover_msg = fonte.render('GAME OVER', True, VERMELHO)
        tela.blit(gameover_msg, (LARGURA // 2 - gameover_msg.get_width() // 2, ALTURA // 2))

        pygame.display.update()
        pygame.time.delay(3000)
        pygame.quit()
        exit()

    pygame.display.update()
    clock.tick(60)
