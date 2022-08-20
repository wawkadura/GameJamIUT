import pygame
from sees import Scene
from sees.TupleEnumTypes import SizeTuple, PosTuple, PosLayerTuple, Resolution, SpriteSize
from typing import NamedTuple, List
from enum import Enum

class Drawable:
    def __init__(self, texture: pygame.image, size: SizeTuple, texPos: PosTuple, pos: PosLayerTuple):
        self.__size = SizeTuple._make(size)
        self.__pos = PosLayerTuple._make(pos)
        self.__tex = texture
        self._srect: pygame.Rect = pygame.Rect(texPos, size)
        self._drect: pygame.Rect = pygame.Rect((self.__pos.x, self.__pos.y), size)
        self._scene: Scene = None

    def draw(self, surface):
        if (self._scene != None and surface != None):
            self._drect.x = self.__pos.x - self._scene.getPosX()
            self._drect.y = self.__pos.y - self._scene.getPosY()
            surface.blit(self.__tex, self._drect, self._srect)
    
    def getRect(self):
        self._drect.x = self.__pos.x
        self._drect.y = self.__pos.y
        return self._drect

    def getSize(self):
        return self.__size
    
    def getPos(self):
        return self.__pos
    
    def setPos(self, pos: PosLayerTuple):
        self.__pos = PosLayerTuple._make(pos)
    
    def getScene(self):
        return self._scene
    
    def setScene(self, scene: Scene):
        self._scene = scene
    
    def getTex(self):
        return self.__tex

class AnimatedDrawable(Drawable):
    def __init__(self, texture: pygame.image, size: SizeTuple, texPos: PosTuple, pos: PosLayerTuple):
        super().__init__(texture, size, (0, 0), pos)
        self.__texPositions = []
        texPosNamed = PosTuple._make(texPos)
        self.__texPositions.append(texPosNamed)
        self._srect.x = texPosNamed.x
        self._srect.y = texPosNamed.y
        self.__state: int = 0
    
    def addTexPosition(self, texPos: PosTuple):
        self.__texPositions.append(PosTuple._make(texPos))
    
    def removeTexPosition(self, texPos: PosTuple):
        self.__texPositions.remove(PosTuple._make(texPos))
    
    def getState(self):
        return self.__state
    
    def setState(self, state: int):
        if state > len(self.__texPositions):
            state = len(self.__texPositions)
        elif state < 0:
            state = 0
        self.__state = state
        self._srect.x = self.__texPositions[state].x
        self._srect.y = self.__texPositions[state].y

class Sprite(Drawable):
    def __init__(self, texture: pygame.image, size: SpriteSize, texPos: PosTuple, pos: PosLayerTuple):
        super().__init__(texture, (size.value, size.value), texPos, pos)

class AnimatedSprite(Sprite, AnimatedDrawable):
    def __init__(self, texture: pygame.image, size: SpriteSize, texPos: PosTuple, pos: PosLayerTuple):
        super().__init__(texture, size, texPos, pos)

class Background(Drawable):
    def __init__(self, texture: pygame.image, res: Resolution, texPos: PosTuple):
        super().__init__(texture, (res.sizeX(), res.sizeY()), texPos, (0, 0, 0))

class AnimatedBackground(Background, AnimatedDrawable):
    def __init__(self, texture: pygame.image, res: Resolution, texPos: PosTuple):
        super().__init__(texture, res, texPos, (0, 0, 0))