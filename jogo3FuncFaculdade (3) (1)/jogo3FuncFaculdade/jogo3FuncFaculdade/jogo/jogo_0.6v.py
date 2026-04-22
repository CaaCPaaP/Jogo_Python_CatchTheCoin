import pygame
import random
from sys import exit

pygame.init()
pygame.mixer.init()
# === CARREGAR SONS ===

som_alerta = pygame.mixer.Sound('PNG/alerta/alerta.wav')
som_moeda = pygame.mixer.Sound('PNG/coin/coin.wav')
som_gameover = pygame.mixer.Sound('PNG/gameover/gameover.wav')

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Boat.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=(LARGURA / 2, ALTURA))
        self.peso = 0
        self.alerta_tocado = False
        self.texto_valor = ''
        self.tempo_valor = 0
        self.texto_valor = ''

        self.tempo_valor = pygame.time.get_ticks()

    def playerInput(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left >= 0:
            self.rect.x -= 5 - self.peso
        if keys[pygame.K_RIGHT]:
            if self.rect.right <= casa_rect.left:
                if self.peso < 3:
                    self.rect.x += 5 - self.peso
                else:
                    if self.rect.right <= LARGURA:
                        self.rect.x += 5 - self.peso


                

    def colisaoMoeda(self):
        global pontuacao_total
        if self.peso < 3:
            moedas_colididas = pygame.sprite.spritecollide(jogador.sprite, moedas_grupo, True)
            for moeda in moedas_colididas:
                pontuacao_total += moeda.valor
                self.peso += 0.5
                som_moeda.play()

                self.texto_valor = f'+{moeda.valor}'
                self.tempo_valor = pygame.time.get_ticks()


    def mostrarValorMoeda(self):
        tempo_atual = pygame.time.get_ticks()
        if self.texto_valor and tempo_atual - self.tempo_valor < 2000:
            texto = fonte.render(self.texto_valor, True, 'red')
            texto_rect = texto.get_rect(center=(self.rect.right, self.rect.top - 60))
            tela.blit(texto, texto_rect)
        elif tempo_atual - self.tempo_valor >= 2000:
            self.texto_valor = ''

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
        self.mostrarValorMoeda()

class Moeda(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.valor = 10
        moeda_maior_1 = pygame.image.load('png/gold/gold_21.png').convert_alpha()
        moeda_maior_2 = pygame.image.load('png/gold/gold_22.png').convert_alpha()
        moeda_maior_3 = pygame.image.load('png/gold/gold_23.png').convert_alpha()
        moeda_maior_4 = pygame.image.load('png/gold/gold_24.png').convert_alpha()
        moeda_maior_5 = pygame.image.load('png/gold/gold_25.png').convert_alpha()
        moeda_maior_6 = pygame.image.load('png/gold/gold_26.png').convert_alpha()
        moeda_maior_7 = pygame.image.load('png/gold/gold_27.png').convert_alpha()
        moeda_maior_8 = pygame.image.load('png/gold/gold_28.png').convert_alpha()
        moeda_maior_9 = pygame.image.load('png/gold/gold_29.png').convert_alpha()
        moeda_maior_10 = pygame.image.load('png/gold/gold_30.png').convert_alpha()
        self.frames = [moeda_maior_1, moeda_maior_2, moeda_maior_3, moeda_maior_4, moeda_maior_5,moeda_maior_6, moeda_maior_7,moeda_maior_8,moeda_maior_9, moeda_maior_10 ]

        for i in range(len(self.frames)):
            self.frames[i] = pygame.transform.scale(self.frames[i], (18, 18))

        self.frame_index = 0

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(midbottom=(random.randint(0, LARGURA - casa_rect.width), -50))

    def queda(self):
        self.rect.y += 2

    def destruirMoeda(self):
        if self.rect.y >= ALTURA + 50:
            self.kill()

    def animacao(self):
        self.frame_index += 0.1
        if self.frame_index >= len(self.frames): self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.queda()
        self.animacao()
        self.destruirMoeda()


class MoedaPrata(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.valor = 5
        moeda_maior_1 = pygame.image.load('png/silver/silver_20.png').convert_alpha()
        moeda_maior_2 = pygame.image.load('png/silver/silver_19.png').convert_alpha()
        moeda_maior_3 = pygame.image.load('png/silver/silver_18.png').convert_alpha()
        moeda_maior_4 = pygame.image.load('png/silver/silver_17.png').convert_alpha()
        moeda_maior_5= pygame.image.load('png/silver/silver_16.png').convert_alpha()
        moeda_maior_6 = pygame.image.load('png/silver/silver_15.png').convert_alpha()
        moeda_maior_7 = pygame.image.load('png/silver/silver_14.png').convert_alpha()
        moeda_maior_8= pygame.image.load('png/silver/silver_13.png').convert_alpha()
        moeda_maior_9 = pygame.image.load('png/silver/silver_12.png').convert_alpha()
        self.frames = [moeda_maior_1, moeda_maior_2, moeda_maior_3, moeda_maior_4, moeda_maior_5,moeda_maior_6, moeda_maior_7]
        for i in range(len(self.frames)):
            self.frames[i] = pygame.transform.scale(self.frames[i], (18, 18))

            self.frame_index = 0

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(midbottom=(random.randint(0, LARGURA - casa_rect.width), -50))

    def queda(self):
        self.rect.y += 3

    def destruirMoeda(self):
        if self.rect.y >= ALTURA + 50:
            self.kill()

    
    def animacao(self):
        self.frame_index += 0.1
        if self.frame_index >= len(self.frames): self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.queda()
        self.animacao()
        self.destruirMoeda()

class MoedaBronze(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.valor = 1
        moeda_maior_1 = pygame.image.load('png/bronze/bronze_10.png').convert_alpha()
        moeda_maior_2 = pygame.image.load('png/bronze/bronze_9.png').convert_alpha()
        moeda_maior_3 = pygame.image.load('png/bronze/bronze_8.png').convert_alpha()
        moeda_maior_4 = pygame.image.load('png/bronze/bronze_7.png').convert_alpha()
        moeda_maior_5 = pygame.image.load('png/bronze/bronze_6.png').convert_alpha()
        moeda_maior_6 = pygame.image.load('png/bronze/bronze_5.png').convert_alpha()
        moeda_maior_7 = pygame.image.load('png/bronze/bronze_4.png').convert_alpha()
        self.frames = [moeda_maior_1, moeda_maior_2, moeda_maior_3, moeda_maior_4, moeda_maior_5,moeda_maior_6, moeda_maior_7]
        for i in range(len(self.frames)):
            self.frames[i] = pygame.transform.scale(self.frames[i], (18, 18))

            self.frame_index = 0

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(midbottom=(random.randint(0, LARGURA - casa_rect.width), -50))

    def queda(self):
        self.rect.y += 5

    def destruirMoeda(self):
        if self.rect.y >= ALTURA + 50:
            self.kill()

    def animacao(self):
        self.frame_index += 0.1
        if self.frame_index >= len(self.frames): self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]


    def update(self):
        self.queda()
        self.animacao()
        self.destruirMoeda()


class Boneca(pygame.sprite.Sprite):
    def __init__(self, jogador):
        super().__init__()
        imagem_original = pygame.image.load("png/boneca/boneca.png").convert_alpha()
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

class Remo(pygame.sprite.Sprite):
    def __init__(self, boneca):
        super().__init__()
        self.boneca = boneca
        self.original_image = pygame.image.load('png/remo/remo.png').convert_alpha()
        escala = 0.2
        largura = int(self.original_image.get_width() * escala)
        altura = int(self.original_image.get_height() * escala)
        self.original_image = pygame.transform.scale(self.original_image, (largura, altura))
        self.image = self.original_image
        self.rect = self.image.get_rect()

        # Angulo inicial e controle de direção (1 para aumentar, -1 para diminuir)
        self.angle = -30
        self.direction = 1
        self.rotation_speed = 1  # graus por frame

        # Offset do remo em relação ao centro da boneca (ajuste conforme a imagem)
        self.offset_x = 10
        self.offset_y = 15

    def update(self):
        # Atualiza o ângulo para rotacionar o remo
        self.angle += self.direction * self.rotation_speed
        if self.angle > 30:
            self.direction = -1
        elif self.angle < -30:
            self.direction = 1

        # Rotaciona a imagem do remo em torno do centro
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()

        # Posiciona o remo na mão da boneca (usando o centro da boneca + offset)
        boneca_pos = self.boneca.rect.center
        self.rect.center = (boneca_pos[0] + self.offset_x, boneca_pos[1] + self.offset_y)

    import pygame
import sys

class Button:
    def __init__(self, texto, pos, fonte, cor_normal, cor_hover):
        self.texto = texto
        self.pos = pos
        self.fonte = fonte
        self.cor_normal = cor_normal
        self.cor_hover = cor_hover
        self.rect = None
        self.render_text(cor_normal)

    def render_text(self, cor):
        self.text_surface = self.fonte.render(self.texto, True, cor)
        self.rect = self.text_surface.get_rect(center=self.pos)

    def draw(self, tela):
        # Detecta se mouse está sobre o botão
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.render_text(self.cor_hover)
        else:
            self.render_text(self.cor_normal)
        tela.blit(self.text_surface, self.rect)

    def clicado(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  # Clique esquerdo
            if self.rect.collidepoint(evento.pos):
                return True
        return False


class Menu:
    def __init__(self, tela, fonte):
        self.tela = tela
        self.fonte = fonte
        self.rodando = True

        cinza_normal = (160, 160, 160)
        cinza_hover = (200, 200, 200)

        self.botao_comecar = Button("Começar", (LARGURA // 2, ALTURA // 2), fonte, cinza_normal, cinza_hover,
                                    "icone_start.png")
        self.botao_sair = Button("Sair", (LARGURA // 2, ALTURA // 2 + 60), fonte, cinza_normal, cinza_hover,
                                 "icone_sair.png")

        self.logo = pygame.image.load("menu.jpg").convert_alpha()
        self.logo = pygame.transform.scale(self.logo, (LARGURA, ALTURA))

    def exibir(self):
        while self.rodando:
            self.tela.fill((0, 0, 0))

            # Desenhar logo
            logo_rect = self.logo.get_rect(topleft=(0, 0))
            self.tela.blit(self.logo, logo_rect)

            # Desenhar botões
            self.botao_comecar.draw(self.tela)
            self.botao_sair.draw(self.tela)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if self.botao_comecar.clicado(event):
                    self.rodando = False  # Sai do menu e começa o jogo

                if self.botao_sair.clicado(event):
                    pygame.quit()
                    sys.exit()


"""def mostrarValorMoeda(jogador, moeda):
    if pygame.time.get_ticks():
        texto_valor = 'teste'
        texto = fonte.render(texto_valor, True, 'black')
        texto_rect = texto.get_rect(center=(jogador.sprite.rect.right, jogador.sprite.rect.top - 60))
        tela.blit(texto, texto_rect)"""

tempo_mostrar_texto = 2000
mostrar_texto = False


# === CONFIGURAÇÕES GLOBAIS ===
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Catch the coin")

font = pygame.font.Font(None, 15)
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

remo_grupo = pygame.sprite.Group()
remo = Remo(boneca_grupo.sprites()[0])
remo_grupo.add(remo)








moedas_grupo = pygame.sprite.Group()
casa = pygame.image.load('porto.png')
casa_rect = casa.get_rect(bottomright=(LARGURA, ALTURA + 38))
fundo = pygame.image.load('png/fundo2.png').convert()
fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))

# Fundo para a tela de instruções
fundo_instrucoes = pygame.image.load("2.jpg").convert_alpha()
fundo_instrucoes = pygame.transform.scale(fundo_instrucoes, (LARGURA, ALTURA))

moeda_timer_evento = pygame.USEREVENT + 1
pygame.time.set_timer(moeda_timer_evento, 2000)

clock = pygame.time.Clock()

menu = Menu(tela, fonte)
menu.exibir()

fase = Fase()  # Garante que o jogo sempre começará na fase 1
inicio_jogo = pygame.time.get_ticks()  # Reinicia o tempo total do jogo


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

    remo_grupo.update()
    remo_grupo.draw(tela)

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




