import sees
import sees.Scene as Sc
import pygame
from Tile import Tile
from enum import Enum

class WallType(Enum):
    TOP_LEFT = 1
    TOP_RIGHT = 2
    BOTTOM_LEFT = 3
    BOTTOM_RIGHT = 4
    TOP = 5
    BOTTOM = 6
    LEFT = 7
    RIGHT = 8

class Wall(Tile):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        pos = sees.PosTuple._make(pos)
        super().__init__(scene, (0, pos.x, pos.y))
    
    def createDrawable(self):
        tex = pygame.image.load(".//Sprites//TileSet.png").convert_alpha()
        self._createDrawableSecond(tex)
    
    def _createDrawableSecond(self, tex):
        return

    def walkable(self):
        return False

class WallTop(Wall):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        super().__init__(scene, pos)

    def _createDrawableSecond(self, tex):
        self._drawable = self._scene.addDrawable(sees.Sprite(tex, sees.SpriteSize.SPR_16x16, (0, 48), (0, self.getPos().x, self.getPos().y)))

class WallRight(Wall):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        super().__init__(scene, pos)
        
    def _createDrawableSecond(self, tex):
        self._drawable = self._scene.addDrawable(sees.Sprite(tex, sees.SpriteSize.SPR_16x16, (16, 48), (0, self.getPos().x, self.getPos().y)))

class WallLeft(Wall):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        super().__init__(scene, pos)
        
    def _createDrawableSecond(self, tex):
        self._drawable = self._scene.addDrawable(sees.Sprite(tex, sees.SpriteSize.SPR_16x16, (32, 48), (0, self.getPos().x, self.getPos().y)))
    
class WallBottom(Wall):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        super().__init__(scene, pos)
        
    def _createDrawableSecond(self, tex):
        self._drawable = self._scene.addDrawable(sees.Sprite(tex, sees.SpriteSize.SPR_16x16, (48, 48), (0, self.getPos().x, self.getPos().y)))

class WallTopLeftIn(Wall):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        super().__init__(scene, pos)
        
    def _createDrawableSecond(self, tex):
        self._drawable = self._scene.addDrawable(sees.Sprite(tex, sees.SpriteSize.SPR_16x16, (0, 16), (0, self.getPos().x, self.getPos().y)))

class WallTopRightIn(Wall):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        super().__init__(scene, pos)
        
    def _createDrawableSecond(self, tex):
        self._drawable = self._scene.addDrawable(sees.Sprite(tex, sees.SpriteSize.SPR_16x16, (16, 16), (0, self.getPos().x, self.getPos().y)))

class WallBottomLeftIn(Wall):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        super().__init__(scene, pos)
        
    def _createDrawableSecond(self, tex):
        self._drawable = self._scene.addDrawable(sees.Sprite(tex, sees.SpriteSize.SPR_16x16, (0, 32), (0, self.getPos().x, self.getPos().y)))

class WallBottomRightIn(Wall):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        super().__init__(scene, pos)
        
    def _createDrawableSecond(self, tex):
        self._drawable = self._scene.addDrawable(sees.Sprite(tex, sees.SpriteSize.SPR_16x16, (16, 32), (0, self.getPos().x, self.getPos().y)))

class WallTopLeftOut(Wall):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        super().__init__(scene, pos)
        
    def _createDrawableSecond(self, tex):
        self._drawable = self._scene.addDrawable(sees.Sprite(tex, sees.SpriteSize.SPR_16x16, (32, 16), (0, self.getPos().x, self.getPos().y)))

class WallTopRightOut(Wall):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        super().__init__(scene, pos)
        
    def _createDrawableSecond(self, tex):
        self._drawable = self._scene.addDrawable(sees.Sprite(tex, sees.SpriteSize.SPR_16x16, (48, 16), (0, self.getPos().x, self.getPos().y)))

class WallBottomLeftOut(Wall):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        super().__init__(scene, pos)
        
    def _createDrawableSecond(self, tex):
        self._drawable = self._scene.addDrawable(sees.Sprite(tex, sees.SpriteSize.SPR_16x16, (32, 32), (0, self.getPos().x, self.getPos().y)))

class WallBottomRightOut(Wall):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        super().__init__(scene, pos)
        
    def _createDrawableSecond(self, tex):
        self._drawable = self._scene.addDrawable(sees.Sprite(tex, sees.SpriteSize.SPR_16x16, (48, 32), (0, self.getPos().x, self.getPos().y)))

class WallBlock(Wall):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        super().__init__(scene, pos)
        
    def _createDrawableSecond(self, tex):
        self._drawable = self._scene.addDrawable(sees.Sprite(tex, sees.SpriteSize.SPR_16x16, (32, 0), (0, self.getPos().x, self.getPos().y)))