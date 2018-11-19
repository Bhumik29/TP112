import module_manager
module_manager.review()
import random 
import TP112-Board

import pygame
pygame.init()
pygame.font.init()

displayWidth=460
displayHeight=250
clock = pygame.time.Clock()
screen = pygame.display.set_mode((460, 250))
pygame.display.set_caption("Welcome")
startImg=pygame.image.load("startscreen.jpg")


def background(x,y):
    screen.blit(startImg, (x,y))

def displayText():
    myfont = pygame.font.SysFont("Helvetica", 25)
    label = myfont.render("Welcome to the Game of Life! Click anywhere to begin.", 1, (255,255,255))
    screen.blit(label, (10, 220))

running = True
while running:
    time = clock.tick(1000) #similar to timerDelay
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            print ("yes")
            
    background(0,0)
    displayText()
    pygame.display.update()

pygame.quit()