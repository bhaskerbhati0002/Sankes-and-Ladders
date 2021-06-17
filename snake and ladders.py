import pygame
import random

pygame.init()
screen_width = 700
screen_height = 500

def text_screen(text, color, x, y, size):
    screen_text = (pygame.font.SysFont(None, size)).render(text, True, color)
    gamewindow.blit(screen_text, [x,y])

#colors
red=(255,0,0)
green = (0,255,0)
cyan = (0,255,255)
black = (0,0,0)
white = (255,255,255)
yellow = (255,255,0)
blue = (0,0,255)
orange = (255,150,0)
pink = (255,150,150)
grey = (128,128,128)

gamewindow = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("snakes and ladders")
pygame.draw.rect(gamewindow, white, [500, 0, 200, 500])
pygame.draw.rect(gamewindow, cyan, [550, 150, 100, 100])
pygame.draw.circle(gamewindow, grey, [550, 350], 25)
pygame.draw.circle(gamewindow, grey, [650, 350], 25)

#sounds
die_roll=pygame.mixer.Sound("snake assets/audio/die roll.mp3")
snake_eat=pygame.mixer.Sound("snake assets/audio/snake eating.mp3")
ladder_climb=pygame.mixer.Sound("snake assets/audio/ladder climb.wav")
game_win=pygame.mixer.Sound("snake assets/audio/game win.wav")

#snakes, tokens, logo, images
logo = pygame.image.load("snake assets/logo.PNG")
arrow=pygame.image.load("snake assets/arrow.png")
token_g=pygame.image.load("snake assets/greentoken.png")
token_r=pygame.image.load("snake assets/redtoken.png")
snake1=pygame.image.load("snake assets/snakes/s1-cutout.png")
snake2=pygame.image.load("snake assets/snakes/s2-cutout.png")
snake3=pygame.image.load("snake assets/snakes/s3-cutout.png")
snake3=pygame.transform.flip(snake3,True,False)
snake6=pygame.image.load("snake assets/snakes/s6-cutout.png")

#ladders
brownladder=pygame.image.load("snake assets/ladders/l1-cutout.png")
redladder=pygame.image.load("snake assets/ladders/l2-cutout.png")
ladder1=pygame.transform.rotate(brownladder,45)
ladder3=pygame.transform.rotate(redladder,-27)
ladder4=pygame.image.load("snake assets/ladders/l4-cutout.png")

#variables
dictionary={4900:150, 4250:500 , 3900: 2000, 2300:350, 300:1800, 1000:2000, 2550:3550, 2750:4650}
exit_game = False
ch=0
ch_1=0
ch_2=0
pos1=0
pos2=0

gamewindow.blit(logo, [500, 10])
for i in range(10):
    x = 10
    y = 465
    if i % 2 == 0:
        pygame.draw.rect(gamewindow, (255, 255, 255), [i * 50, 450, 50, 50])
        text_screen(str(i + 1), black, x + i * 50, y, 40)
    else:
        pygame.draw.rect(gamewindow, pink, [i * 50, 450, 50, 50])
        text_screen(str(i + 1), black, x + i * 50, y, 40)
for i in range(10, 20):
    x = 10
    y = 415
    a = i % 10
    if a % 2 == 0:
        pygame.draw.rect(gamewindow, (255, 255, 255), [450 - a * 50, 400, 50, 50])
        text_screen(str(i + 1), black, x + (450 - a * 50), y, 40)
    else:
        pygame.draw.rect(gamewindow, (255, 150, 150), [450 - a * 50, 400, 50, 50])
        text_screen(str(i + 1), black, x + (450 - a * 50), y, 40)

for i in range(20, 30):
    x = 10
    y = 365
    a = i % 10
    if a % 2 == 0:
        pygame.draw.rect(gamewindow, (255, 255, 255), [a * 50, 350, 50, 50])
        text_screen(str(i + 1), black, x + a * 50, y, 40)
    else:
        pygame.draw.rect(gamewindow, (255, 150, 150), [a * 50, 350, 50, 50])
        text_screen(str(i + 1), black, x + a * 50, y, 40)
