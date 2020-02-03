import random, pygame, sys

class Button():
    def __init__(self, x, y,size,code,image,image2, window):
        self.x = x
        self.y = y
        self.size = size
        self.tile = pygame.Surface((self.size, self.size))
        self.image = image
        self.image2 = image2
        self.code = code
        self.faceUp = False
        self.enabled = True
        self.window = window

    def is_inside(self,inX, inY):
        if inX >= self.x and inX <= self.x + self.size:
            if inY >= self.y and inY <= self.y + self.size:
                return True
            else:
                return False
        else:
            return False

    def flip(self):
        if self.enabled == True:
            self.faceUp = not self.faceUp
            self.draw()

    def draw(self):
        if self.faceUp == False:
            self.window.blit(self.image2,(self.x,self.y))
        else:
            self.window.blit(self.image,(self.x,self.y))



    def win(self):
        return True

    def disable(self):
        self.enabled = False
