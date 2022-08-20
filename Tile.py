import sees
import sees.Scene as Sc
import pygame
from enum import Enum

class TileFacing(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4

class Tile:
    def __init__(self, scene: Sc, pos: sees.PosLayerTuple):
        self._scene = scene
        self._drawable = None
        pos = sees.PosLayerTuple._make(pos)
        self.__pos = pos
        self.__rect = pygame.Rect((self.__pos.x, self.__pos.y), (16, 16))

    def createDrawable(self):
        return

    def getPos(self):
        return sees.PosTuple._make((self.__pos[1], self.__pos[2]))
    
    def setPos(self, pos: sees.PosTuple):
        pos = sees.PosTuple._make(pos)
        self.__pos = (self.__pos[0], pos.x, pos.y)
        self.__rect = pygame.Rect(pos, (16, 16))
        self._scene.getDrawable(self._drawable).setPos(self.__pos)
    
    def getDrawable(self):
        return self._drawable
    
    def getRect(self):
        return self.__rect
    
    def walkable(self):
        return True
    
    def moveable(self):
        return False
    
    def blinks(self):
        return False
    
    def isColliding(self, tile):
        return self.__rect.colliderect(tile.getRect())
    
    def isCollidingPos(self, pos: sees.PosTuple):
        return self.__rect.colliderect(pygame.Rect(pos, (16, 16)))

class BoxButton(Tile):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        pos = sees.PosTuple._make(pos)
        super().__init__(scene, (0, pos.x, pos.y))

    def createDrawable(self):
        tex = pygame.image.load(".//Sprites//TileSet.png").convert_alpha()
        drawable = sees.AnimatedSprite(tex, sees.SpriteSize.SPR_16x16, (0, 144), (0, self.getPos().x, self.getPos().y))
        drawable.addTexPosition((16, 144))
        self._drawable = self._scene.addDrawable(drawable)
    
    def blinks(self):
        return True
    
    def changeSprite(self):
        drawable = self._scene.getDrawable(self._drawable)
        if (drawable.getState() == 1):
            drawable.setState(0)
        else:
            drawable.setState(1)

###################### CLASS NON ANIMER #############################

class Ground(Tile):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        pos = sees.PosTuple._make(pos)
        super().__init__(scene,(0, pos.x, pos.y))

    def createDrawable(self):
        tex = pygame.image.load(".//Sprites//TileSet.png").convert_alpha()
        self._drawable = self._scene.addDrawable(sees.Sprite(tex, sees.SpriteSize.SPR_16x16, (0, 0), (0, self.getPos().x, self.getPos().y)))

class Hole(Tile):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        pos = sees.PosTuple._make(pos)
        self.__filled = False
        super().__init__(scene, (0, pos.x, pos.y))

    def createDrawable(self):
        tex = pygame.image.load(".//Sprites//TileSet.png").convert_alpha()
        self._drawable = self._scene.addDrawable(sees.Sprite(tex, sees.SpriteSize.SPR_16x16, (48, 0), (0, self.getPos().x, self.getPos().y)))

    def isFilled(self):
        return self.__filled
    
    def fill(self):
        self.__filled = True

    def walkable(self):
        return self.__filled

class AfficheRouge(Tile):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        pos = sees.PosTuple._make(pos)
        super().__init__(scene, (0, pos.x, pos.y))

    def createDrawable(self):
        tex = pygame.image.load(".//Sprites//AssetSet.png").convert_alpha()
        self._drawable = self._scene.addDrawable(sees.Sprite(tex, sees.SpriteSize.SPR_16x16, (48, 0), (1, self.getPos().x, self.getPos().y)))

class DoublePapier(Tile):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        pos = sees.PosTuple._make(pos)
        super().__init__(scene, (0, pos.x, pos.y))

    def createDrawable(self):
        tex = pygame.image.load(".//Sprites//AssetSet.png").convert_alpha()
        self._drawable = self._scene.addDrawable(sees.Sprite(tex, sees.SpriteSize.SPR_16x16, (64, 0), (1, self.getPos().x, self.getPos().y)))

class Flaque(Tile):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        pos = sees.PosTuple._make(pos)
        super().__init__(scene, (0, pos.x, pos.y))

    def createDrawable(self):
        tex = pygame.image.load(".//Sprites//AssetSet.png").convert_alpha()
        self._drawable = self._scene.addDrawable(sees.Sprite(tex, sees.SpriteSize.SPR_16x16, (80, 0), (1, self.getPos().x, self.getPos().y)))

class SimplePapier(Tile):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        pos = sees.PosTuple._make(pos)
        super().__init__(scene, (0, pos.x, pos.y))

    def createDrawable(self):
        tex = pygame.image.load(".//Sprites//AssetSet.png").convert_alpha()
        self._drawable = self._scene.addDrawable(sees.Sprite(tex, sees.SpriteSize.SPR_16x16, (96, 0), (1, self.getPos().x, self.getPos().y)))

class ArmoirFermerHaut(Tile):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        pos = sees.PosTuple._make(pos)
        super().__init__(scene, (0, pos.x, pos.y))

    def createDrawable(self):
        tex = pygame.image.load(".//Sprites//AssetSet.png").convert_alpha()
        self._drawable = self._scene.addDrawable(sees.Sprite(tex, sees.SpriteSize.SPR_16x16, (16, 16), (1, self.getPos().x, self.getPos().y)))

    def walkable(self):
        return False

class ArmoirFermerBas(Tile):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        pos = sees.PosTuple._make(pos)
        super().__init__(scene, (0, pos.x, pos.y))

    def createDrawable(self):
        tex = pygame.image.load(".//Sprites//AssetSet.png").convert_alpha()
        self._drawable = self._scene.addDrawable(sees.Sprite(tex, sees.SpriteSize.SPR_16x16, (16, 32), (1, self.getPos().x, self.getPos().y)))

class ArmoirOuvertHaut(Tile):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        pos = sees.PosTuple._make(pos)
        super().__init__(scene, (0, pos.x, pos.y))

    def createDrawable(self):
        tex = pygame.image.load(".//Sprites//AssetSet.png").convert_alpha()
        self._drawable = self._scene.addDrawable(sees.Sprite(tex, sees.SpriteSize.SPR_16x16, (32, 16), (1, self.getPos().x, self.getPos().y)))

    def walkable(self):
        return False

class ArmoirOuvertBas(Tile):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        pos = sees.PosTuple._make(pos)
        super().__init__(scene, (0, pos.x, pos.y))

    def createDrawable(self):
        tex = pygame.image.load(".//Sprites//AssetSet.png").convert_alpha()
        self._drawable = self._scene.addDrawable(sees.Sprite(tex, sees.SpriteSize.SPR_16x16, (32, 32), (1, self.getPos().x, self.getPos().y)))

class ArmoirDosHaut(Tile):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        pos = sees.PosTuple._make(pos)
        super().__init__(scene, (0, pos.x, pos.y))

    def createDrawable(self):
        tex = pygame.image.load(".//Sprites//AssetSet.png").convert_alpha()
        self._drawable = self._scene.addDrawable(sees.Sprite(tex, sees.SpriteSize.SPR_16x16, (32, 48), (1, self.getPos().x, self.getPos().y)))

    def walkable(self):
        return False

class ArmoirDosBas(Tile):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        pos = sees.PosTuple._make(pos)
        super().__init__(scene, (0, pos.x, pos.y))

    def createDrawable(self):
        tex = pygame.image.load(".//Sprites//AssetSet.png").convert_alpha()
        self._drawable = self._scene.addDrawable(sees.Sprite(tex, sees.SpriteSize.SPR_16x16, (32, 64), (1, self.getPos().x, self.getPos().y)))

class Cartons(Tile):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        pos = sees.PosTuple._make(pos)
        super().__init__(scene, (0, pos.x, pos.y))

    def createDrawable(self):
        tex = pygame.image.load(".//Sprites//AssetSet.png").convert_alpha()
        self._drawable = self._scene.addDrawable(sees.Sprite(tex, sees.SpriteSize.SPR_16x16, (48, 16), (1, self.getPos().x, self.getPos().y)))

class AffichageRougePencher(Tile):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        pos = sees.PosTuple._make(pos)
        super().__init__(scene, (0, pos.x, pos.y))

    def createDrawable(self):
        tex = pygame.image.load(".//Sprites//AssetSet.png").convert_alpha()
        self._drawable = self._scene.addDrawable(sees.Sprite(tex, sees.SpriteSize.SPR_16x16, (64, 16), (1, self.getPos().x, self.getPos().y)))

class Chaise(Tile):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        pos = sees.PosTuple._make(pos)
        super().__init__(scene, (0, pos.x, pos.y))

    def createDrawable(self):
        tex = pygame.image.load(".//Sprites//AssetSet.png").convert_alpha()
        self._drawable = self._scene.addDrawable(sees.Sprite(tex, sees.SpriteSize.SPR_16x16, (0, 32), (1, self.getPos().x, self.getPos().y)))
    
    def walkable(self):
        return False

class BureauDos(Tile):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        pos = sees.PosTuple._make(pos)
        super().__init__(scene, (0, pos.x, pos.y))
    
    def createDrawable(self):
        tex = pygame.image.load(".//Sprites//AssetSet.png").convert_alpha()
        self._drawable = self._scene.addDrawable(sees.Sprite(tex, sees.SpriteSize.SPR_16x16, (48, 48), (1, self.getPos().x, self.getPos().y)))
    
    def walkable(self):
        return False

################### CLASS ANIMATION ##########################3333

class FeuEteint(Tile):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        pos = sees.PosTuple._make(pos)
        super().__init__(scene, (0, pos.x, pos.y))
    
    def createDrawable(self):
        tex = pygame.image.load(".//Sprites//AssetSet.png").convert_alpha()
        drawable = sees.AnimatedSprite(tex, sees.SpriteSize.SPR_16x16, (32, 144), (1, self.getPos().x, self.getPos().y))
        drawable.addTexPosition((48, 144))
        self._drawable = self._scene.addDrawable(drawable)
    
    def blinks(self):
        return True
    
    def changeSprite(self):
        drawable = self._scene.getDrawable(self._drawable)
        if (drawable.getState() == 1):
            drawable.setState(0)
        else:
            drawable.setState(1)

    def walkable(self):
        return False

class FeuAllumer(Tile):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        pos = sees.PosTuple._make(pos)
        super().__init__(scene, (0, pos.x, pos.y))

    def createDrawable(self):
        tex = pygame.image.load(".//Sprites//AssetSet.png").convert_alpha()
        drawable = sees.AnimatedSprite(tex, sees.SpriteSize.SPR_16x16, (32, 128), (1, self.getPos().x, self.getPos().y))
        drawable.addTexPosition((48, 128))
        self._drawable = self._scene.addDrawable(drawable)
    
    def blinks(self):
        return True
    
    def changeSprite(self):
        drawable = self._scene.getDrawable(self._drawable)
        if (drawable.getState() == 1):
            drawable.setState(0)
        else:
            drawable.setState(1)

    def walkable(self):
        return False

class BureauDroite(Tile):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        pos = sees.PosTuple._make(pos)
        super().__init__(scene, (0, pos.x, pos.y))

    def createDrawable(self):
        tex = pygame.image.load(".//Sprites//AssetSet.png").convert_alpha()
        drawable = sees.AnimatedSprite(tex, sees.SpriteSize.SPR_16x16, (64, 128), (1, self.getPos().x, self.getPos().y))
        drawable.addTexPosition((80, 128))
        self._drawable = self._scene.addDrawable(drawable)
    
    def blinks(self):
        return True
    
    def changeSprite(self):
        drawable = self._scene.getDrawable(self._drawable)
        if (drawable.getState() == 1):
            drawable.setState(0)
        else:
            drawable.setState(1)

    def walkable(self):
        return False

class BureauGauche(Tile):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        pos = sees.PosTuple._make(pos)
        super().__init__(scene, (0, pos.x, pos.y))

    def createDrawable(self):
        tex = pygame.image.load(".//Sprites//AssetSet.png").convert_alpha()
        drawable = sees.AnimatedSprite(tex, sees.SpriteSize.SPR_16x16, (96, 128), (1, self.getPos().x, self.getPos().y))
        drawable.addTexPosition((112, 128))
        self._drawable = self._scene.addDrawable(drawable)
    
    def blinks(self):
        return True
    
    def changeSprite(self):
        drawable = self._scene.getDrawable(self._drawable)
        if (drawable.getState() == 1):
            drawable.setState(0)
        else:
            drawable.setState(1)

    def walkable(self):
        return False

class BureauFace(Tile):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        pos = sees.PosTuple._make(pos)
        super().__init__(scene, (0, pos.x, pos.y))

    def createDrawable(self):
        tex = pygame.image.load(".//Sprites//AssetSet.png").convert_alpha()
        drawable = sees.AnimatedSprite(tex, sees.SpriteSize.SPR_16x16, (64, 144), (1, self.getPos().x, self.getPos().y))
        drawable.addTexPosition((80, 144))
        self._drawable = self._scene.addDrawable(drawable)
    
    def blinks(self):
        return True
    
    def changeSprite(self):
        drawable = self._scene.getDrawable(self._drawable)
        if (drawable.getState() == 1):
            drawable.setState(0)
        else:
            drawable.setState(1)

    def walkable(self):
        return False

class EntryDoor(Tile):
    def __init__(self, scene: Sc, pos: sees.PosTuple, orientation: TileFacing):
        self._orientation=orientation
        pos = sees.PosTuple._make(pos)
        super().__init__(scene, (0, pos.x, pos.y))
        
    def createDrawable(self):
        tex = pygame.image.load(".//Sprites//TileSet.png").convert_alpha()
        if self._orientation == TileFacing.NORTH:
            drawable = sees.Sprite(tex, sees.SpriteSize.SPR_16x16, (48, 64), (0, self.getPos().x, self.getPos().y))
        elif self._orientation == TileFacing.SOUTH:
            drawable = sees.Sprite(tex, sees.SpriteSize.SPR_16x16, (16, 64), (0, self.getPos().x, self.getPos().y))
        elif self._orientation == TileFacing.WEST:
            drawable = sees.Sprite(tex, sees.SpriteSize.SPR_16x16, (0, 64), (0, self.getPos().x, self.getPos().y))
        elif self._orientation == TileFacing.EAST:
            drawable = sees.Sprite(tex, sees.SpriteSize.SPR_16x16, (32, 64), (0, self.getPos().x, self.getPos().y))
        self._drawable = self._scene.addDrawable(drawable)