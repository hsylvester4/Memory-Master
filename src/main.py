"""
Team Hopper: Alex Mandel, Hunter Sylvester, Will Meyer
Artwork by Maya Quandt
SEMESTER Project: Memory Master
"""

import random, pygame, sys
from Button import Button
from pygame.locals import *


BG_COLOR = (0,0,102)
BOX_COLOR = (255,255,91)
TEXT_COLOR = (255,255,255)
WIN_WIDTH = 600
WIN_HEIGHT = 600
NUM_CARDS_X = 4
NUM_CARDS_Y = 4
BOX_WIDTH = int(WIN_WIDTH * 2 / (NUM_CARDS_X * 3))
BOX_HEIGHT = int(WIN_HEIGHT * 2 / (NUM_CARDS_Y * 3))
GAP = int(WIN_WIDTH/((NUM_CARDS_X+1) * 6) + WIN_HEIGHT/((NUM_CARDS_Y+1) * 6))

def startmenu():
    window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    startscreen = pygame.image.load("../data/assets/startup-screen.png")
    buttonimg = pygame.image.load("../data/buttons/start-button.png")
    startButton = Button(178, 450, 0, None, None, buttonimg, window)

    while True:
        startButton.draw()
        window.blit(startscreen, (0, 0))

        draw_text(window,"Version 0.9.0",500,550,"arial",20,(255,255,255))
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                print(pygame.mouse.get_pos())
                if startButton.is_inside(178,450):
                    window = setup_window()
                    tiles = setup_tiles(window)
                    gameplay(tiles, window)
                else:
                    pass
        pygame.display.update()

def draw_text(window,text,x,y,font,size,color):
    font = pygame.font.SysFont(font,size)
    text = font.render(text, True, (color))
    window.blit(text,(x,y))

"""
def levelmenu():
    window = setup_window()
    easybutton = pygame.image.load("../data/buttons/easy-button.png")
    medbutton = pygame.image.load("../data/buttons/medium-button.png")
    hardbutton = pygame.image.load("../data/buttons/hard-button.png")
    easy = Button(232,362,0,140,53,None,None,easybutton,window)
    medium = Button(232,427,0,142,53,None,None,medbutton,window)
    hard = Button(232,494,0,140,52,None,None,hardbutton,window)
    levelscreen = pygame.image.load("../data/assets/level-screen.png")

    while True:
        easy.draw()
        medium.draw()
        hard.draw()
        window.blit(levelscreen,(0,0))
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if easy.is_inside(232, 362):
                    #setup_tiles_easy()
                    print("easy")
                elif medium.is_inside(232,427):
                    print("medium")
                elif hard.is_inside(232,427):
                    print("hard")
                else:
                    pass
        pygame.display.update()
"""
def pressButton(x,y,button):
    if button.is_inside(x,y):
        return True

def hasWon():
    window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    image = pygame.image.load("../data/assets/win-screen.png")
    playagainimg = pygame.image.load("../data/buttons/play-again-button.png")
    playagain = Button(185,450,0,None,None,playagainimg,window)

    while True:
        window.blit(image,(0,0))
        playagain.draw()

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if playagain.is_inside(185,450):
                    startmenu()
        pygame.display.update()

def ifWon(tiles):
    for b in tiles:
        if b.enabled == True:
            return False
    return True

def load_images():
    image0 = pygame.image.load("../data/Tile Art/front-back of cards/apple.png")
    image1 = pygame.image.load("../data/Tile Art/front-back of cards/avocado.png")
    image2 = pygame.image.load("../data/Tile Art/front-back of cards/grapes.png")
    image3 = pygame.image.load("../data/Tile Art/front-back of cards/kiwi.png")
    image4 = pygame.image.load("../data/Tile Art/front-back of cards/lemon.png")
    image5 = pygame.image.load("../data/Tile Art/front-back of cards/pineapple.png")
    image6 = pygame.image.load("../data/Tile Art/front-back of cards/strawberry.png")
    image7 = pygame.image.load("../data/Tile Art/front-back of cards/watermelon.png")
    # create a list of images
    images = [image0, image1, image2, image3,
              image4, image5, image6, image7]
    rescaled = [pygame.transform.scale(image, (BOX_WIDTH, BOX_HEIGHT)) for image in images]
    return rescaled

def setup_window():
    clock = pygame.time.Clock()
    mouseX = 0
    mouseY = 0
    Xmargin = 50
    Ymargin = 50
    pygame.display.set_caption("Memory Master")

    window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    window.fill(BG_COLOR)
    return window

def setup_tiles(window):
    images = load_images()
    # This is to keep track of images
    ids = [i for i in range(len(images))]
    # There are 2 of each image, so we double the id list
    ids += ids
    # shuffle the image ids
    random.shuffle(ids)
    # Here we make an ordered list of the images
    shuffled_images = [images[i] for i in ids]

    card_back_img = pygame.image.load("../data/Tile Art/front-back of cards/back-of-card.png")
    card_back_img = pygame.transform.scale(card_back_img, (BOX_WIDTH, BOX_HEIGHT))
    tiles = []
    for i in range(4):
        for j in range(4):
            y = i * BOX_HEIGHT + i * GAP + GAP
            x = j * BOX_WIDTH + j * GAP + GAP
            # this gets the correct image...
            # 4i+j converts an i,j entry in the
            # grid to the correct spot in a 16
            # images long list
            idx = 4*i + j
            # this gets the image number/id
            code = ids[idx]
            # this gets the image
            card_front_img = shuffled_images[idx]
            b = Button(x,y,80,code,card_front_img,card_back_img,window)
            tiles.append(b)
    return tiles

def find_tile(x,y, tiles):
    for b in tiles:
        if b.is_inside(x,y):
            if b.enabled:
                return b
    return None

def gameplay(tiles, window):
    prevTile = None
    revealedTiles = []
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mouseX, mouseY = event.pos
            elif event.type == MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
                x,y = pygame.mouse.get_pos()

                newTile = find_tile(mouseX,mouseY, tiles)

                if (not newTile) or newTile == prevTile: # not a new tile
                    if prevTile:
                        prevTile.flip()
                    prevTile = None
                elif not prevTile: # there's not already a visible tile
                    prevTile = newTile
                    newTile.flip()
                elif prevTile.code == newTile.code: # if correct
                    newTile.flip()
                    prevTile.disable()
                    newTile.disable()
                    revealedTiles.append(prevTile)
                    revealedTiles.append(newTile)
                    prevTile = None
                else: # if not correct
                    newTile.flip()
                    pygame.time.wait(0)
                    prevTile.flip()
                    newTile.flip()
                    prevTile = None
            if ifWon(tiles):
                hasWon()

            window.fill(BG_COLOR)
            for b in tiles:
                b.draw()

        pygame.display.update()

def main():
    pygame.init()
    window = setup_window()
    tiles = setup_tiles(window)
    #gameplay(tiles, window)
    startmenu()
    #hasWon()
    #levelmenu()
main()

