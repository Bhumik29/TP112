import module_manager
module_manager.review()
import random 


import pygame
pygame.init()

displayWidthStart=460
displayHeightStart=250
clock = pygame.time.Clock()
startScreen = pygame.display.set_mode((460, 250))
pygame.display.set_caption("Welcome")
startImg=pygame.image.load("startscreen.jpg")


def background(x,y):
    startScreen.blit(startImg, (x,y))

def displayText():
    myfont = pygame.font.SysFont("Helvetica", 25)
    label = myfont.render("Welcome to the Game of Life! Click anywhere to begin.", 1, (255,255,255))
    startScreen.blit(label, (10, 220))

startRunning=True
while startRunning:
    time = clock.tick(1000) #similar to timerDelay
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            startRunning = False
        if event.type == pygame.MOUSEBUTTONUP:
            running=True
            startRunning=False
    background(0,0)
    displayText()
    pygame.display.update()

pygame.quit()




displayWidth=600
displayHeight=800
black=(0,0,0)
white=(255,255,255)



clock = pygame.time.Clock()
screen = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Play Game")
carImg=pygame.image.load("rsz_lifecar.png")
spinnerImg=pygame.image.load("rsz_spinnerlife.png")
boardImg=pygame.image.load("rsz_boardback.jpg")
exampleCard=pygame.image.load("rsz_examplecard.png")
blueCar=pygame.image.load("rsz_bluecar.png")
gameOverImg=pygame.image.load("rsz_gameover.png")
carX=300
carY=620
pos1stPath=[(300, 620), (287, 667), (222, 681), (177, 710), (231, 740), (297, 740), (355, 740), (416, 740), (480, 734), (543, 722), (542, 623), (549, 551), (544, 554), (499, 610), (455, 638), (419, 599), (460, 531), (516, 487), (556, 446), (512, 405), (438, 403), (388, 405), (321, 402), (259, 404), (187, 385), (115, 382), (52, 358), (48, 272), (44, 147), (95, 56), (122, 31), (194, 34), (228, 126), (257, 159), (298, 155), (373, 152), (426, 117), (508, 74), (554, 221), (554, 324), (528, 356), (464, 358), (400, 360), (365, 360), (279, 358), (222, 342), (267, 317), (291, 274), (374, 271), (436, 261), (435, 265), (444, 197), (479, 247), (518, 199), (460, 143), (390, 57), (309, 31), (240, 37), (189, 122), (188, 204), (148, 284), (89, 339), (148, 335), (179, 422), (135, 472), (85, 469), (30, 485), (24, 546), (21, 617), (23, 710), (55, 765), (130, 733), (59, 677), (110, 632), (179, 641)]
pos2ndPath=[(300, 620), (333, 682), (420, 686), (464, 689), (480, 734), (543, 722), (542, 623), (549, 551), (544, 554), (499, 610), (455, 638), (419, 599), (460, 531), (516, 487), (556, 446), (512, 405), (438, 403), (388, 405), (321, 402), (259, 404), (187, 385), (115, 382), (52, 358), (48, 272), (44, 147), (95, 56), (122, 31), (194, 34), (228, 126), (257, 159), (298, 155), (373, 152), (426, 117), (508, 74), (554, 221), (554, 324), (528, 356), (464, 358), (400, 360), (365, 360), (279, 358), (222, 342), (267, 317), (291, 274), (374, 271), (436, 261), (435, 265), (444, 197), (479, 247), (518, 199), (460, 143), (390, 57), (309, 31), (240, 37), (189, 122), (188, 204), (148, 284), (89, 339), (148, 335), (179, 422), (135, 472), (85, 469), (30, 485), (24, 546), (21, 617), (23, 710), (55, 765), (130, 733), (59, 677), (110, 632), (179, 641)]

pop1stPath=[exampleCard]*len(pos1stPath)
playerIndex=0
compIndex=0
player1=True

    
def car(x,y, path, index):
    x=pos1stPath[index][0]
    y=pos1stPath[index][1]
    screen.blit(carImg, (x,y))

def computerCar(x,y,path,index):
    x=pos1stPath[index][0]
    y=pos1stPath[index][1]
    screen.blit(blueCar, (x,y))

def move(path):
    for i in range (len(path)):
        car(path[i][0], path[i][1], pracPath, index, player1)
        
def spinner(x,y):
    screen.blit(spinnerImg, (x,y))
    

def background(x,y):
    screen.blit(boardImg, (x,y))
    
def gameOver():
    screen.blit(gameOverImg, (0,0))

def spinWheel(path, index):
    move=random.randint(1,10)
    index+=move
    return index
    
def popUp(index, path):
    screen.blit(exampleCard, (displayWidth//2-100, displayHeight//2))
  
   

while running:
    time = clock.tick(100) #similar to timerDelay
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                carX-=10
            if event.key==pygame.K_RIGHT:
                carX+=10
            if event.key==pygame.K_DOWN:
                carY+=10
            if event.key==pygame.K_UP:
                carY-=10
            if event.key==pygame.K_SPACE:
                if (player1):
                    playerIndex=spinWheel(pos1stPath, playerIndex)
                    player1=False
                    if (playerIndex>len(pos1stPath)):
                        running=False
                else:
                    compIndex=spinWheel(pos1stPath, compIndex)
                    if (compIndex>len(pos1stPath)):
                        running=False
                    player1=True
        if event.type == pygame.MOUSEBUTTONUP:
            print (pygame.mouse.get_pos())
    if (running):
        background(0,0)
        spinner(225,440)
        car(pos1stPath[0][0], pos1stPath[0][1], pos1stPath, playerIndex)
        computerCar(pos1stPath[0][0], pos1stPath[0][1], pos1stPath, compIndex)
    else:
        gameOver()
    pygame.display.update()

pygame.quit()

