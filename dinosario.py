
import pygame #importa o pygame
import os #importa o sistema operacional
import random #importa o aleatorio

pygame.init() #inicia o pygame
#definições da tela:
altura_tela = 600
largura_tela = 1100
tela = pygame.display.set_mode((largura_tela, altura_tela))
#definindo as imagens
correndo = [[pygame.image.load(os.path.join("Assets/Dino", "DinoRun1.png")),
            pygame.image.load(os.path.join("Assets/Dino", "DinoRun2.png"))],

            [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1_emo.png")),
            pygame.image.load(os.path.join("Assets/Dino", "DinoRun2_emo.png"))],
            
            [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1_inv.png")),
            pygame.image.load(os.path.join("Assets/Dino", "DinoRun2_inv.png"))],

            [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1_niver.png")),
            pygame.image.load(os.path.join("Assets/Dino", "DinoRun2_niver.png"))],
            
            [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1_dino.png")),
            pygame.image.load(os.path.join("Assets/Dino", "DinoRun2_dino.png"))],

            [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1_morte.png")),
            pygame.image.load(os.path.join("Assets/Dino", "DinoRun2_morte.png"))]]

pulando = [pygame.image.load(os.path.join("Assets/Dino", "DinoJump.png")),

           pygame.image.load(os.path.join("Assets/Dino", "DinoJump_emo.png")),
           
           pygame.image.load(os.path.join("Assets/Dino", "DinoJump_inv.png")),
           
           pygame.image.load(os.path.join("Assets/Dino", "DinoJump_niver.png")),

           pygame.image.load(os.path.join("Assets/Dino", "DinoJump_dino.png")),

           pygame.image.load(os.path.join("Assets/Dino", "DinoJump_morte.png"))]

abaixando = [[pygame.image.load(os.path.join("Assets/Dino", "DinoDuck1.png")),
             pygame.image.load(os.path.join("Assets/Dino", "DinoDuck2.png"))],

             [pygame.image.load(os.path.join("Assets/Dino", "DinoDuck1_emo.png")),
             pygame.image.load(os.path.join("Assets/Dino", "DinoDuck2_emo.png"))],
             
            [pygame.image.load(os.path.join("Assets/Dino", "DinoDuck1_inv.png")),
             pygame.image.load(os.path.join("Assets/Dino", "DinoDuck2_inv.png"))],

            [pygame.image.load(os.path.join("Assets/Dino", "DinoDuck1_niver.png")),
             pygame.image.load(os.path.join("Assets/Dino", "DinoDuck2_niver.png"))],

            [pygame.image.load(os.path.join("Assets/Dino", "DinoDuck1_dino.png")),
             pygame.image.load(os.path.join("Assets/Dino", "DinoDuck2_dino.png"))],

            [pygame.image.load(os.path.join("Assets/Dino", "DinoDuck1_morte.png")),
             pygame.image.load(os.path.join("Assets/Dino", "DinoDuck2_morte.png"))]]

bazuca = [[pygame.image.load(os.path.join("Assets/Dino", "DinoRunB1.png")),
          pygame.image.load(os.path.join("Assets/Dino", "DinoRunB2.png"))],
          
          [pygame.image.load(os.path.join("Assets/Dino", "DinoRunB1_emo.png")),
          pygame.image.load(os.path.join("Assets/Dino", "DinoRunB2_emo.png"))],
          
          [pygame.image.load(os.path.join("Assets/Dino", "DinoRunB1_inv.png")),
          pygame.image.load(os.path.join("Assets/Dino", "DinoRunB2_inv.png"))],

          [pygame.image.load(os.path.join("Assets/Dino", "DinoRunB1_niver.png")),
          pygame.image.load(os.path.join("Assets/Dino", "DinoRunB2_niver.png"))],

          [pygame.image.load(os.path.join("Assets/Dino", "DinoRunB1_dino.png")),
          pygame.image.load(os.path.join("Assets/Dino", "DinoRunB2_dino.png"))],

          [pygame.image.load(os.path.join("Assets/Dino", "DinoRunB1_morte.png")),
          pygame.image.load(os.path.join("Assets/Dino", "DinoRunB2_morte.png"))]]

