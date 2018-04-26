import pygame, sys
import pickle
from pygame.locals import *
from ItemsClasses import *
from PlayerClasses import *

#Colors   R    G   B
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
FUCHSIA = (255, 0, 255)
GRAY = (128, 128, 128)
LIME = (0, 128, 0)
MAROON = (128, 0, 0)
NAVYBLUE = (0, 0, 128)
OLIVE = (128, 128, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)
SILVER = (192, 192, 192)
TEAL = (0, 128, 128)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
CYAN = (0, 255, 255)

pygame.init()
DISPLAYWIDTH = 1024
DISPLAYHEIGHT = 683
DISPLAYSURF = pygame.display.set_mode((DISPLAYWIDTH, DISPLAYHEIGHT))
FPS = 30
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption("Lost in the Forest!")

inventoryFont = pygame.font.Font(None, 32)
selectFont = pygame.font.Font(None, 32)
selectFont.set_underline(True)
charImgs = ('characters/guy0.png','characters/guy1.png','characters/guy2.png')
coinImg = 'items/coin0.png' 
mapImg = 'items/map.png'
coinSound = 'sounds/coin.wav'
player = Player(700,500,charImgs)#starting(x,y)coords
all_sprites = pygame.sprite.Group()

levelitems = pygame.sprite.Group()
coin = Item('c1',500,600,{'coin':1},coinImg,coinSound)
coin2 = Item('c2',220,530,{'coin':1},coinImg,coinSound)
mapitem = Item('themap',900,500,{'map':1},mapImg,coinSound)
levelitems.add(coin, coin2, mapitem)
levelwalls = pygame.sprite.Group()
wall = Wall('w1',0,450,1000,10)
wall1 = Wall('w2',0,683,1000,10)
wall3 = Wall('w3',1020,450,5,300)
levelwalls.add(wall, wall1, wall3)

all_sprites.add(levelwalls,levelitems)

def level():
    moveX,moveY=0,0
    player.set_location(level)
    background = pygame.image.load("backgrounds/forest.jpg").convert()
    while True:#Game Loop
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    moveX = -5
                if event.key==pygame.K_d:
                    moveX = 5
                if event.key==pygame.K_w:
                    moveY = -5
                if event.key==pygame.K_s:
                    moveY = 5
                if event.key==pygame.K_e:
                    moveX = 0
                    moveY = 0
                    inventoryMenu()
                if (event.key==K_ESCAPE):
                    moveX=0
                    moveY=0
                    pauseMenu()
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_a:
                    moveX=0
                if event.key==pygame.K_d:
                    moveX=0
                if event.key==pygame.K_w:
                    moveY=0
                if event.key==pygame.K_s:
                    moveY=0
        if player.get_x() < 5:
            player.set_rect(DISPLAYWIDTH-100, player.get_y(),
                            player.get_width(), player.get_height())
            level2()
        DISPLAYSURF.blit(background, (0,0))
        player.update(moveX,moveY,levelitems,levelwalls)
        player.draw(DISPLAYSURF)
        levelitems.draw(DISPLAYSURF)
        FPSCLOCK.tick(FPS)
        pygame.display.update()

level2items = pygame.sprite.Group()
coin = Item('c3',350,575,{'coin':1},coinImg,coinSound)
level2items.add(coin)
level2walls = pygame.sprite.Group()
wall = Wall('w4',0,450,1000,10)
wall1 = Wall('w5',0,683,1000,10)
wall2 = Wall('w6',0,450,5,300)
level2walls.add(wall, wall1, wall2)

all_sprites.add(level2walls,level2items)

def level2():
    moveX,moveY=0,0
    player.set_location(level2)
    background = pygame.image.load("backgrounds/forestfront.jpg").convert()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    moveX = -5
                if event.key==pygame.K_d:
                    moveX = 5
                if event.key==pygame.K_w:
                    moveY = -5
                if event.key==pygame.K_s:
                    moveY = 5
                if event.key==pygame.K_e:
                    moveX = 0
                    moveY = 0
                    inventoryMenu()
                if (event.key==K_ESCAPE):
                    moveX=0
                    moveY=0
                    pauseMenu()
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_a:
                    moveX=0
                if event.key==pygame.K_d:
                    moveX=0
                if event.key==pygame.K_w:
                    moveY=0
                if event.key==pygame.K_s:
                    moveY=0
        if player.get_x() > DISPLAYWIDTH-90:
            player.set_rect(10, player.get_y(), player.get_width(), player.get_height())
            level()
        DISPLAYSURF.blit(background, (0,0))
        player.update(moveX,moveY,level2items,level2walls)
        player.draw(DISPLAYSURF)
        level2items.draw(DISPLAYSURF)
        FPSCLOCK.tick(FPS)
        pygame.display.update()

