import pygame
import sees
import sees.Scene as Sc

class EditSelector:
    def __init__(self, scene: Sc):
        self.__scene = scene
        self.__drawable = None
        self.__pos = sees.PosTuple._make((0, 0))

    def createDrawable(self, scene: Sc):
        tex = pygame.image.load(".//editselector.png").convert_alpha()
        self.__drawable = scene.addDrawable(sees.Sprite(tex, sees.SpriteSize.SPR_16x16, (0, 0), (2, 0, 0)))
    
    def getPos(self):
        return self.__pos
    
    def setPos(self, pos: sees.PosTuple):
        self.__pos = sees.PosTuple._make(pos)
        self.__scene.getDrawable(self.__drawable).setPos((2, self.__pos.x, self.__pos.y))
    
    def getDrawable(self):
        return self.__drawable

class Editor(Sc.Scene):
    def __init__(self):
        super().__init__(sees.Resolution.RES_256x224, 60)
        self.__selector = EditSelector(self)
        self.__tiles = []
        self.__tiles.append((0, 0))
    
    def getSelector(self):
        return self.__selector
    
    def createDrawables(self):
        self.__selector.createDrawable(self)
    
    def logic(self):
        return