voando = [[pygame.image.load(os.path.join("Assets/Dino", "DinoFly1.png")),
          pygame.image.load(os.path.join("Assets/Dino", "DinoFly2.png"))],
          
          [pygame.image.load(os.path.join("Assets/Dino", "DinoFly1_emo.png")),
          pygame.image.load(os.path.join("Assets/Dino", "DinoFly2_emo.png"))],
          
          [pygame.image.load(os.path.join("Assets/Dino", "DinoFly1_inv.png")),
          pygame.image.load(os.path.join("Assets/Dino", "DinoFly2_inv.png"))],
          
          [pygame.image.load(os.path.join("Assets/Dino", "DinoFly1_niver.png")),
          pygame.image.load(os.path.join("Assets/Dino", "DinoFly2_niver.png"))],

          [pygame.image.load(os.path.join("Assets/Dino", "DinoFly1_dino.png")),
          pygame.image.load(os.path.join("Assets/Dino", "DinoFly2_dino.png"))],

          [pygame.image.load(os.path.join("Assets/Dino", "DinoFly1_morte.png")),
          pygame.image.load(os.path.join("Assets/Dino", "DinoFly2_morte.png"))]]

cactus_pequeno = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
                  pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
                  pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]
cactus_grande = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
                 pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
                 pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png"))]
pterodatilo = [pygame.image.load(os.path.join("Assets/Bird", "Bird1.png")),
               pygame.image.load(os.path.join("Assets/Bird", "Bird2.png"))]
espinho = [pygame.image.load(os.path.join("Assets/Other", "espinhos.png"))]
parede = [pygame.image.load(os.path.join("Assets/Other", "parede.png"))]
boss_img = [pygame.image.load(os.path.join("Assets/Other", "boss1.png")),
            pygame.image.load(os.path.join("Assets/Other", "boss2.png"))]
nuvem = [pygame.image.load(os.path.join("Assets/Other", "Cloud.png")),
         pygame.image.load(os.path.join("Assets/Other", "alexandre.png")),
         pygame.image.load(os.path.join("Assets/Other", "dani.png"))]
nsei = 0
fundo = pygame.image.load(os.path.join("Assets/Other", "Track.png"))

b_jogar = pygame.image.load(os.path.join("Assets/Other", "botao_jogar.png"))
b_menu = pygame.image.load(os.path.join("Assets/Other", "botao_menu.png"))
b_skins = pygame.image.load(os.path.join("Assets/Other", "botao_skins.png"))
b_normal = [pygame.image.load(os.path.join("Assets/Other", "normal.png")),
            pygame.image.load(os.path.join("Assets/Other", "normal_sel.png"))]
b_emo = [pygame.image.load(os.path.join("Assets/Other", "emo.png")),
        pygame.image.load(os.path.join("Assets/Other", "emo_sel.png")),
        pygame.image.load(os.path.join("Assets/Other", "bloqueado.png"))]
b_inv = [pygame.image.load(os.path.join("Assets/Other", "inver.png")),
        pygame.image.load(os.path.join("Assets/Other", "inver_sel.png")),
        pygame.image.load(os.path.join("Assets/Other", "bloqueado.png"))]
b_niver = [pygame.image.load(os.path.join("Assets/Other", "niver.png")),
        pygame.image.load(os.path.join("Assets/Other", "niver_sel.png")),
        pygame.image.load(os.path.join("Assets/Other", "bloqueado.png"))]
b_dino = [pygame.image.load(os.path.join("Assets/Other", "dino.png")),
        pygame.image.load(os.path.join("Assets/Other", "dino_sel.png")),
        pygame.image.load(os.path.join("Assets/Other", "bloqueado.png"))]
b_morte = [pygame.image.load(os.path.join("Assets/Other", "morte.png")),
        pygame.image.load(os.path.join("Assets/Other", "morte_sel.png")),
        pygame.image.load(os.path.join("Assets/Other", "bloqueado.png"))]

if os.path.exists("pontos.txt"):
            with open("pontos.txt", "r") as file:
                maior_pontuacao = int(file.read())

