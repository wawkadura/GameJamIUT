import pygame
from enum import Enum
from sees.TupleEnumTypes import SceneState, PosLayerTuple, Resolution
from sees import Drawables
from sees.Input import InputBindings
from typing import NamedTuple

class player(object):
    def __init__(self,x,y):
        self.imagePerso= pygame.image.load(".//Sprites//MainCharacter.png").convert_alpha()
        self.x = x
        self.y = y
        self.width= 16
        self.height= 16
        self.vel= 16
        self.left= False
        self.right= False
        self.up= False
        self.down= False
        self.hitbox= (self.x , self.y, 16, 16)
        self.spritesPerso= {'standing':(0,0),'right':(0,16),'left': (0,32), 'back': (0,48)}
        self.spritesFeu = {'up':(64,48) , 'down': (64,0), 'right':(64,16), 'left':(64,32) }

    def direction(self,direction):
        if direction=="left":
            self.left=True
            self.right=False
            self.up=False
            self.down=False
        elif direction == "right":
            self.left=False
            self.right=True
            self.up=False
            self.down=False
        elif direction == "up":
            self.left=False
            self.right=False
            self.up=True
            self.down=False
        else:
            self.left=False
            self.right=False
            self.up=False
            self.down=True

    def getImagePerso(self):
        if self.right: return self.spritesPerso['right']
        if self.left: return self.spritesPerso['left']
        if self.down: return self.spritesPerso['standing']
        if self.up: return self.spritesPerso['back']
        else: return self.spritesPerso['standing']
