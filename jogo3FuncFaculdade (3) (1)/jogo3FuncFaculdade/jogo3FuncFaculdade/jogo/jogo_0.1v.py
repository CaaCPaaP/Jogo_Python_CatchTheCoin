import pygame
import random
from sys import exit

pygame.init()

# === CARREGAR SONS ===
som_alerta = pygame.mixer.Sound(r'D:\Usuario\Pictures\jogo\PNG\alerta\alerta.wav')
som_moeda = pygame.mixer.Sound(r'D:\Usuario\Pictures\jogo\PNG\coin\coin.wav')
som_gameover = pygame.mixer.Sound(r'D:\Usuario\Pictures\jogo\PNG\gameover\gameover.wav')


class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("boat.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=(LARGURA / 2, ALTURA))
        self.peso = 0
        self.alerta_tocado = False

    def playerInput(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left >= 0:
            self.rect.x -= 5 - self.peso
        if keys[pygame.K_RIGHT] and self.rect.right <= LARGURA:
            self.rect.x += 5 - self.peso

    def colisaoMoeda(self):
        global pontuacao_total
        if self.peso < 3:
            moedas_colididas = pygame.sprite.spritecollide(jogador.sprite, moedas_grupo, True)
            for moeda in moedas_colididas:
                self.peso += 0.5
                pontuacao_total += moeda.valor
                som_moeda.play()

    def colisaoPorto(self):
        global tempo_restante
        if self.rect.colliderect(casa_rect):
            self.peso = 0
            tempo_restante = None
            global piscar_vermelho
            piscar_vermelho = False
            self.alerta_tocado = False

    def update(self):
        self.playerInput()
        self.colisaoMoeda()
        self.colisaoPorto()


class Moeda(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.valor = 10
        moeda_maior = pygame.image.load('png/gold/gold_21.png').convert_alpha()
        self.image = pygame.transform.scale(moeda_maior, (18, 18))
        self.rect = self.image.get_rect(midbottom=(random.randint(0, LARGURA), -50))

    def queda(self):
        self.rect.y += 2

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
        self.image = pygame.transform.scale(moeda_maior, (18, 18))
        self.rect = self.image.get_rect(midbottom=(random.randint(0, LARGURA), -50))

    def queda(self):
        self.rect.y += 3

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
        self.image = pygame.transform.scale(moeda_maior, (18, 18))
        self.rect = self.image.get_rect(midbottom=(random.randint(0, LARGURA), -50))

    def queda(self):
        self.rect.y += 5

    def destruirMoeda(self):
        if self.rect.y >= ALTURA + 50:
            self.kill()

    def update(self):
        self.queda()
        self.destruirMoeda()


class Boneca(pygame.sprite.Sprite):
    def __init__(self, jogador):
        super().__init__()
        imagem_original = pygame.image.load(r"D:\Usuario\Pictures\jogo\png\boneca\boneca.png").convert_alpha()
        largura_barco, altura_barco = jogador.image.get_size()

        escala_largura = int(largura_barco * 0.7)
        escala_altura = int(imagem_original.get_height() * (escala_largura / imagem_original.get_width()))

        self.image = pygame.transform.scale(imagem_original, (escala_largura, escala_altura))
        self.rect = self.image.get_rect()

        cintura_y = jogador.rect.top + int(altura_barco * 0.6)
        self.rect.midbottom = (jogador.rect.centerx, cintura_y)
        self.jogador = jogador

    def update(self):
        largura_barco, altura_barco = self.jogador.image.get_size()
        cintura_y = self.jogador.rect.top + int(altura_barco * 0.6)
        self.rect.midbottom = (self.jogador.rect.centerx, cintura_y)


# === CONFIGURAÇÕES GLOBAIS ===
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Catch the coin")
AZUL = (137, 207, 240)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
fonte = pygame.font.SysFont(None, 36)

tempo_limite = 5
tempo_restante = None
game_over = False
pontuacao_total = 0
inicio_jogo = pygame.time.get_ticks()
piscar_vermelho = False
contador_piscar = 0
game_over_tocado = False

jogador = pygame.sprite.GroupSingle()
jogador.add(Jogador())

boneca_grupo = pygame.sprite.Group()
boneca_grupo.add(Boneca(jogador.sprite))

moedas_grupo = pygame.sprite.Group()
casa = pygame.image.load('porto.png')
casa_rect = casa.get_rect(bottomright=(LARGURA, ALTURA + 38))
fundo = pygame.image.load('1.png').convert()
fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))

moeda_timer_evento = pygame.USEREVENT + 1
pygame.time.set_timer(moeda_timer_evento, 2000)

clock = pygame.time.Clock()

# --- LOOP PRINCIPAL ---
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

    if jogador.sprite.peso >= 3:
        piscar_vermelho = True
        if not jogador.sprite.alerta_tocado:
            som_alerta.play()
            jogador.sprite.alerta_tocado = True
        contador_piscar += 1
        if contador_piscar % 20 < 10:
            tela.fill(VERMELHO)
        else:
            tela.blit(fundo, (0, 0))
    else:
        piscar_vermelho = False
        contador_piscar = 0
        tela.blit(fundo, (0, 0))

    moedas_grupo.draw(tela)
    moedas_grupo.update()

    jogador.draw(tela)
    jogador.update()

    boneca_grupo.draw(tela)
    boneca_grupo.update()

    if jogador.sprite.peso >= 3:
        mensagem = fonte.render('Barco cheio', False, PRETO)
        mensagem_rect = mensagem.get_rect(midbottom=(jogador.sprite.rect.x, 550))
        tela.blit(mensagem, mensagem_rect)

    tela.blit(casa, casa_rect)

    if jogador.sprite.peso >= 3:
        if tempo_restante is None:
            tempo_restante = pygame.time.get_ticks()
        tempo_atual = pygame.time.get_ticks()
        segundos_passados = (tempo_atual - tempo_restante) / 1000
        if segundos_passados >= tempo_limite:
            game_over = True

        tempo_texto = fonte.render(f'Tempo: {max(0, int(tempo_limite - segundos_passados))}', True, PRETO)
        tela.blit(tempo_texto, (10, 100))

    tempo_total_segundos = (pygame.time.get_ticks() - inicio_jogo) // 1000
    tempo_total_texto = fonte.render(f'Tempo total: {tempo_total_segundos}s', True, PRETO)
    pontuacao_texto = fonte.render(f'Score: {pontuacao_total}', True, PRETO)
    tela.blit(tempo_total_texto, (10, 10))
    tela.blit(pontuacao_texto, (10, 40))

    if game_over:
        if not game_over_tocado:
            som_gameover.play()
            game_over_tocado = True

        # Tela preta semitransparente para escurecer o fundo
        tela_preta = pygame.Surface((LARGURA, ALTURA))
        tela_preta.set_alpha(200)  # 0 transparente, 255 opaco
        tela_preta.fill((0, 0, 0))
        tela.blit(tela_preta, (0, 0))

        mensagem_gameover = fonte.render('GAME OVER', True, VERMELHO)
        mensagem_gameover_rect = mensagem_gameover.get_rect(center=(LARGURA / 2, ALTURA / 2))
        tela.blit(mensagem_gameover, mensagem_gameover_rect)
        pygame.display.update()
        pygame.time.delay(5000)
        pygame.quit()
        exit()

    pygame.display.update()
    clock.tick(60)



