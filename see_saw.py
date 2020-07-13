"""See Saw game"""

#Written and video tutorial coming soon

"""
author: ashraf minhaj
email: ashraf_minhaj@yahoo.com
blog: ashrafminhajfb.blogspot.com
"""

import pygame
import os
from pandas import read_csv

#game variables
WHITE = (255, 255, 255)                         #Tuple to store color RGB values (R, G, B)
BLACK = (0, 0, 0)

IMAGE_POS = (50, 50)                                    #x, y coordinates of image to be displayed
PARENT_WIDTH, PARENT_HEIGHT = 400, 300                  #game window width height
BTN1_X, BTN1_Y = 30, PARENT_HEIGHT - 30                 #Circular button x, y
BTN2_X, BTN2_Y = PARENT_WIDTH - 30, PARENT_HEIGHT - 30
BTN_RADIUS = 20                                         #circle radius
BTN_WIDTH = 3                                           #button (circle) thickness

pebble_count = 0                   #pebble_count = 2 and GAME OVER
status = 0                         #to count questions
score = 0

"""things to be performed by code itself"""
parent_path =  os.path.dirname(os.path.abspath(__file__))   #the path where the code is saved
#read images
images = []                        #empty list to store the images
for i in range(4):
    image = pygame.image.load(parent_path + '\\images\\' + str(i) + '.png')  #read an image
    images.append(image)                                             #add to the list

qst_file = read_csv(parent_path + '\\questions.csv')   #read the question file
num_of_qst = len(qst_file.index)                       #check how many questions are there
print(num_of_qst)

"""define window parameters"""
pygame.init()                                  #initialize pygame window
window = pygame.display.set_mode((PARENT_WIDTH, PARENT_HEIGHT)) #set the display dimension
pygame.display.set_caption("See Saw")          #game name on the title bar

FONT = pygame.font.Font('freesansbold.ttf', 32)
FONT1 = pygame.font.Font('freesansbold.ttf', 18)
#FONT2 = pygame.font.Font('freesansbold.ttf', 15)
BTN1_TEXT = FONT.render('A', True, BLACK)
BTN2_TEXT = FONT.render('B', True, BLACK)


"""setup game loop"""
FPS = 60                    #Window refresh per second
clock = pygame.time.Clock()
run = True

while run:
    clock.tick(FPS)         #update the window/run loop by this speed

    if pebble_count == 3:
        window.fill(WHITE)                             #change the color
        window.blit(images[pebble_count], IMAGE_POS)   #add last image

        xtext = FONT.render("GAME OVER", True, BLACK)                                            #end text
        score_text = FONT1.render("Score: " + str(score) + "/" + str(num_of_qst), True, BLACK)   #score
        x_rect = xtext.get_rect(center=(PARENT_WIDTH/2, BTN1_Y - 80))                            #pos
        score_rect = score_text.get_rect(center=(PARENT_WIDTH/2, BTN1_Y - 10))

        window.blit(xtext, x_rect)                #finally place the texts
        window.blit(score_text, score_rect)

    elif status >= num_of_qst:
        window.fill(WHITE)
        finish_text = FONT.render("The little Man lives!", True, BLACK)
        score_text = FONT1.render("Score: " + str(score) + "/" + str(num_of_qst), True, BLACK)
        
        score_rect = score_text.get_rect(center=(PARENT_WIDTH/2, BTN1_Y - 10))
        finish_text_rect = finish_text.get_rect(center=(PARENT_WIDTH/2, PARENT_HEIGHT/2))

        window.blit(finish_text, finish_text_rect)
        window.blit(score_text, score_rect)


    elif status < num_of_qst:
        question = qst_file.iat[status, 0]    #read the question from datas and so on
        hint = qst_file.iat[status, 1]        
        ans = qst_file.iat[status, 2]

        qst_text = FONT1.render(question, True, BLACK)  #make a text surface for pygame
        hint_text = FONT1.render(hint, True, BLACK)     #hint surface

        window.fill(WHITE)                              #fill the window with white color
        window.blit(images[pebble_count], IMAGE_POS)                                     #add image (the man on see saw)
        c0 = pygame.draw.circle(window, BLACK, (BTN1_X, BTN1_Y), BTN_RADIUS, BTN_WIDTH)  #circle1 for button
        c1 = pygame.draw.circle(window, BLACK, (BTN2_X, BTN2_Y), BTN_RADIUS, BTN_WIDTH)  #circle2 

        window.blit(BTN1_TEXT, (BTN1_X - 10, BTN1_Y-15))    #add button text - A
        window.blit(BTN2_TEXT, (BTN2_X - 10, BTN2_Y-15))    #B

        qst_rect = qst_text.get_rect(center=(PARENT_WIDTH/2, BTN1_Y - 80))     #get size, half in x axis, 80 pixel less than btn in y
        hint_rect = hint_text.get_rect(center=(PARENT_WIDTH/2, BTN1_Y - 50))
        window.blit(qst_text, qst_rect)                                        #position text in place
        window.blit(hint_text, hint_rect)


    pygame.display.update()    #update the display

    #check for events
    for event in pygame.event.get():    #quit button
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            cx, cy = pygame.mouse.get_pos()          #get mouse click position
            #print(cx, " ", cy)

            #check for button clicks
            if (abs(BTN1_X - cx) < 20) and (abs(BTN1_Y - cy) < 20):    #A is pressed
                print(len(ans))
                if ans == 'a':
                    status += 1
                    score += 1
                else:
                    pebble_count +=1
                    status += 1

            elif (abs(BTN2_X - cx) < 20) and (abs(BTN2_Y - cy) < 20):  #B is pressed
                print(len(ans))
                if ans == 'b':
                    status += 1
                    score += 1
                else:
                    pebble_count += 1
                    status += 1

pygame.quit()      #close everything