for i in range(30, 40):
    x = 10
    y = 315
    a = i % 10
    if a % 2 == 0:
        pygame.draw.rect(gamewindow, (255, 255, 255), [450 - a * 50, 300, 50, 50])
        text_screen(str(i + 1), black, x + (450 - a * 50), y, 40)
    else:
        pygame.draw.rect(gamewindow, (255, 150, 150), [450 - a * 50, 300, 50, 50])
        text_screen(str(i + 1), black, x + (450 - a * 50), y, 40)
for i in range(40, 50):
    x = 10
    y = 265
    a = i % 10
    if a % 2 == 0:
        pygame.draw.rect(gamewindow, (255, 255, 255), [a * 50, 250, 50, 50])
        text_screen(str(i + 1), black, x + a * 50, y, 40)
    else:
        pygame.draw.rect(gamewindow, (255, 150, 150), [a * 50, 250, 50, 50])
        text_screen(str(i + 1), black, x + a * 50, y, 40)
for i in range(50, 60):
    x = 10
    y = 215
    a = i % 10
    if a % 2 == 0:
        pygame.draw.rect(gamewindow, (255, 255, 255), [450 - a * 50, 200, 50, 50])
        text_screen(str(i + 1), black, x + (450 - a * 50), y, 40)
    else:
        pygame.draw.rect(gamewindow, (255, 150, 150), [450 - a * 50, 200, 50, 50])
        text_screen(str(i + 1), black, x + (450 - a * 50), y, 40)
for i in range(60, 70):
    x = 10
    y = 165
    a = i % 10
    if a % 2 == 0:
        pygame.draw.rect(gamewindow, (255, 255, 255), [a * 50, 150, 50, 50])
        text_screen(str(i + 1), black, x + a * 50, y, 40)
    else:
        pygame.draw.rect(gamewindow, (255, 150, 150), [a * 50, 150, 50, 50])
        text_screen(str(i + 1), black, x + a * 50, y, 40)
for i in range(70, 80):
    x = 10
    y = 115
    a = i % 10
    if a % 2 == 0:
        pygame.draw.rect(gamewindow, (255, 255, 255), [450 - a * 50, 100, 50, 50])
        text_screen(str(i + 1), black, x + (450 - a * 50), y, 40)
    else:
        pygame.draw.rect(gamewindow, (255, 150, 150), [450 - a * 50, 100, 50, 50])
        text_screen(str(i + 1), black, x + (450 - a * 50), y, 40)
for i in range(80, 90):
    x = 10
    y = 65
    a = i % 10
    if a % 2 == 0:
        pygame.draw.rect(gamewindow, (255, 255, 255), [a * 50, 50, 50, 50])
        text_screen(str(i + 1), black, x + a * 50, y, 40)
    else:
        pygame.draw.rect(gamewindow, (255, 150, 150), [a * 50, 50, 50, 50])
        text_screen(str(i + 1), black, x + a * 50, y, 40)
for i in range(90, 100):
    x = 5
    y = 15
    a = i % 10
    if a % 2 == 0:
        pygame.draw.rect(gamewindow, (255, 255, 255), [450 - a * 50, 0, 50, 50])
        text_screen(str(i + 1), black, x + (450 - a * 50), y, 40)
    else:
        pygame.draw.rect(gamewindow, (255, 150, 150), [450 - a * 50, 0, 50, 50])
        text_screen(str(i + 1), black, x + (450 - a * 50), y, 40)

gamewindow.blit(snake1,[20,100])
gamewindow.blit(snake2,[250,45])
gamewindow.blit(snake3,[80,20])
gamewindow.blit(snake6,[320,250])
gamewindow.blit(ladder1,[170,320])
gamewindow.blit(ladder4,[5,280])
gamewindow.blit(ladder3,[200,5])
gamewindow.blit(ladder4,[405,130])