scroll = pygame.image.load("backgrounds/scroll.png").convert_alpha()
scroll = pygame.transform.scale(scroll, (844, 543))#scroll (width, height)
scrollX = 90#90 default
scrollY = 70#70 default

def startMenu():
    background = pygame.image.load("backgrounds/forest.jpg").convert()
    selectNew = True
    loadingFail = False
    xcoord = 212
    Titletext = inventoryFont.render('Welcome to your adventure game!', True, BLACK)
    while True:
        ycoord = 150
        DISPLAYSURF.blit(background, (0,0))
        DISPLAYSURF.blit(scroll, (scrollX,scrollY))
        for event in pygame.event.get():
            if (event.type==pygame.QUIT):
                pygame.quit()
                sys.exit()
            if (event.type==pygame.KEYDOWN):
                if (event.key==pygame.K_w):
                    selectNew = True
                if (event.key==pygame.K_s):
                    selectNew = False
                if (event.key==K_SPACE):
                    if selectNew == True:
                        player.get_location()()
                    else:
                        try:
                            importGame()
                        except:
                            loadingFail = True
                            selectNew = True
                            print('Make sure the save files are saved as ' +
                                 'GuyGameSpriteSave.obj and GuyGamePlayerSave.obj ' +
                                  'in the same directory as MainGame.py')
        if selectNew == True:
            Newtext = selectFont.render('New Game!', True, BLACK)
            Loadtext = inventoryFont.render('Load Game!', True, BLACK)
        else:
            Newtext = inventoryFont.render('New Game!', True, BLACK)
            Loadtext = selectFont.render('Load Game!', True, BLACK)
        if loadingFail:
            Loadtext = inventoryFont.render('Save files not found. Try a new game.', True, BLACK)
            selectNew = True
        DISPLAYSURF.blit(Titletext, (xcoord,ycoord))
        ycoord += 50
        DISPLAYSURF.blit(Newtext, (xcoord,ycoord))
        ycoord += 50
        DISPLAYSURF.blit(Loadtext, (xcoord,ycoord))
        FPSCLOCK.tick(FPS)
        pygame.display.update()

def pauseMenu():
    inMenu = True
    xcoord = 212
    selection = 0
    Titletext = inventoryFont.render('Paused -- Press escape to return to the game.',
                                     True, BLACK)
    menuTexts = ['Save Game', 'Load Game', 'Exit Game']
    while inMenu:
        ycoord = 150
        for event in pygame.event.get():
            if (event.type==pygame.QUIT):
                pygame.quit()
                sys.exit()
            if (event.type==pygame.KEYDOWN):
                if (event.key==K_w):
                    if selection <= 0:
                        selection = 2
                    else:
                        selection -= 1
                if (event.key==K_s):
                    if selection >= 2:
                        selection = 0
                    else:
                        selection += 1
                if (event.key==K_SPACE):
                    inMenu = False
                if (event.key==K_ESCAPE):
                    return
        DISPLAYSURF.blit(scroll, (scrollX,scrollY))
        DISPLAYSURF.blit(Titletext, (xcoord,ycoord))
        ycoord += 50
        for text in menuTexts:
            if menuTexts.index(text) == selection:
                Selecttext = selectFont.render(text, True, BLACK)
                DISPLAYSURF.blit(Selecttext, (xcoord,ycoord))
                ycoord += 50
            else:
                Notext = inventoryFont.render(text, True, BLACK)
                DISPLAYSURF.blit(Notext, (xcoord,ycoord))
                ycoord += 50
        FPSCLOCK.tick(FPS)
        pygame.display.update()         
    if selection == 0:
        saveMenu()
    elif selection == 1:
        loadMenu()
    else:
        pygame.quit()
        sys.exit()

def loadMenu():
    Loadtext = inventoryFont.render("Restart the game and choose 'load game' at the start menu.", True, BLACK)
    Loadtext2 = inventoryFont.render("Press esc to return to the game.", True, BLACK)
    while True:
        for event in pygame.event.get():
            if (event.type==pygame.QUIT):
                pygame.quit()
                sys.exit()
            if (event.type==pygame.KEYDOWN):
                if (event.key==K_ESCAPE):
                    return        
        DISPLAYSURF.blit(scroll, (scrollX,scrollY))
        DISPLAYSURF.blit(Loadtext, (170,150))
        DISPLAYSURF.blit(Loadtext2, (170,200))
        FPSCLOCK.tick(FPS)
        pygame.display.update()

