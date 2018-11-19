import module_manager
module_manager.review()

import pygame
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Welcome")

spinner=pygame.image.load("spinnerLife.jpg")


running = True
while running:
    time = clock.tick(50) #similar to timerDelay

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.draw.rect(screen, (255,0,0), (300,300,40,40))
    pygame.display.update()
    
   

pygame.quit()