def play(ch,a,ch_1,ch_2,pos1,pos2):
    gamewindow.blit(logo, [500, 10])
    for i in range(10):
        x = 10
        y = 465
        if i % 2 == 0:
            pygame.draw.rect(gamewindow, (255, 255, 255), [i * 50, 450, 50, 50])
            text_screen(str(i + 1), black, x + i * 50, y, 40)
        else:
            pygame.draw.rect(gamewindow, pink, [i * 50, 450, 50, 50])
            text_screen(str(i + 1), black, x + i * 50, y, 40)
    for i in range(10, 20):
        x = 10
        y = 415
        a = i % 10
        if a % 2 == 0:
            pygame.draw.rect(gamewindow, (255, 255, 255), [450 - a * 50, 400, 50, 50])
            text_screen(str(i + 1), black, x + (450 - a * 50), y, 40)
        else:
            pygame.draw.rect(gamewindow, (255, 150, 150), [450 - a * 50, 400, 50, 50])
            text_screen(str(i + 1), black, x + (450 - a * 50), y, 40)

    for i in range(20, 30):
        x = 10
        y = 365
        a = i % 10
        if a % 2 == 0:
            pygame.draw.rect(gamewindow, (255, 255, 255), [a * 50, 350, 50, 50])
            text_screen(str(i + 1), black, x + a * 50, y, 40)
        else:
            pygame.draw.rect(gamewindow, (255, 150, 150), [a * 50, 350, 50, 50])
            text_screen(str(i + 1), black, x + a * 50, y, 40)
    for i in range(30, 40):
        x = 10
        y = 315
        a = i % 10
        if a % 2 == 0:
            pygame.draw.rect(gamewindow, (255, 255, 255), [450 - a * 50, 300, 50, 50])
            text_screen(str(i + 1), black, x + (450 - a * 50), y, 40)
        else:
            pygame.draw.rect(gamewindow, (255, 150, 150), [450 - a * 50, 300, 50, 50])
            text_screen(str(i + 1), black, x + (450 - a * 50), y, 40)
    for i in range(40, 50):
        x = 10
        y = 265
        a = i % 10
        if a % 2 == 0:
            pygame.draw.rect(gamewindow, (255, 255, 255), [a * 50, 250, 50, 50])
            text_screen(str(i + 1), black, x + a * 50, y, 40)
        else:
            pygame.draw.rect(gamewindow, (255, 150, 150), [a * 50, 250, 50, 50])
            text_screen(str(i + 1), black, x + a * 50, y, 40)
    for i in range(50, 60):
        x = 10
        y = 215
        a = i % 10
        if a % 2 == 0:
            pygame.draw.rect(gamewindow, (255, 255, 255), [450 - a * 50, 200, 50, 50])
            text_screen(str(i + 1), black, x + (450 - a * 50), y, 40)
        else:
            pygame.draw.rect(gamewindow, (255, 150, 150), [450 - a * 50, 200, 50, 50])
            text_screen(str(i + 1), black, x + (450 - a * 50), y, 40)
    for i in range(60, 70):
        x = 10
        y = 165
        a = i % 10
        if a % 2 == 0:
            pygame.draw.rect(gamewindow, (255, 255, 255), [a * 50, 150, 50, 50])
            text_screen(str(i + 1), black, x + a * 50, y, 40)
        else:
            pygame.draw.rect(gamewindow, (255, 150, 150), [a * 50, 150, 50, 50])
            text_screen(str(i + 1), black, x + a * 50, y, 40)
    for i in range(70, 80):
        x = 10
        y = 115
        a = i % 10
        if a % 2 == 0:
            pygame.draw.rect(gamewindow, (255, 255, 255), [450 - a * 50, 100, 50, 50])
            text_screen(str(i + 1), black, x + (450 - a * 50), y, 40)
        else:
            pygame.draw.rect(gamewindow, (255, 150, 150), [450 - a * 50, 100, 50, 50])
            text_screen(str(i + 1), black, x + (450 - a * 50), y, 40)
    for i in range(80, 90):
        x = 10
        y = 65
        a = i % 10
        if a % 2 == 0:
            pygame.draw.rect(gamewindow, (255, 255, 255), [a * 50, 50, 50, 50])
            text_screen(str(i + 1), black, x + a * 50, y, 40)
        else:
            pygame.draw.rect(gamewindow, (255, 150, 150), [a * 50, 50, 50, 50])
            text_screen(str(i + 1), black, x + a * 50, y, 40)
    for i in range(90, 100):
        x = 5
        y = 15
        a = i % 10
        if a % 2 == 0:
            pygame.draw.rect(gamewindow, (255, 255, 255), [450 - a * 50, 0, 50, 50])
            text_screen(str(i + 1), black, x + (450 - a * 50), y, 40)
        else:
            pygame.draw.rect(gamewindow, (255, 150, 150), [450 - a * 50, 0, 50, 50])
            text_screen(str(i + 1), black, x + (450 - a * 50), y, 40)

    gamewindow.blit(snake1, [20, 100])
    gamewindow.blit(snake2, [250, 45])
    gamewindow.blit(snake3, [80, 20])
    gamewindow.blit(snake6, [320, 250])
    gamewindow.blit(ladder1, [170, 320])
    gamewindow.blit(ladder4, [5, 280])
    gamewindow.blit(ladder3, [200, 5])
    gamewindow.blit(ladder4, [405, 130])

    if ch_1==1 and (ch%2!=0):
        if (pos1<=450):
            gamewindow.blit(token_r, [pos1, 450])

        elif (450<pos1<=950):
            gamewindow.blit(token_r, [950-pos1, 400])

        elif (950<pos1<=1450):
            gamewindow.blit(token_r, [pos1-1000,350])

        elif (1450<pos1<=1950):
            gamewindow.blit(token_r, [1950-pos1, 300])

        elif (1950 < pos1 <= 2450):
            gamewindow.blit(token_r, [pos1-2000, 250])

        elif (2450 < pos1 <= 2950):
            gamewindow.blit(token_r, [2950 - pos1, 200])

        elif (2950<pos1<=3450):
            gamewindow.blit(token_r, [pos1-3000,150])

        elif (3450<pos1<=3950):
            gamewindow.blit(token_r, [3950-pos1, 100])

        elif (3950 < pos1 <= 4450):
            gamewindow.blit(token_r, [pos1-4000, 50])

        elif (4450 < pos1 <= 4950):
            gamewindow.blit(token_r, [4950 - pos1, 0])


    if ch_2 == 1 and (ch % 2 == 0):
        if (pos2<=450):
            gamewindow.blit(token_g, [pos2, 450])

        elif (450<pos2<=950):
            gamewindow.blit(token_g, [950-pos2, 400])

        elif (950<pos2<=1450):
            gamewindow.blit(token_g, [pos2-1000,350])

        elif (1450<pos2<=1950):
            gamewindow.blit(token_g, [1950-pos2, 300])

        elif (1950 < pos2 <= 2450):
            gamewindow.blit(token_g, [pos2-2000, 250])

        elif (2450 < pos2 <= 2950):
            gamewindow.blit(token_g, [2950 - pos2, 200])

        elif (2950<pos2<=3450):
            gamewindow.blit(token_g, [pos2-3000,150])

        elif (3450<pos2<=3950):
            gamewindow.blit(token_g, [3950-pos2, 100])

        elif (3950 < pos2 <= 4450):
            gamewindow.blit(token_g, [pos2-4000, 50])

        elif (4450 < pos2 <= 4950):
            gamewindow.blit(token_g, [4950 - pos2, 0])

    if ch_1>1 and ch%2!=0:
        if (pos1 <= 450):
            gamewindow.blit(token_r, [pos1, 450])

        elif (450 < pos1 <= 950):
            gamewindow.blit(token_r, [950 - pos1, 400])

        elif (950 < pos1 <= 1450):
            gamewindow.blit(token_r, [pos1 - 1000, 350])

        elif (1450 < pos1 <= 1950):
            gamewindow.blit(token_r, [1950 - pos1, 300])

        elif (1950 < pos1 <= 2450):
            gamewindow.blit(token_r, [pos1 - 2000, 250])

        elif (2450 < pos1 <= 2950):
            gamewindow.blit(token_r, [2950 - pos1, 200])

        elif (2950 < pos1 <= 3450):
            gamewindow.blit(token_r, [pos1 - 3000, 150])

        elif (3450 < pos1 <= 3950):
            gamewindow.blit(token_r, [3950 - pos1, 100])

        elif (3950 < pos1 <= 4450):
            gamewindow.blit(token_r, [pos1 - 4000, 50])

        elif (4450 < pos1 <= 4950):
            gamewindow.blit(token_r, [4950 - pos1, 0])



    if ch_2>1 and ch%2==0:
        if (pos2 <= 450):
            gamewindow.blit(token_g, [pos2, 450])

        elif (450 < pos2 <= 950):
            gamewindow.blit(token_g, [950 - pos2, 400])

        elif (950 < pos2 <= 1450):
            gamewindow.blit(token_g, [pos2 - 1000, 350])

        elif (1450 < pos2 <= 1950):
            gamewindow.blit(token_g, [1950 - pos2, 300])

        elif (1950 < pos2 <= 2450):
            gamewindow.blit(token_g, [pos2 - 2000, 250])

        elif (2450 < pos2 <= 2950):
            gamewindow.blit(token_g, [2950 - pos2, 200])

        elif (2950 < pos2 <= 3450):
            gamewindow.blit(token_g, [pos2 - 3000, 150])

        elif (3450 < pos2 <= 3950):
            gamewindow.blit(token_g, [3950 - pos2, 100])

        elif (3950 < pos2 <= 4450):
            gamewindow.blit(token_g, [pos2 - 4000, 50])

        elif (4450 < pos2 <= 4950):
            gamewindow.blit(token_g, [4950 - pos2, 0])