oof = pygame.mixer.Sound("Assets/Sounds/oof_p.mp3")
OOF = pygame.mixer.Sound("Assets/Sounds/OOF_b.mp3")
som_tiro = pygame.mixer.Sound("Assets/Sounds/Tiro.wav")
som_pulo = pygame.mixer.Sound("Assets/Sounds/Som_pulo.wav")
som_morte = pygame.mixer.Sound("Assets/Sounds/Som_morte.mp3")

skin = 0
# Classe do projétil da bazuca
class Projetil:
    def __init__(self, x, y):
        self.image = pygame.image.load(os.path.join("Assets/Other", "Bullet.png"))  
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidade = 20  # Velocidade do projétil

    def update(self):
        self.rect.x += self.velocidade  # Faz o projétil se mover para a direita

    def draw(self, tela):
        tela.blit(self.image, (self.rect.x, self.rect.y))

# Classe do dinossauro
class dinossauro:
    pos_X = 80
    pos_Y = 310
    pos_Y_duck = 340 #posição abaixado
    velocidade_pulo = 8.5 #"força do pulo"
    morreu = 0
    mortes = 0
    if os.path.exists("mortes.txt"):
        file = open("mortes.txt", "r")
        for p in file.readlines():
            mortes = int(p)
        file.close()
# define a funçao "self"
    def __init__(self):
        #imagens
        self.duck_img = abaixando[skin]
        self.run_img = correndo[skin]
        self.jump_img = pulando[skin]
        self.bazuca_img = bazuca[skin]
        self.fly_img = voando[skin]
        #define o estado das ações quando iniciado:
        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False
        self.dino_bazuca = False
        self.dino_voo = False
        self.recarga_voo = True
        self.tempo_recarga_voo = False
        #definições de controle funcional
        self.step_index = 0
        self.vel_pulo = self.velocidade_pulo
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.pos_X
        self.dino_rect.y = self.pos_Y
        self.tempo_bazuca = 0  # Variável para controlar o tempo da bazuca
        self.bazuca_ativa = False 
        self.projeteis = []  # Lista para armazenar os projéteis
#controles e ações
    def update(self, input):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        if self.dino_bazuca:
            self.bazuca()
        if self.dino_voo:
            self.voo()
        if self.step_index >= 10:
            self.step_index = 0

        # Controle da bazuca
        if input[pygame.K_LEFT] and not self.bazuca_ativa and not self.dino_duck:
            self.dino_duck = False
            self.dino_run = False
            self.dino_bazuca = True
            self.tempo_bazuca = pygame.time.get_ticks()  # Ativa o temporizador
            self.bazuca_ativa = True  # Marca que a bazuca está ativa
            self.atirar()  # Atira o projétil
            som_tiro.play()

        # Desativar a bazuca após 1/2 segundo
        if self.bazuca_ativa and pygame.time.get_ticks() - self.tempo_bazuca > 500:
            self.dino_bazuca = False
            
            self.bazuca_ativa = False  # Reset da bazuca

        # pulo
        if input[pygame.K_UP] and not self.dino_jump and self.dino_rect.y == 310:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
            som_pulo.play()
      
        if input[pygame.K_DOWN] and self.dino_jump:
            self.vel_pulo -= 0.5
            
        #abaixar
        if input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
            self.dino_bazuca = False
        #correr
        if not (self.dino_jump or input[pygame.K_DOWN] or self.bazuca_ativa):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False
        #voar
        
        if input[pygame.K_RIGHT] and self.dino_jump and self.recarga_voo:
            self.dino_voo = True
            self.tempo_de_voo = pygame.time.get_ticks()
            self.recarga_voo = False 
            self.tempo_recarga_voo = True           
        if self.dino_voo and pygame.time.get_ticks() - self.tempo_de_voo > 1500:
            self.dino_voo = False
            self.vel_pulo = self.parado

        if self.tempo_recarga_voo and self.dino_rect.y == 310:
            self.recarga_voo = True    
            self.tempo_recarga_voo = False

        if input[pygame.K_DOWN] and self.dino_voo:
            self.dino_voo = False

        # Atualizar os projéteis
        for proj in self.projeteis:
            proj.update()
