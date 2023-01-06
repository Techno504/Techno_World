import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 800

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

dark_green = (0,200,0)
dark_red = (200,0,0)

character_width = 60
character_height = 160

technowizard_width = 60
technowizard_height = 160

pause = False

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Techno World 2')
clock = pygame.time.Clock()

characterImg = pygame.image.load('character_gimp2.png')
character_iconImg = pygame.image.load('character_icon.png')
technowizardImg = pygame.image.load('techno_wizard_gimp2.png')
chestImg = pygame.image.load('chest_3d.png')
doorImg = pygame.image.load('door3.png')
rugImg = pygame.image.load('rug.png')

pygame.display.set_icon(character_iconImg)

def technowizard(technowizard_startx, technowizard_starty, technowizard_width, technowizard_height):
    gameDisplay.blit(technowizardImg, (technowizard_startx,technowizard_starty))

def character(x,y):
    gameDisplay.blit(characterImg, (x,y))

def chest(x,y):
    gameDisplay.blit(chestImg, (x,y))

def door(x,y):
    gameDisplay.blit(doorImg, (x,y))

def rug(x,y):
    gameDisplay.blit(rugImg, (x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def dialogue(text):
    smallText = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(text, smallText)
    TextSurf.fill(white)
    TextRect.center = (515, 150)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def techno_wizard_dialogue_1():
    dialogue("Hello")

def button(msg, x, y, w, h, ic, ac, action=None): # msg=message; x=xpos; y=ypos; w=width; h=height; ic=inactivecolour; ac=activecolour
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y: # mouse[0] => x value of coordinate tuple
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    TextSurf, TextRect = text_objects(msg, smallText)
    TextRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(TextSurf, TextRect)

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pause = False

def paused():
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',100)
        TextSurf, TextRect = text_objects("Paused", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Continue", 150, 450, 100, 50, dark_green, green, unpause)
        button("Quit", 550, 450, 100, 50, dark_red, red, quitgame)

        pygame.display.update()
        clock.tick(15)

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',100)
        TextSurf, TextRect = text_objects("Techno World 2", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Play", 150, 450, 100, 50, dark_green, green, game_loop)
        button("Quit", 550, 450, 100, 50, dark_red, red, quitgame)

        pygame.display.update()
        clock.tick(15)

def game_loop():
    global pause
    x = (display_width * 0.45)
    y = (display_height * 0.6)

    x_change = 0
    y_change = 0

    technowizard_startx = 200
    technowizard_starty = -600
    techno_wizard_speed = 1

    chest_x = 540
    chest_y = 250

    door_x = 240
    door_y = 50

    rug_x = 50
    rug_y = 350

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key==pygame.K_a:
                    x_change = -2
                elif event.key == pygame.K_RIGHT or event.key==pygame.K_d:
                    x_change = 2
                elif event.key == pygame.K_UP or event.key==pygame.K_w:
                    y_change = -2
                elif event.key == pygame.K_DOWN or event.key==pygame.K_s:
                    y_change = 2
                elif event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key==pygame.K_a or event.key==pygame.K_d:
                    x_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key==pygame.K_w or event.key==pygame.K_s:
                    y_change = 0

        if (x + x_change) > -18 and (x + x_change) < (display_width - character_width):
            x += x_change

        if (y + y_change) > 62 and (y + y_change) < 350:
            y += y_change

        gameDisplay.fill((34,67,89))

        pygame.draw.rect(gameDisplay, red, (0,0,800,200))

        chest(chest_x, chest_y)

        door(door_x, door_y)

        rug(rug_x, rug_y)

        technowizard(technowizard_startx, technowizard_starty, technowizard_width, technowizard_height)
        n = 150
        p = 415
        q = 515
        if technowizard_starty < n:
            technowizard_starty += techno_wizard_speed
            n = n - 1
        if technowizard_starty == n and technowizard_startx < p:
            technowizard_startx += techno_wizard_speed
            p = p - 1
        if technowizard_startx == (200 + (p - 1)) and technowizard_starty < q:
            technowizard_starty += techno_wizard_speed
            q = q - 1

        character(x,y)

        pygame.draw.rect(gameDisplay, white, (0,600,800,800))

        #if y < (technowizard_starty + technowizard_height):
            #message_display("y crossover")

            #if x > technowizard_startx and x < (technowizard_startx + technowizard_width) or (x + character_width) > technowizard_startx and (x + technowizard_width) < (technowizard_startx + technowizard_width):
                #message_display("x crossover")
                #techno_wizard_dialogue_1()

        pygame.display.update()
        clock.tick(200)

game_intro()

game_loop()
pygame.quit()
quit()
