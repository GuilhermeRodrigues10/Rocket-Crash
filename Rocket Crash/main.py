import pygame
import random

pygame.init()

### criação de tela ###
screen = pygame.display.set_mode([700, 497])
pygame.display.set_caption("Rocket Crash")
### criação de tela ###

### frame por segundo ###
clock = pygame.time.Clock()
### frame por segundo ###

## imagens e sons ##
img_player = pygame.image.load('img/player.png')
img_wallo = pygame.image.load('img/planeta.png')
img_bg1 = pygame.image.load('img/bg.jpg')
img_bg2 = pygame.image.load('img/bg.jpg')
img_logo = pygame.image.load('img/intro.png')
img_start = pygame.image.load('img/rocket_intro.png')
img_gameover = pygame.image.load('img/rocket_over.png')
img_meter = pygame.image.load('img/img_meter.png')
hit = pygame.mixer.Sound('sounds/crash.wav')
## imagens e sons ##


## funcao para desenhar o foguete ##
def player(player_area):
    #pygame.draw.rect(screen, [0,0,0], player_area)
    screen.blit(img_player,player_area)

## funcao para desenhar os planetas ##
def wall(wallo):
    #pygame.draw.rect(screen, [0,0,0], wallo)
    screen.blit(img_wallo, [wall_locx,wall_alt])

## funcao para desenhar os meteoros ##
def meteoro(meter):
    screen.blit(img_meter, [locx, alt])

## funcao para desenhar os pontos ##
def score(points):
    font = pygame.font.Font('fonts/geo.ttf', 55)
    text = font.render(str(points), True, [255,255,255])
    screen.blit(text, [350,20])

## funcao para a tela de introducao ##
def intro():
    screen.fill([255, 255, 255])
    screen.blit(img_logo, [40, 320])
    screen.blit(img_start, [170, 100])
    font = pygame.font.Font('fonts/geo.ttf', 20)
    text = font.render("W para cima e S para baixo", True, [0,0,0])
    text2 = font.render("Instruções", True, [0,0,0])
    screen.blit(text, [200,30])
    screen.blit(text2,[290,0])
    pygame.display.update()
    pygame.time.wait(4000)

## variaveis ##
close = False

## variaveis da posicao do foguete ##
playerx = 150
playery = 250
speed = 1

## variaveis para posicao do planeta ##
wall_locx = 700
wall_larg = 50
wall_alt = playery
speedwall = 12

## variaveis para posicao do meteoro ##
locx = 3000
larg = 50
alt = random.randint(50, 350)
speed_meteor = 18

## variaveis da pontuacao ##
points = 0

## variaveis para bg ##
Img = 1320
posImg = 0

## variaveis para delimitar a tela ##
up = 0
down = 450

## variavel para quando perder ##
gameover = False

## variavel para armazenar o recorde ##
recorde = -1

## chamada da introducao ##
intro()

##loop para manter a janela aberta e fechar quando necessário. essencial par ao jogo##
while not close:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close = True
        if event.type == pygame.KEYDOWN:
            ## manten o foguete para cima e para baixo ##
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                speed = -4

            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                speed = 4


    ### background - branco  ###
    #screen.fill([255,255,255])
    screen.blit(img_bg1, (posImg, 0))
    screen.blit(img_bg2, (posImg + Img, 0))
    posImg -= 2  # Velocidade
    if posImg * -1 == Img:  # Recomeçar
        posImg = 0

    ## desenho do jogador ##
    player_area = pygame.Rect(playerx, playery, 45, 45)
    player(player_area)
    playery += speed

    ## desenho dos planetas ##
    wallo = pygame.Rect(wall_locx, wall_alt, wall_larg, 50)
    wall(wallo)


    ## deslocamento dos planetas ##
    wall_locx -= speedwall

    if wall_locx < -30:
        wall_locx = 700
        wall_alt = playery

    ## deslocamento dos planetas ##

    ## desenho dos meteoros ##
    meter = pygame.Rect(locx, alt, larg, 50)
    meteoro(meter)

    ## deslocamento dos meteoros ##
    locx -= speed_meteor

    ## deslocamento dos meteoros ##
    if locx < -30:
        locx = 3000
        alt = random.randint(50, 350)

    ## chamada para os pontos ##
    score(points)


    ## soma da pontuacao ##
    if playerx == wall_locx + wall_larg:
        points += 1

    if playerx == locx + larg:
        points += 1

    ## deteccao de colisao ##
    if (playery > down or playery < up):
        hit.play()
        speed = 0
        speedwall = 0
        gameover = True
        if points > recorde:
            recorde = points

    ## deteccao de colisao ##
    if player_area.colliderect(wallo) or player_area.colliderect(meter):
        hit.play()
        speed = 0
        speedwall = 0
        gameover = True
        if points > recorde:
            recorde = points





    ## atualiza o fundo do jogo ##
    pygame.display.flip()
    clock.tick(60)
    ## atualiza o fundo do jogo ##

    ## chamada para gameover ##
    while gameover:
        pygame.time.wait(300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True
                gameover = False
            # Apertar uma tecla
            if event.type == pygame.KEYDOWN:
                # Aperta Tecla "espaço"
                if event.key == pygame.K_SPACE:
                    playerx = 150
                    playery = 250

                    speed = 1

                    wall_locx = 800
                    wall_larg = 50
                    wall_alt = playery
                    speedwall = 12

                    locx = 3000
                    larg = 50
                    alt = random.randint(0, 350)
                    speed_meteor = 18

                    if points > recorde:
                        recorde = points

                    points = 0

                    gameover = False

        ## Imagem game over ##
        screen.fill([255, 255, 255])
        screen.blit(img_gameover, (170, 130))
        font = pygame.font.Font('fonts/geo.ttf', 40)
        font2 = pygame.font.Font('fonts/geo.ttf', 28)
        text = font.render(str(points), True, [238, 37, 79])
        text3 = font.render("Sua Pontuação: ", True, [238, 37, 79])
        text5 = font.render("Seu Recorde: ", True, [238, 37, 79])
        text4 = font2.render("Pressione espaço para jogar novamente!", True, [238,37,79])
        recorde1 = font.render(str(recorde), True, [238, 37, 79])
        screen.blit(text, [500, 43])
        screen.blit(text3, [155, 43])
        screen.blit(text4, [50, 400])
        screen.blit(recorde1, [500, 340])
        screen.blit(text5, [150, 340])

        pygame.display.flip()


pygame.quit()