# define oque acontece quando a ação e chamada
    def atirar(self):
        # Cria um novo projétil na posição do dinossauro
        novo_projetil = Projetil(self.dino_rect.x + self.dino_rect.width, self.dino_rect.y + self.dino_rect.height // 2 -20)
        self.projeteis.append(novo_projetil)

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.pos_X
        self.dino_rect.y = self.pos_Y_duck
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.pos_X
        self.dino_rect.y = self.pos_Y
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.vel_pulo * 4
            self.vel_pulo -= 0.8

            if self.dino_rect.y > 310:
                self.dino_jump = False
                self.vel_pulo = self.velocidade_pulo
        if self.vel_pulo < - self.velocidade_pulo:
            self.dino_jump = False
            self.vel_pulo = self.velocidade_pulo

    def bazuca(self):
        self.image = self.bazuca_img[self.step_index // 5]
        if not self.dino_voo:
            self.step_index += 1
        
    
    def voo(self):
        self.image = self.fly_img[self.step_index // 5]
        self.step_index += 1
        if self.dino_voo:
            self.parado = self.vel_pulo
            self.vel_pulo = 0


    def morrer(self):
        pygame.time.delay(500)  # Pausa breve para dar feedback visual
        self.mortes += 1
        # Salva o número de mortes no arquivo
        with open("mortes.txt", "w") as file:
            file.write(str(self.mortes))
        # Chama o menu de morte
        menu(1)

    def draw(self, tela):
        tela.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
        # Desenhar os projéteis
        for proj in self.projeteis:
            proj.draw(tela)

class cloud:

    #nuvem :D
    def __init__(self,nsei):
        self.nsei = nsei
        self.x = largura_tela + random.randint(700, 1000)
        self.y = random.randint(40, 110)
        self.image = nuvem[self.nsei]
        self.largura = self.image.get_width()
        
       

    def update(self):
        self.x -= vel_jogo
        if self.x < -self.largura:
            self.x = largura_tela + random.randint(250, 300)
            self.y = random.randint(50, 100)
        if pygame.time.get_ticks() - self.tempo > 300:
                    aleatorio = random.randit(1,5) 
                    if aleatorio == 5:
                        print("buu")
                        teste = random.randint(0,1)
                        if teste == 0:
                            self.nsei = 1
                        else:
                            self.nsei = 2
    def draw(self, tela): 
        tela.blit(self.image, (self.x, self.y))

 #obstaculos
class Obstacle:
   
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = largura_tela

    def update(self):
        self.rect.x -=vel_jogo
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, tela):
        tela.blit(self.image[self.type], self.rect)


class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325


class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0
    def draw(self, tela):
        if self.index >= 9:
            self.index = 0
        tela.blit(self.image[self.index//5], self.rect)
        self.index += 1


class Espinho(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 360


class Parede(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 100


class Boss:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = largura_tela  # Começa fora da tela
        self.rect.y = 150  # Posição Y do boss
        self.vida = 10  # Vida do boss
        self.velocidade = 5  # Velocidade de movimento
        self.ataque_cooldown = 0  # Tempo entre ataques (em milissegundos)
        self.ultimo_ataque = pygame.time.get_ticks()  # Tempo do último ataque
        self.ataques = []  # Lista de ataques (quadrados vermelhos)
        self.derrotado = True  # Indica se o boss foi derrotado
        self.x_barra = 800

        
    def update(self, tela, player):
        self.barra_vida = pygame.Surface([self.x_barra, 30])
        self.dano = pygame.Surface([800, 30])
        self.barra_vida.fill((0,255,0))
        self.dano.fill((255,0,0))
        self.dano_rect = self.dano.get_rect(midleft=(largura_tela // 8, altura_tela // 1.2))
        self.vida_rect = self.barra_vida.get_rect(midleft=(largura_tela // 8, altura_tela // 1.2))

        tela.blit(self.dano, self.dano_rect)
        tela.blit(self.barra_vida, self.vida_rect)
        
        if self.derrotado:
            return  # Se o boss foi derrotado, não faz nada

        # Movimentação do boss
        if self.rect.x > largura_tela - 200:  # Para o boss antes de sair da tela
            self.rect.x -= self.velocidade

        # Verifica se é hora de atacar
        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - self.ultimo_ataque >= self.ataque_cooldown:
            self.atacar(player)  # Passa o jogador como referência para o ataque
            self.ultimo_ataque = tempo_atual

        # Atualiza e desenha os ataques do boss
        for ataque in self.ataques:
            ataque.update(player)  # Move o ataque em direção ao jogador
            ataque.draw(tela)  # Desenha o ataque

        # Remove ataques que saíram da tela
        self.ataques = [ataque for ataque in self.ataques if ataque.rect.x > 0]

        # Desenha o boss
        tela.blit(self.image[self.type], self.rect)

    def atacar(self, player):
        # Cria um novo ataque (quadrado vermelho) na posição do boss
        novo_ataque = AtaqueBoss(self.rect.x, self.rect.y, player)
        self.ataques.append(novo_ataque)

    def levar_dano(self, quantidade):
        self.x_barra -= 80
        self.vida -= quantidade
        if self.vida <= 5:
            self.type = 1
            self.ataque_cooldown = 700
        if self.vida <= 0:
            self.morrer()

    def morrer(self):
        self.ataques = []
        pygame.mixer.music.stop()
        OOF.play()
        OOF.set_volume(0.7)
        self.derrotado = True

class AtaqueBoss:
    def __init__(self, x, y, player):
        global vel_jogo
        tipo = random.randint(0, 1)
        if tipo == 0:
            self.image = pygame.Surface((100, 20))  # Cria um quadrado vermelho
            self.image.fill((255, 0, 0))  # Preenche o quadrado com vermelho
            self.rect = self.image.get_rect()
            self.rect.x = x 
            self.rect.y = y + 230
        else:
            self.image = pygame.Surface((20, 200))  # Cria um quadrado vermelho
            self.image.fill((255, 0, 0))  # Preenche o quadrado com vermelho
            self.rect = self.image.get_rect()
            self.rect.x = x 
            self.rect.y = y -20           
        

    def update(self, player):
        self.rect.x -= vel_jogo

    def draw(self, tela):
        tela.blit(self.image, self.rect)

#maioria das coisas
#chama as funções definidas anteriormente
def main():
    global vel_jogo, x_pos_bg, y_pos_bg, pontos, obstacles
    funcionar = True
    relogio = pygame.time.Clock()
    player = dinossauro()
    Nuvem = cloud(nsei)
    boss = Boss(boss_img, 0)  # Cria o boss
    vel_jogo = 14
    x_pos_bg = 0
    y_pos_bg = 380
    pontos = 1
    fonte = pygame.font.Font('Minecraft.ttf', 20)
    obstacles = []
    

    def pontuacao():
        global pontos, vel_jogo
        pontos += 1
        if os.path.exists("pontos.txt"):
            with open("pontos.txt", "r") as file:
                maior_pontuacao = int(file.read())
        if pontos > maior_pontuacao:
            with open("pontos.txt", "w") as file:
                file.write(str(pontos))
        if vel_jogo <= 40 and pontos % 100 == 0:
            vel_jogo += 1
        texto = fonte.render("pontos: " + str(pontos), True, (0, 0, 0))
        texto2 = fonte.render("melhor partida: " + str(maior_pontuacao), True, (0, 0, 0))
        textrect = texto.get_rect(center=(1000, 30))
        textrect2 = texto2.get_rect(topleft=(20, 20))
        tela.blit(texto, textrect)
        tela.blit(texto2, textrect2)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = fundo.get_width()
        tela.blit(fundo, (x_pos_bg, y_pos_bg))
        tela.blit(fundo, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            x_pos_bg = 0
        x_pos_bg -= vel_jogo

    while funcionar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                funcionar = False

        tela.fill((255, 255, 255))
        input = pygame.key.get_pressed()

        player.draw(tela)
        player.update(input)
        if pontos%3000 == 0:
            obstacles = []
            boss.derrotado = False
            pygame.mixer.music.load("Assets/Sounds/i_r_tacos.mp3")
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(0.5)
        if not boss.derrotado:
            boss.update(tela, player)

            # Verifica colisão entre projéteis do jogador e o boss
            for proj in player.projeteis:
                if proj.rect.colliderect(boss.rect):
                    boss.levar_dano(1)
                    player.projeteis.remove(proj)

        if boss.derrotado or not boss.rect.x < largura_tela:  # Boss não está na tela
            if len(obstacles) == 0:
                if random.randint(0, 4) == 0:
                    obstacles.append(SmallCactus(cactus_pequeno))
                elif random.randint(0, 4) == 1:
                    obstacles.append(LargeCactus(cactus_grande))
                elif random.randint(0, 4) == 2:
                    obstacles.append(Bird(pterodatilo))
                elif random.randint(0, 4) == 3:
                    obstacles.append(Espinho(espinho))
                elif random.randint(0, 4) == 4:
                    obstacles.append(Parede(parede))

        for obstacle in obstacles:
            obstacle.draw(tela)
            obstacle.update()

            # Detecta a colisão entre o dinossauro e o obstáculo
            if player.dino_rect.colliderect(obstacle.rect):
                pygame.mixer.music.stop()
                som_morte.play()
                player.morrer()  # Chama o método morrer do dinossauro

        # Verifica colisão entre o jogador e os ataques do boss
        for ataque in boss.ataques:
            if ataque.rect.colliderect(player.dino_rect):
                pygame.mixer.music.stop()
                oof.play()
                player.morrer()  # Chama o método morrer do dinossauro

        # Verifica se o obstáculo é uma Parede
        for obstacle in obstacles:
            if isinstance(obstacle, Parede):
                # Verifica se algum projétil colide com a parede
                for proj in player.projeteis:
                    if proj.rect.colliderect(obstacle.rect):
                        obstacles.remove(obstacle)  # Remove a parede ao ser atingida
                        player.projeteis.remove(proj)  # Remove o projétil após a colisão

        Nuvem.draw(tela)
        Nuvem.update()

       
       

        background()
        pontuacao()

        relogio.tick(30)
        pygame.display.update()

def m_skins():
    global maior_pontuacao, skin
    funciona = True
    fonte_maior = pygame.font.Font('Minecraft.ttf', 20)
    fonte_menor = pygame.font.Font('Minecraft.ttf', 15)
    if os.path.exists("pontos.txt"):
            with open("pontos.txt", "r") as file:
                maior_pontuacao = int(file.read())
    if os.path.exists("mortes.txt"):
            file = open("mortes.txt", "r")
            for p in file.readlines():
                mortes = int(p)
            file.close()
    print(mortes)
    while funciona:
        tela.fill((255,255,255))

        if skin == 0:
            nor_sel = 1
        else:
            nor_sel = 0
        if maior_pontuacao >= 1000:
            if skin == 1:
                emo_sel = 1
            else:
                emo_sel = 0
        else:
            emo_sel = 2
        if maior_pontuacao >= 2000:
            if skin == 2:
                inv_sel = 1
            else:
                inv_sel = 0
        else:
            inv_sel = 2
        if maior_pontuacao >= 4000:
            if skin == 3:
                niver_sel = 1
            else:
                niver_sel = 0
        else:
            niver_sel = 2

        if maior_pontuacao >= 7000:
            if skin == 4:
                dino_sel = 1
            else:
                dino_sel = 0
        else:
            dino_sel = 2
        if mortes >= 100:
            if skin == 5:
                morte_sel = 1
            else:
                morte_sel = 0
        else:
            morte_sel = 2
        
        nor = b_normal[nor_sel]
        emoo = b_emo[emo_sel]
        inve = b_inv[inv_sel]
        niver = b_niver[niver_sel]
        dino = b_dino[dino_sel]
        morte = b_morte[morte_sel]



        titulo_normal = fonte_maior.render("Dinossario", True, (0, 0, 0))
        titulo_emo = fonte_maior.render("Emo", True, (0, 0, 0))
        titulo_invertido = fonte_maior.render("oirassoniD", True, (0, 0, 0))
        titulo_niver = fonte_maior.render("Aniversario", True, (0, 0, 0))
        titulo_dino = fonte_maior.render("Dino^2", True, (0, 0, 0))
        titulo_morte = fonte_maior.render("Morte", True, (0, 0, 0))

        

        texto_normal = fonte_menor.render("skin inicial", True, (0, 0, 0))
        texto_emo1 = fonte_menor.render("Atinja 1000 pontos", True, (0, 0, 0))
        texto_invertido1 = fonte_menor.render("Atinja 2000 pontos", True, (0, 0, 0))
        texto_niver1 = fonte_menor.render("Atinja 4000 pontos", True, (0, 0, 0))
        texto_dino1 = fonte_menor.render("Atinja 7000 pontos", True, (0, 0, 0))
        texto_morte1 = fonte_menor.render("Morra 100 vezes", True, (0, 0, 0))
        texto_emo2 = fonte_menor.render("para desbloquear", True, (0, 0, 0))
        texto_invertido2 = fonte_menor.render("para desbloquear", True, (0, 0, 0))
        texto_niver2 = fonte_menor.render("para desbloquear", True, (0, 0, 0))
        texto_dino2 = fonte_menor.render("para desbloquear", True, (0, 0, 0))
        texto_morte2 = fonte_menor.render("para desbloquear", True, (0, 0, 0))

        normal_rect_t = titulo_normal.get_rect(center=(largura_tela // 4, altura_tela // 3.6))
        emo_rect_t = titulo_emo.get_rect(center=(largura_tela // 2, altura_tela // 3.6))
        inver_rect_t = titulo_invertido.get_rect(center=(largura_tela // 1.3, altura_tela // 3.6))
        niver_rect_t = titulo_niver.get_rect(center=(largura_tela // 4, altura_tela // 1.25))
        dino_rect_t = titulo_dino.get_rect(center=(largura_tela // 2, altura_tela // 1.25))
        morte_rect_t = titulo_morte.get_rect(center=(largura_tela // 1.3, altura_tela // 1.25))
        
        normal_rect_te = texto_normal.get_rect(center=(largura_tela // 4, altura_tela // 3))
        emo_rect_te1 = texto_emo1.get_rect(center=(largura_tela // 2, altura_tela // 3))
        inver_rect_te1 = texto_invertido1.get_rect(center=(largura_tela // 1.3, altura_tela // 3))
        niver_rect_te1 = texto_niver1.get_rect(center=(largura_tela // 4, altura_tela // 1.15))
        dino_rect_te1 = texto_dino1.get_rect(center=(largura_tela // 2, altura_tela // 1.15))
        morte_rect_te1 = texto_morte1.get_rect(center=(largura_tela // 1.3, altura_tela // 1.15))
        emo_rect_te2 = texto_emo2.get_rect(center=(largura_tela // 2, altura_tela // 2.7))
        inver_rect_te2 = texto_invertido2.get_rect(center=(largura_tela // 1.3, altura_tela // 2.7))
        niver_rect_te2 = texto_niver2.get_rect(center=(largura_tela // 4, altura_tela // 1.1))
        dino_rect_te2 = texto_dino2.get_rect(center=(largura_tela // 2, altura_tela // 1.1))
        morte_rect_te2 = texto_morte2.get_rect(center=(largura_tela // 1.3, altura_tela // 1.1))

        normal_rect = nor.get_rect(center=(largura_tela // 4, altura_tela // 4))
        emo_rect = emoo.get_rect(center=(largura_tela // 2, altura_tela // 4))
        inver_rect = inve.get_rect(center=(largura_tela // 1.3, altura_tela // 4))
        niver_rect = niver.get_rect(center=(largura_tela // 4, altura_tela // 1.3))
        dino_rect = dino.get_rect(center=(largura_tela // 2, altura_tela // 1.3))
        morte_rect = dino.get_rect(center=(largura_tela // 1.3, altura_tela // 1.3))
        

        # Desenha os botões na tela

        tela.blit(nor, normal_rect)
        tela.blit(emoo, emo_rect)
        tela.blit(inve, inver_rect)
        tela.blit(niver, niver_rect)
        tela.blit(dino, dino_rect)
        tela.blit(morte, morte_rect)

        tela.blit(titulo_normal, normal_rect_t)
        tela.blit(titulo_emo, emo_rect_t)
        tela.blit(titulo_invertido, inver_rect_t)
        tela.blit(titulo_niver, niver_rect_t)
        tela.blit(titulo_dino, dino_rect_t)
        tela.blit(titulo_morte, morte_rect_t)
        
        tela.blit(texto_normal, normal_rect_te)
        tela.blit(texto_emo1, emo_rect_te1)
        tela.blit(texto_invertido1, inver_rect_te1)
        tela.blit(texto_niver1, niver_rect_te1)
        tela.blit(texto_dino1, dino_rect_te1)
        tela.blit(texto_morte1, morte_rect_te1)
        tela.blit(texto_emo2, emo_rect_te2)
        tela.blit(texto_invertido2, inver_rect_te2)
        tela.blit(texto_niver2, niver_rect_te2)
        tela.blit(texto_dino2, dino_rect_te2)
        tela.blit(texto_morte2, morte_rect_te2)

        # Atualiza a tela
        pygame.display.update()

        # Eventos do menu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                funciona = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()


                if normal_rect.collidepoint(mouse_pos):
                    skin = 0  # Seleciona a skin normal
                    print("Skin normal selecionada!")
                    
                    
                if not emo_sel ==2:
                    if emo_rect.collidepoint(mouse_pos):
                        skin = 1  # Seleciona a skin emo
                        print("Skin emo selecionada!") 
                        
                    
                if not inv_sel == 2:
                    if inver_rect.collidepoint(mouse_pos):
                        skin = 2  # Seleciona a skin invertida
                        print("Skin invertida selecionada!")
                
                if not niver_sel == 2:
                    if niver_rect.collidepoint(mouse_pos):
                        skin = 3  # Seleciona a skin invertida
                        print("Skin aniversario selecionada!")
                if not dino_sel == 2:
                    if dino_rect.collidepoint(mouse_pos):
                        skin = 4  # Seleciona a skin invertida
                        print("Skin dino^2 selecionada!")
                if not morte_sel == 2:
                    if morte_rect.collidepoint(mouse_pos):
                        skin = 5  # Seleciona a skin invertida
                        print("Skin morte selecionada!")
                    

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Volta ao menu principal ao pressionar ESC
                    funciona = False
                    menu(0)

def menu(death_count):
    global pontos
    run = True
    while run:
        tela.fill((255, 255, 255))
        font = pygame.font.Font('Minecraft.ttf', 50)
        f_menor = pygame.font.Font('Minecraft.ttf', 20)

        # Coordenadas e dimensões dos botões
        botao_jogar_rect = b_jogar.get_rect(center=(largura_tela - 400, altura_tela // 2 + 50))
        botao_skins_rect = b_skins.get_rect(center=(largura_tela - 700, altura_tela // 2 + 50))
        botao_menu_rect = b_menu.get_rect(center=(largura_tela // 2, altura_tela // 2 + 100))

        if death_count == 0:
            # Menu inicial
            text = font.render("DINOSSARIO", True, (0, 0, 0))
            textRect = text.get_rect(center=(largura_tela // 2, altura_tela // 2 - 150))
            tela.blit(text, textRect)
            tela.blit(b_jogar, botao_jogar_rect)
            tela.blit(b_skins, botao_skins_rect)
        else:
            # Menu de morte
            text = font.render("Voce morreu!", True, (0, 0, 0))
            score = font.render(f"Seus pontos: {pontos}", True, (0, 0, 0))
            info = f_menor.render("Aperte qualquer botao para tentar de novo", True, (0, 0, 0))
            textRect = text.get_rect(center=(largura_tela // 2, altura_tela // 2 - 100))
            scoreRect = score.get_rect(center=(largura_tela // 2, altura_tela // 2 - 20))
            infoRect = info.get_rect(center=(largura_tela // 2, altura_tela - 40))
            tela.blit(text, textRect)
            tela.blit(score, scoreRect)
            tela.blit(info, infoRect)
            tela.blit(b_menu, botao_menu_rect)

        # Atualizar a tela
        pygame.display.update()

        # Eventos do menu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                run = False
            
            if death_count > 0 and event.type == pygame.KEYDOWN:
                main()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                # Botão Jogar
                if death_count == 0 and botao_jogar_rect.collidepoint(mouse_pos):
                    main()

                # Botão Skins
                if death_count == 0 and botao_skins_rect.collidepoint(mouse_pos):
                    m_skins()

                # Botão Menu
                if death_count > 0 and botao_menu_rect.collidepoint(mouse_pos):
                    death_count = 0  # Reseta o contador de mortes para voltar ao menu inicial
menu(0)