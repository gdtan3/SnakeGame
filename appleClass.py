import pygame
import random

'''
Used to split apple to respawn in grids of size - limit
'''
def myround(x, limit):
    remainder = x % limit
    val1 = limit - remainder
    return x + val1

class Apple:

    def __init__(self):
        self.x = 600
        self.y = 200
        self.apple_width = 20
        self.apple_height = 20

    def update(self, display_width,display_height):
        randx = random.randint(0, display_width-20)        
        randy = random.randint(0, display_height-20)

        self.x = myround(randx, 20)
        self.y = myround(randy, 20)

    def show(self, display):
        pygame.draw.rect(display, (255,0,0), (self.x, self.y, self.apple_width,
                                              self.apple_height))
        

    def get_pos(self):
        return [self.x, self.y]