def opener(a,ch,ch_1,ch_2,pos1,pos2):

    if ch_1==1:
        if ch % 2 != 0:
            pygame.draw.circle(gamewindow, red, [550, 350], 25)

    if ch_2==1:
        if ch % 2 == 0:
            pygame.draw.circle(gamewindow, green, [650, 350], 25)

    play(ch,a,ch_1,ch_2, pos1,pos2)

def display_score(pos1,pos2,ch_1,ch_2):
    pygame.draw.rect(gamewindow,white,[500,400,200,100])
    if ch_1>=1:
        text_screen(str(pos1//50+1),red,530,400,50)
    if ch_2>=1:
        text_screen(str(pos2//50+1), green, 630, 400, 50)

def dice(x,y,ch,a, ch_1,ch_2,pos1,pos2):
    if (550<x<650 and 150<y<250):

        pygame.draw.rect(gamewindow, cyan, [550, 150, 100, 100])

        if a==1:
            text_screen("•", black, 588, 165, 100)
        if a==2:
            text_screen("•", black, 615, 140, 100)
            text_screen("•", black, 565, 190, 100)

        if a==3:
            text_screen("•", black, 615, 135, 100)
            text_screen("•", black, 565, 190, 100)
            text_screen("•", black, 590, 163, 100)

        if a==4:
            text_screen("•", black, 615, 140, 100)
            text_screen("•", black, 565, 190, 100)
            text_screen("•", black, 565, 140, 100)
            text_screen("•", black, 615, 190, 100)

        if a==5:
            text_screen("•", black, 615, 140, 100)
            text_screen("•", black, 565, 190, 100)
            text_screen("•", black, 565, 140, 100)
            text_screen("•", black, 615, 190, 100)
            text_screen("•", black, 590, 165, 100)

        if a==6:
            text_screen("•", black, 615, 140, 100)
            text_screen("•", black, 565, 190, 100)
            text_screen("•", black, 565, 140, 100)
            text_screen("•", black, 615, 190, 100)
            text_screen("•", black, 615, 165, 100)
            text_screen("•", black, 565, 165, 100)

        opener(a,ch,ch_1,ch_2,pos1,pos2)

def win(pos1,pos2):

    if pos1==4950:
        game_win.play()
        while exit_game != True:
            gamewindow.fill(white)
            text_screen('"RED" token WIN.', red,200,200,50)
            text_screen('Thanks for playing.',red,190,250,50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
            pygame.display.update()

    if pos2==4950:
        game_win.play()
        while exit_game != True:
            gamewindow.fill(white)
            text_screen('"GREEN" token WIN.', green,170,200,50)
            text_screen('Thanks for playing.',red,190,250,50)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
            pygame.display.update()

def turn(ch):
    pygame.draw.rect(gamewindow,white,[500,251,200,70])
    if ch%2!=0:
        gamewindow.blit(arrow,[520,260])
        pygame.display.update()
    if ch % 2 == 0:
        gamewindow.blit(arrow,[620,260])
        pygame.display.update()

while exit_game!=True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit_game=True
        if event.type == pygame.MOUSEBUTTONDOWN:
            a=random.randint(1,6)
            (x, y) = pygame.mouse.get_pos()

            if a==6:
                if ch%2!=0:
                    ch_1=ch_1+1
                if ch%2==0:
                    ch_2=ch_2+1

            if ch_1==1 and (a==1 or a==2 or a==3 or a==4 or a==5) and ch%2!=0:

                if (4700<pos1<4950):
                    if pos1 == 4700:
                        if a == 6 and ch % 2 != 0:
                            pygame.draw.rect(gamewindow, (255, 255, 255), [250, 0, 50, 50])
                            text_screen(str(95), black, 255, 15, 40)
                            gamewindow.blit(ladder3, [200, 5])
                            gamewindow.blit(token_r, [270, 0])

                        else:
                            pos1 = pos1 + a * 50

                    if pos1 == 4750:
                        if (a == 5 or a == 6) and (ch % 2 != 0):
                            pygame.draw.rect(gamewindow, (255, 150, 150), [200, 0, 50, 50])
                            text_screen(str(96), black, 205, 15, 40)
                            gamewindow.blit(token_r, [220, 0])
                        else:
                            pos1 = pos1 + a * 50

                    if pos1 == 4800:
                        if (a == 4 or a == 5 or a == 6) and (ch % 2 != 0):
                            pygame.draw.rect(gamewindow, (255, 255, 255), [150, 0, 50, 50])
                            text_screen(str(97), black, 155, 15, 40)
                            gamewindow.blit(token_r, [170, 0])
                        else:
                            pos1 = pos1 + a * 50

                    if pos1 == 4850:
                        if (a == 3 or a == 4 or a == 5 or a == 6) and (ch % 2 != 0):
                            pygame.draw.rect(gamewindow, (255, 150, 150), [100, 0, 50, 50])
                            text_screen(str(98), black, 105, 15, 40)
                            gamewindow.blit(snake3, [80, 20])
                            gamewindow.blit(token_r, [120, 0])
                        else:
                            pos1 = pos1 + a * 50

                    if pos1 == 4900:
                        if (a == 2 or a == 3 or a == 4 or a == 5 or a == 6) and (ch % 2 != 0):
                            pygame.draw.rect(gamewindow, (255, 255, 255), [50, 0, 50, 50])
                            text_screen(str(99), black, 55, 15, 40)
                            gamewindow.blit(snake3, [80, 20])
                            gamewindow.blit(token_r, [70, 0])
                        else:
                            pos1 = pos1 + a * 50
                elif pos1==300:
                    ladder_climb.play()
                    pos1=dictionary[300]+a*50
                elif pos1==1000:
                    ladder_climb.play()
                    pos1=dictionary[1000]+a*50
                elif pos1==2550:
                    ladder_climb.play()
                    pos1=dictionary[2550]+a*50
                elif pos1==2750:
                    ladder_climb.play()
                    pos1=dictionary[2750]+a*50
                elif pos1==2300:
                    snake_eat.play()
                    pos1=dictionary[2300]+a*50
                elif pos1==3900:
                    snake_eat.play()
                    pos1=dictionary[3900]+a*50
                elif pos1==4250:
                    snake_eat.play()
                    pos1=dictionary[4250]+a*50
                elif pos1==4900:
                    snake_eat.play()
                    pos1=dictionary[4900]+a*50

                else:
                    pos1=pos1+a*50

            if ch_2==1 and (a==1 or a==2 or a==3 or a==4 or a==5) and ch%2==0:
                if (4700<pos2<4950):
                    if pos2 == 4700:
                        if a == 6 and ch % 2 == 0:
                            pygame.draw.rect(gamewindow, (255, 255, 255), [250, 0, 50, 50])
                            text_screen(str(95), black, 255, 15, 40)
                            gamewindow.blit(ladder3, [200, 5])
                            gamewindow.blit(token_g, [250, 0])
                        else:
                            pos2 = pos2 + a * 50

                    if pos2 == 4750:
                        if (a == 5 or a == 6) and (ch % 2 == 0):
                            pygame.draw.rect(gamewindow, (255, 150, 150), [200, 0, 50, 50])
                            text_screen(str(96), black, 205, 15, 40)
                            gamewindow.blit(token_g, [200, 0])
                        else:
                            pos2 = pos2 + a * 50

                    if pos2 == 4800:
                        if (a == 4 or a == 5 or a == 6) and (ch % 2 == 0):
                            pygame.draw.rect(gamewindow, (255, 255, 255), [150, 0, 50, 50])
                            text_screen(str(97), black, 155, 15, 40)
                            gamewindow.blit(token_g, [150, 0])
                        else:
                            pos2 = pos2 + a * 50

                    if pos2 == 4850:
                        if (a == 3 or a == 4 or a == 5 or a == 6) and (ch % 2 == 0):
                            pygame.draw.rect(gamewindow, (255, 150, 150), [100, 0, 50, 50])
                            text_screen(str(98), black, 105, 15, 40)
                            gamewindow.blit(snake3, [80, 20])
                            gamewindow.blit(token_g, [100, 0])
                        else:
                            pos2 = pos2 + a * 50

                    if pos2 == 4900:
                        if (a == 2 or a == 3 or a == 4 or a == 5 or a == 6) and (ch % 2 == 0):
                            pygame.draw.rect(gamewindow, (255, 255, 255), [50, 0, 50, 50])
                            text_screen(str(99), black, 55, 15, 40)
                            gamewindow.blit(snake3, [80, 20])
                            gamewindow.blit(token_g, [50, 0])
                        else:
                            pos2 = pos2 + a * 50
                elif pos2==300:
                    ladder_climb.play()
                    pos2=dictionary[300]+a*50
                elif pos2==1000:
                    ladder_climb.play()
                    pos2=dictionary[1000]+a*50
                elif pos2==2550:
                    ladder_climb.play()
                    pos2=dictionary[2550]+a*50
                elif pos2==2750:
                    ladder_climb.play()
                    pos2=dictionary[2750]+a*50
                elif pos2==2300:
                    snake_eat.play()
                    pos2=dictionary[2300]+a*50
                elif pos2==3900:
                    snake_eat.play()
                    pos2=dictionary[3900]+a*50
                elif pos2==4250:
                    snake_eat.play()
                    pos2=dictionary[4250]+a*50
                elif pos2==4900:
                    snake_eat.play()
                    pos2=dictionary[4900]+a*50

                else:
                    pos2=pos2+a*50

            if ch_1>1 and ch%2!=0:
                if (4700 < pos1 < 4950):
                    if pos1 == 4700:
                        if a == 6 and ch % 2 != 0:
                            pygame.draw.rect(gamewindow, (255, 255, 255), [250, 0, 50, 50])
                            text_screen(str(95), black, 255, 15, 40)
                            gamewindow.blit(ladder3, [200, 5])
                            gamewindow.blit(token_r, [270, 0])
                        else:
                            pos1 = pos1 + a * 50

                    if pos1 == 4750:
                        if (a == 5 or a == 6) and (ch % 2 != 0):
                            pygame.draw.rect(gamewindow, (255, 150, 150), [200, 0, 50, 50])
                            text_screen(str(96), black, 205, 15, 40)
                            gamewindow.blit(token_r, [220, 0])
                        else:
                            pos1 = pos1 + a * 50

                    if pos1 == 4800:
                        if (a == 4 or a == 5 or a == 6) and (ch % 2 != 0):
                            pygame.draw.rect(gamewindow, (255, 255, 255), [150, 0, 50, 50])
                            text_screen(str(97), black, 155, 15, 40)
                            gamewindow.blit(token_r, [170, 0])
                        else:
                            pos1 = pos1 + a * 50

                    if pos1 == 4850:
                        if (a == 3 or a == 4 or a == 5 or a == 6) and (ch % 2 != 0):
                            pygame.draw.rect(gamewindow, (255, 150, 150), [100, 0, 50, 50])
                            text_screen(str(98), black, 105, 15, 40)
                            gamewindow.blit(snake3, [80, 20])
                            gamewindow.blit(token_r, [120, 0])
                        else:
                            pos1 = pos1 + a * 50

                    if pos1 == 4900:
                        if (a == 2 or a == 3 or a == 4 or a == 5 or a == 6) and (ch % 2 != 0):
                            pygame.draw.rect(gamewindow, (255, 255, 255), [50, 0, 50, 50])
                            text_screen(str(99), black, 55, 15, 40)
                            gamewindow.blit(snake3, [80, 20])
                            gamewindow.blit(token_r, [70, 0])
                        else:
                            pos1 = pos1 + a * 50
                elif pos1==300:
                    ladder_climb.play()
                    pos1=dictionary[300]+a*50
                elif pos1==1000:
                    ladder_climb.play()
                    pos1=dictionary[1000]+a*50
                elif pos1==2550:
                    ladder_climb.play()
                    pos1=dictionary[2550]+a*50
                elif pos1==2750:
                    ladder_climb.play()
                    pos1=dictionary[2750]+a*50
                elif pos1==2300:
                    snake_eat.play()
                    pos1=dictionary[2300]+a*50
                elif pos1==3900:
                    snake_eat.play()
                    pos1=dictionary[3900]+a*50
                elif pos1==4250:
                    snake_eat.play()
                    pos1=dictionary[4250]+a*50
                elif pos1==4900:
                    snake_eat.play()
                    pos1=dictionary[4900]+a*50

                else:
                    pos1 = pos1 + a * 50

            if ch_2>1 and ch%2==0:
                if (4700 < pos2 < 4950):
                    if pos2 == 4700:
                        if a == 6 and ch % 2 == 0:
                            pygame.draw.rect(gamewindow, (255, 255, 255), [250, 0, 50, 50])
                            text_screen(str(95), black, 255, 15, 40)
                            gamewindow.blit(ladder3, [200, 5])
                            gamewindow.blit(token_g, [250, 0])
                        else:
                            pos2 = pos2 + a * 50

                    if pos2 == 4750:
                        if (a == 5 or a == 6) and (ch % 2 == 0):
                            pygame.draw.rect(gamewindow, (255, 150, 150), [200, 0, 50, 50])
                            text_screen(str(96), black, 205, 15, 40)
                            gamewindow.blit(token_g, [200, 0])
                        else:
                            pos2 = pos2 + a * 50

                    if pos2 == 4800:
                        if (a == 4 or a == 5 or a == 6) and (ch % 2 == 0):
                            pygame.draw.rect(gamewindow, (255, 255, 255), [150, 0, 50, 50])
                            text_screen(str(97), black, 155, 15, 40)
                            gamewindow.blit(token_g, [150, 0])
                        else:
                            pos2 = pos2 + a * 50

                    if pos2 == 4850:
                        if (a == 3 or a == 4 or a == 5 or a == 6) and (ch % 2 == 0):
                            pygame.draw.rect(gamewindow, (255, 150, 150), [100, 0, 50, 50])
                            text_screen(str(98), black, 105, 15, 40)
                            gamewindow.blit(snake3, [80, 20])
                            gamewindow.blit(token_g, [100, 0])
                        else:
                            pos2 = pos2 + a * 50

                    if pos2 == 4900:
                        if (a == 2 or a == 3 or a == 4 or a == 5 or a == 6) and (ch % 2 == 0):
                            pygame.draw.rect(gamewindow, (255, 255, 255), [50, 0, 50, 50])
                            text_screen(str(99), black, 55, 15, 40)
                            gamewindow.blit(snake3, [80, 20])
                            gamewindow.blit(token_g, [50, 0])
                        else:
                            pos2 = pos2 + a * 50
                elif pos2==300:
                    ladder_climb.play()
                    pos2=dictionary[300]+a*50
                elif pos2==1000:
                    ladder_climb.play()
                    pos2=dictionary[1000]+a*50
                elif pos2==2550:
                    ladder_climb.play()
                    pos2=dictionary[2550]+a*50
                elif pos2==2750:
                    ladder_climb.play()
                    pos2=dictionary[2750]+a*50
                elif pos2==2300:
                    snake_eat.play()
                    pos2=dictionary[2300]+a*50
                elif pos2==3900:
                    snake_eat.play()
                    pos2=dictionary[3900]+a*50
                elif pos2==4250:
                    snake_eat.play()
                    pos2=dictionary[4250]+a*50
                elif pos2==4900:
                    snake_eat.play()
                    pos2=dictionary[4900]+a*50

                else:
                    pos2 = pos2 + a * 50

            if (550 < x < 650 and 150 < y < 250):
                die_roll.play()
            dice(x, y, ch, a, ch_1,ch_2,pos1,pos2)
            if a==1 or a==2 or a==3 or a==4 or a==5:
                ch=ch+1
            display_score(pos1,pos2,ch_1,ch_2)
            turn(ch)
            win(pos1, pos2)

    pygame.display.update()