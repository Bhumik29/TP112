import module_manager
module_manager.review()
import random 
import pygame
import sys
import os
pygame.init()

displayWidth=600
displayHeight=800
ani=4

clock = pygame.time.Clock()
screen = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Play Game")
spinnerImg=pygame.image.load("rsz_spinnerlife.png")
boardImg=pygame.image.load("rsz_boardback.jpg")
pos1stPath=[(300, 620), (287, 667), (222, 681), (177, 710), (231, 740), (297, 740), (355, 740), (416, 740), (480, 734), (543, 722), (542, 623), (549, 551), (544, 554), (499, 610), (455, 638), (419, 599), (460, 531), (516, 487), (556, 446), (512, 405), (438, 403), (388, 405), (321, 402), (259, 404), (187, 385), (115, 382), (52, 358), (48, 272), (44, 147), (95, 56), (122, 31), (194, 34), (228, 126), (257, 159), (298, 155), (373, 152), (426, 117), (508, 74), (554, 221), (554, 324), (528, 356), (464, 358), (400, 360), (365, 360), (279, 358), (222, 342), (267, 317), (291, 274), (374, 271), (436, 261), (435, 265), (444, 197), (479, 247), (518, 199), (460, 143), (390, 57), (309, 31), (240, 37), (189, 122), (188, 204), (148, 284), (89, 339), (148, 335), (179, 422), (135, 472), (85, 469), (30, 485), (24, 546), (21, 617), (23, 710), (55, 765), (130, 733), (59, 677), (110, 632), (179, 641)]
index=0

pracPath=[(290, 625), (290, 630)]

class Player(pygame.sprite.Sprite):
    '''
    Spawn a player
    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = pygame.image.load("rsz_lifecar.png")
        self.images.append(img)
        self.image = self.images[0]
        self.rect  = self.image.get_rect()
        self.movex = 0 
        self.movey = 0 
        self.frame = 0
    def control(self, x,y):
        self.movex += x
        self.movey += y
    def update(self):
        self.rect.x = self.rect.x + self.movex   
        self.rect.y = self.rect.y + self.movey
    

player = Player()   # spawn player
player.rect.x = 290   # go to x
player.rect.y = 620   # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10 



def background(x,y):
    screen.blit(boardImg, (x,y))
def spinner(x,y):
    screen.blit(spinnerImg, (x,y))
def spinWheel(path, index):
    move=random.randint(1,10)
    index+=move
    return index
    
running = True
while running:
    time = clock.tick(10) #similar to timerDelay
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                index=spinWheel(pos1stPath, index)
                if (index>len(pos1stPath)):
                    gameOver()
                    running=False
        if event.type == pygame.MOUSEBUTTONUP:
            background(0,0)
            spinner(225,440)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps,0)
            if event.key == pygame.K_UP
                player.control(steps,0)
            if event.key == pygame.K_DOWN:
                player.control(-steps,0)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-steps,0)
    background(0,0)
    spinner(225,440)
    player.update()
    player_list.draw(screen)
    pygame.display.flip()
    # clock.tick(fps)
pygame.quit()