def saveMenu():
    inMenu = True
    save = False
    xcoord = 212
    Titletext = inventoryFont.render('Save the game?', True, BLACK)
    while inMenu:
        ycoord = 150
        for event in pygame.event.get():
            if (event.type==pygame.QUIT):
                pygame.quit()
                sys.exit()
            if (event.type==pygame.KEYDOWN):
                if (event.key==K_w):
                    save = True
                if (event.key==K_s):
                    save = False
                if (event.key==K_SPACE):
                    inMenu = False
        if save == True:
            Yestext = selectFont.render('Yes!', True, BLACK)
            Notext = inventoryFont.render('No!', True, BLACK)
        else:
            Yestext = inventoryFont.render('Yes!', True, BLACK)
            Notext = selectFont.render('No!', True, BLACK)
        DISPLAYSURF.blit(scroll, (scrollX,scrollY))
        DISPLAYSURF.blit(Titletext, (xcoord,ycoord))
        ycoord += 50
        DISPLAYSURF.blit(Yestext, (xcoord,ycoord))
        ycoord += 50
        DISPLAYSURF.blit(Notext, (xcoord,ycoord))
        FPSCLOCK.tick(FPS)
        pygame.display.update()
    if save == True:
        saveGame()

def saveGame():
    allNames = []
    for sprite in all_sprites:
        allNames.append(sprite.get_name())
    playerTraits = (player.get_x(),player.get_y(),player.get_inventory(),player.get_location())
    saveObject(playerTraits, 'GuyGamePlayerSave.obj') 
    saveObject(allNames, 'GuyGameSpriteSave.obj')
        
def saveObject(obj, filename):
    with open(filename, 'wb') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

def importGame():
    allNames = importNames('GuyGameSpriteSave.obj')
    for sprite in all_sprites:
        if sprite.get_name() not in allNames:
            sprite.kill()
    playerTraits = importPlayer('GuyGamePlayerSave.obj')
    player.set_rect(playerTraits[0],playerTraits[1],
                    player.get_width(),player.get_height())
    player.set_inventory(playerTraits[2])
    player.set_location(playerTraits[3])
    player.get_location()()
       
def importPlayer(filename):
    with open(filename, 'rb') as input:
        playerTraits = pickle.load(input)
    return playerTraits

def importNames(filename):
    with open(filename, 'rb') as input:
        allNames = pickle.load(input)
    return allNames

def inventoryMenu():
    '''chooses inventory menu'''
    playerInv = player.get_inventory()
    invKeys = []
    if playerInv == {}:
        emptyInvMessage()
    else:
        for key in playerInv.keys():
            invKeys.append(key)
        if len(invKeys) <= 8:
            smallInvMenu(playerInv, invKeys)

def emptyInvMessage():
    HeaderText = inventoryFont.render('--Inventory--', True, BLACK)
    EmptyText = inventoryFont.render('Inventory is Empty... Go find some stuff!!', True, BLACK)
    xcoord = 212
    ycoord = 150
    Open = True
    while Open:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_e:
                    Open = False
        DISPLAYSURF.blit(scroll, (scrollX,scrollY))
        DISPLAYSURF.blit(HeaderText, (xcoord,ycoord))
        DISPLAYSURF.blit(EmptyText, (xcoord,ycoord+50))
        FPSCLOCK.tick(FPS)
        pygame.display.update()

def smallInvMenu(playerInv, invKeys):
    HeaderText = inventoryFont.render('--Inventory--', True, BLACK)
    xcoord = 212
    Open = True
    selectNum = 0
    while Open:
        ycoord = 150
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_e:
                    Open = False
                if event.key==pygame.K_w:
                    if selectNum > 0:
                        selectNum -= 1
                    else:
                        selectNum = len(invKeys)-1
                if event.key==pygame.K_s:
                    if selectNum < len(invKeys)-1:
                        selectNum += 1
                    else:
                        selectNum = 0
        DISPLAYSURF.blit(scroll, (scrollX,scrollY))
        DISPLAYSURF.blit(HeaderText, (xcoord,ycoord))
        ycoord += 50
        for key in invKeys:
            if invKeys[selectNum] == key:
                itemtext = selectFont.render(key + '---' + str(playerInv[key]),
                                             True, BLACK)
            else:
                itemtext = inventoryFont.render(key + '---' + str(playerInv[key]),
                                                True, BLACK)
            DISPLAYSURF.blit(itemtext, (xcoord,ycoord))
            ycoord += 40
        FPSCLOCK.tick(FPS)
        pygame.display.update()

#start location---------------
player.set_location(level)
#start game--------------
startMenu()