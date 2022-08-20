import sees
import sees.Scene as Sc
import pygame
import Tile as T

class Entity(T.Tile):
    def __init__(self, scene: Sc, pos: sees.PosLayerTuple):
        super().__init__(scene, pos)

    def createDrawable(self):
        tex = pygame.image.load(".//Sprites/AssetSet.png").convert_alpha()
        self._createDrawableSecond(tex)
    
    def _createDrawableSecond(self, tex):
        return

    def walkable(self):
        return True
    
    def moveable(self):
        return True

class EntityPlayer(Entity):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        pos = sees.PosTuple._make(pos)
        super().__init__(scene, (3, pos.x, pos.y))
        self.__orientation = T.TileFacing.SOUTH
        facingPos = sees.PosTuple._make(pos)
        facingPosY = facingPos.y + 16
        self.__facingRect = pygame.Rect((facingPos.x, facingPosY), (16, 16))
        self.__powerLevel = 3
    
    def createDrawable(self):
        tex = pygame.image.load(".//Sprites/MainCharacter.png").convert_alpha()
        drawable = sees.AnimatedSprite(tex, sees.SpriteSize.SPR_16x16, (0, 0), (3, self.getPos().x, self.getPos().y))
        drawable.addTexPosition((16, 0)) # SOUTH2 : 1
        drawable.addTexPosition((0, 16)) # EAST : 2
        drawable.addTexPosition((16, 16)) # EAST2 : 3
        drawable.addTexPosition((0, 32)) # WEST :  4
        drawable.addTexPosition((16, 32))# WEST2 : 5
        drawable.addTexPosition((0, 48)) # NORTH : 6
        drawable.addTexPosition((16, 48)) # NORTH2 : 7

        drawable.addTexPosition((32, 0)) #power SOUTH : 8
        drawable.addTexPosition((32, 16)) #power EAST : 9
        drawable.addTexPosition((32, 32)) #power WEST : 10
        drawable.addTexPosition((32, 48)) #power NORTH : 11

        self._drawable = self._scene.addDrawable(drawable)
    
    def move(self, direction: T.TileFacing):
        player = self._scene.getPlayer()
        pos = player.getPos()
        if player.getOrientation() == direction and self._scene.playerCanMove():
            if (direction == T.TileFacing.WEST and pos.x > 0 or
                direction == T.TileFacing.EAST and pos.x < 240 or
                direction == T.TileFacing.NORTH and pos.y > 0 or
                direction == T.TileFacing.SOUTH and pos.y < 208):
                for i in range(1, 17):
                    if direction == T.TileFacing.WEST:
                        player.setPos((pos.x - i, pos.y))
                    elif direction == T.TileFacing.EAST:
                        player.setPos((pos.x + i, pos.y))
                    elif direction == T.TileFacing.NORTH:
                        player.setPos((pos.x, pos.y - i))
                    elif direction == T.TileFacing.SOUTH:
                        player.setPos((pos.x, pos.y + i))
                    pygame.time.wait(5)
                    self._scene.redraw()
                player.changeFrame()
        else:
            player.setOrientation(direction)
    
    def setPowerLevel(self, level: int):
        if level < 1:
            level = 1
        if level > 3:
            level = 3
        self.__powerLevel = level
    
    def powerAttract(self):
        self._scene.stopRegisterInput()
        drawable = self._scene.getDrawable(self._drawable)
        if self.__orientation == T.TileFacing.NORTH:
            drawable.setState(11)
        elif self.__orientation == T.TileFacing.SOUTH:
            drawable.setState(8)
        elif self.__orientation == T.TileFacing.EAST:
            drawable.setState(9)
        elif self.__orientation == T.TileFacing.WEST:
            drawable.setState(10)
            
        entities = []
        nextPos = (self.__facingRect.x, self.__facingRect.y)
        blocked = False
        i = 1
        
        while (not blocked) and i < self.__powerLevel:
        #for i in range(1, self.__powerLevel):
            result = self.__createWindEntities(nextPos, entities, blocked, False, True)
            nextPos = result[0]
            entities = result[1]
            blocked = result[2]
            i += 1
        result = self.__createWindEntities(nextPos, entities, blocked, True, True)
        nextPos = result[0]
        entities = result[1]

        for entity in list(reversed(entities)):
            pos = entity.getPos()
            entity.removeDrawable()
            for tile in self._scene.getMoveableTiles():
                if tile.moveable() == True and entity.isCollidingNext(tile):
                    canMove = True
                    for hole in self._scene.getHoles():
                        if hole.isCollidingPos(pos) and (not hole.isFilled()) and (not isinstance(tile, EntitySecondaryCube)):
                            canMove = False
                    if canMove:
                        tile.setPos(pos)
                        if isinstance(tile, EntitySecondaryCube):
                            for hole in self._scene.getHoles():
                                if hole.isColliding(tile) and (not hole.isFilled()):
                                    hole.fill()
                                    tile.insert()
            pygame.time.wait(50)
        
        self.setOrientation(self.__orientation)
    
    def powerRepulse(self):
        self._scene.stopRegisterInput()
        drawable = self._scene.getDrawable(self._drawable)
        if self.__orientation == T.TileFacing.NORTH:
            drawable.setState(11)
        elif self.__orientation == T.TileFacing.SOUTH:
            drawable.setState(8)
        elif self.__orientation == T.TileFacing.EAST:
            drawable.setState(9)
        elif self.__orientation == T.TileFacing.WEST:
            drawable.setState(10)
            
        entities = []
        nextPos = (self.__facingRect.x, self.__facingRect.y)
        blocked = False
        i = 1
        
        while (not blocked) and i < self.__powerLevel:
        #for i in range(1, self.__powerLevel):
            result = self.__createWindEntities(nextPos, entities, blocked, False, False)
            nextPos = result[0]
            entities = result[1]
            blocked = result[2]
            i += 1
        result = self.__createWindEntities(nextPos, entities, blocked, True, False)
        entities = result[1]

        for entity in entities:
            entity.removeDrawable()
            pygame.time.wait(50)
        
        self.setOrientation(self.__orientation)
        
        self._scene.registerInput()
    
    def __createWindEntities(self, nextPos, entities, blocked, final, attract):
        for tile in self._scene.getBlockingTiles():
            if tile.isCollidingPos(nextPos) and (not isinstance(tile, T.Hole)) and (not isinstance(tile, EntitySecondaryCube)) and (not tile.walkable()):
                if attract:
                    blocked = True
                elif (not tile.moveable()):
                    blocked = True
        if not blocked:
            entity = EntityWind(self._scene, nextPos, self.__orientation, final, attract)
            entity.createDrawable()
            nextPos = entity.getNextPos()
            if attract == False:
                for tile in self._scene.getMoveableTiles():
                    if tile.moveable() and entity.isColliding(tile):
                        canMove = True
                        for blocking in self._scene.getBlockingTiles():
                            if (not blocking.walkable()) and entity.isCollidingNext(blocking):
                                if not (isinstance(tile, EntitySecondaryCube) and isinstance(blocking, T.Hole) and not blocking.isFilled()):
                                    canMove = False
                        if canMove:
                            tile.setPos(nextPos)
                            if isinstance(tile, EntitySecondaryCube):
                                for hole in self._scene.getHoles():
                                    if hole.isColliding(tile) and (not hole.isFilled()):
                                        hole.fill()
                                        tile.insert()
            self._scene.redraw()
            pygame.time.wait(50)
            entities.append(entity)
        return (nextPos, entities, blocked)

    def setPos(self, pos: sees.PosTuple):
        super().setPos(pos)
        self.__setFacingRect(pos)

    def getFacing(self):
        return self.__facingRect
    
    def isCollidingFace(self, tile: T.Tile):
        return self.__facingRect.colliderect(tile.getRect())

    def __setFacingRect(self, pos: sees.PosTuple):
        facingPos = sees.PosTuple._make(pos)
        if self.__orientation == T.TileFacing.NORTH:
            facingPos = (facingPos.x, facingPos.y - 16)
        elif self.__orientation == T.TileFacing.SOUTH:
            facingPos = (facingPos.x, facingPos.y + 16)
        elif self.__orientation == T.TileFacing.EAST:
            facingPos = (facingPos.x + 16, facingPos.y)
        elif self.__orientation == T.TileFacing.WEST:
            facingPos = (facingPos.x - 16, facingPos.y)
        self.__facingRect = pygame.Rect(facingPos, (16, 16))
    
    def setOrientation(self, orientation: T.TileFacing):
        self.__orientation = orientation
        drawable = self._scene.getDrawable(self._drawable)
        if orientation == T.TileFacing.NORTH:
            drawable.setState(6)
        elif orientation == T.TileFacing.SOUTH:
            drawable.setState(0)
        elif orientation == T.TileFacing.EAST:
            drawable.setState(2)
        elif orientation == T.TileFacing.WEST:
            drawable.setState(4)
        self.__setFacingRect(self.getPos())
    
    def getOrientation(self):
        return self.__orientation
    
    def changeFrame(self):
        drawable = self._scene.getDrawable(self._drawable)
        state = drawable.getState()
        if self.__orientation == T.TileFacing.NORTH:
            drawable.setState(7 if state == 6 else 6)
        elif self.__orientation == T.TileFacing.SOUTH:
            drawable.setState(1 if state == 0 else 0)
        elif self.__orientation == T.TileFacing.EAST:
            drawable.setState(3 if state == 2 else 2)
        elif self.__orientation == T.TileFacing.WEST:
            drawable.setState(5 if state == 4 else 4)

class EntityCube(Entity):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        pos = sees.PosTuple._make(pos)
        super().__init__(scene, (2, pos.x, pos.y))
    
    def _createDrawableSecond(self, tex):
        drawable = sees.AnimatedSprite(tex, sees.SpriteSize.SPR_16x16, (0, 176), (2, self.getPos().x, self.getPos().y))
        drawable.addTexPosition((16, 176))
        self._drawable = self._scene.addDrawable(drawable)
        
    def walkable(self):
        return False
    
    def blinks(self):
        return True
    
    def changeSprite(self):
        drawable = self._scene.getDrawable(self._drawable)
        if (drawable.getState() == 1):
            drawable.setState(0)
        else:
            drawable.setState(1)

class EntityWind(Entity):
    def __init__(self, scene: Sc, pos: sees.PosTuple, orientation: T.TileFacing, final: bool, attract: bool):
        pos = sees.PosTuple._make(pos)
        super().__init__(scene, (2, pos.x, pos.y))
        self.__orientation = orientation
        self.__final = final
        self.__attract = attract
        self.__nextPos = sees.PosTuple._make(pos)
        if self.__orientation == T.TileFacing.NORTH:
            self.__nextPos = (self.__nextPos.x, self.__nextPos.y - 16)
        elif self.__orientation == T.TileFacing.SOUTH:
            self.__nextPos = (self.__nextPos.x, self.__nextPos.y + 16)
        elif self.__orientation == T.TileFacing.EAST:
            self.__nextPos = (self.__nextPos.x + 16, self.__nextPos.y)
        elif self.__orientation == T.TileFacing.WEST:
            self.__nextPos = (self.__nextPos.x - 16, self.__nextPos.y)
        self.__nextRect = pygame.Rect(self.__nextPos, (16, 16))
    
    def getNextPos(self):
        return self.__nextPos
    
    def createDrawable(self):
        tex = pygame.image.load(".//Sprites/MainCharacter.png").convert_alpha()
        pos = (0, 0)
        if self.__orientation == T.TileFacing.NORTH:
            if self.__attract:
                if self.__final: pos = (96, 48)
                else: pos = (80, 48)
            else:
                if self.__final: pos = (64, 48)
                else: pos = (48, 48)
        elif self.__orientation == T.TileFacing.SOUTH:
            if self.__attract:
                if self.__final: pos = (96, 0)
                else: pos = (80, 0)
            else:
                if self.__final: pos = (64, 0)
                else: pos = (48, 0)
        elif self.__orientation == T.TileFacing.EAST:
            if self.__attract:
                if self.__final: pos = (96, 16)
                else: pos = (80, 16)
            else:
                if self.__final: pos = (64, 16)
                else: pos = (48, 16)
        elif self.__orientation == T.TileFacing.WEST:
            if self.__attract:
                if self.__final: pos = (96, 32)
                else: pos = (80, 32)
            else:
                if self.__final: pos = (64, 32)
                else: pos = (48, 32)
        self._drawable = self._scene.addDrawable(sees.Sprite(tex, sees.SpriteSize.SPR_16x16, pos, (2, self.getPos().x, self.getPos().y)))
        self._scene.redraw()

    def removeDrawable(self):
        self._scene.removeDrawable(self._drawable)
        self._scene.redraw()
    
    def moveable(self):
        return False
    
    def isCollidingNext(self, tile):
        return self.__nextRect.colliderect(tile.getRect())

class ExitDoor(T.Tile):
    def __init__(self, scene: Sc, pos: sees.PosTuple, orientation: T.TileFacing):
        self._orientation = orientation
        pos = sees.PosTuple._make(pos)
        super().__init__(scene, (0, pos.x, pos.y))
        self.__opened = False

    def createDrawable(self):
        tex = pygame.image.load(".//Sprites//TileSet.png").convert_alpha()
        if self._orientation == T.TileFacing.NORTH:
            drawable = sees.AnimatedSprite(tex, sees.SpriteSize.SPR_16x16, (32, 128), (0, self.getPos().x, self.getPos().y))
            drawable.addTexPosition((48, 128))
        elif self._orientation == T.TileFacing.SOUTH:
            drawable = sees.AnimatedSprite(tex, sees.SpriteSize.SPR_16x16, (96, 128), (0, self.getPos().x, self.getPos().y))
            drawable.addTexPosition((112, 128))
        elif self._orientation == T.TileFacing.WEST:
            drawable = sees.AnimatedSprite(tex, sees.SpriteSize.SPR_16x16, (64, 128), (0, self.getPos().x, self.getPos().y))
            drawable.addTexPosition((80, 128))
        elif self._orientation == T.TileFacing.EAST:
            drawable = sees.AnimatedSprite(tex, sees.SpriteSize.SPR_16x16, (0, 128), (0, self.getPos().x, self.getPos().y))
            drawable.addTexPosition((16, 128))
        drawable.addTexPosition((16, 0))
        self._drawable = self._scene.addDrawable(drawable)
    
    def blinks(self):
        return True
    
    def getOpened(self):
        return self.__opened
    
    def setOpened(self, opened: bool):
        self.__opened = opened
        drawable = self._scene.getDrawable(self._drawable)
        if opened:
            drawable.setState(2)
        else:
            drawable.setState(0)
    
    def changeSprite(self):
        if self.__opened == False:
            drawable = self._scene.getDrawable(self._drawable)
            if (drawable.getState() == 1):
                drawable.setState(0)
            else:
                drawable.setState(1)
    
    def walkable(self):
        return self.__opened

class LightBarrier(T.Tile):
    def __init__(self, scene: Sc, pos: sees.PosTuple, vertical: bool):
        pos = sees.PosTuple._make(pos)
        super().__init__(scene, (0, pos.x, pos.y))
        self.__opened = False
        self.__vertical = vertical

    def createDrawable(self):
        tex = pygame.image.load(".//Sprites//AssetSet.png").convert_alpha()
        if self.__vertical:
            drawable = sees.AnimatedSprite(tex, sees.SpriteSize.SPR_16x16, (0, 128), (0, self.getPos().x, self.getPos().y))
            drawable.addTexPosition((16, 128))
            drawable.addTexPosition((16, 48))
        else:
            drawable = sees.AnimatedSprite(tex, sees.SpriteSize.SPR_16x16, (0, 144), (0, self.getPos().x, self.getPos().y))
            drawable.addTexPosition((16, 144))
            drawable.addTexPosition((0, 48))
        self._drawable = self._scene.addDrawable(drawable)
    
    def blinks(self):
        return True
    
    def getOpened(self):
        return self.__opened
    
    def setOpened(self, opened: bool):
        self.__opened = opened
        drawable = self._scene.getDrawable(self._drawable)
        if opened:
            drawable.setState(2)
        else:
            drawable.setState(0)
    
    def changeSprite(self):
        if self.__opened == False:
            drawable = self._scene.getDrawable(self._drawable)
            if (drawable.getState() == 1):
                drawable.setState(0)
            else:
                drawable.setState(1)
    
    def walkable(self):
        return self.__opened


class OnePushButton(T.Tile):
    def __init__(self, scene: Sc, pos: sees.PosTuple, barrier: LightBarrier):
        pos = sees.PosTuple._make(pos)
        super().__init__(scene, (0, pos.x, pos.y))
        self.__pushed = False
        self.__barrier = barrier

    def createDrawable(self):
        tex = pygame.image.load(".//Sprites//AssetSet.png").convert_alpha()
        drawable = sees.AnimatedSprite(tex, sees.SpriteSize.SPR_16x16, (16, 0), (1, self.getPos().x, self.getPos().y))
        drawable.addTexPosition((32, 0))
        self._drawable = self._scene.addDrawable(drawable)
    
    def isPushed(self):
        return self.__pushed
    
    def push(self):
        self.__pushed = True
        self._scene.getDrawable(self._drawable).setState(1)
        if self.__barrier != None:
            self.__barrier.setOpened(True)

class EntitySecondaryCube(Entity):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        pos = sees.PosTuple._make(pos)
        super().__init__(scene, (2, pos.x, pos.y))
        self.__inserted = False
    
    def _createDrawableSecond(self, tex):
        self._drawable = self._scene.addDrawable(sees.Sprite(tex, sees.SpriteSize.SPR_16x16, (0, 16), (2, self.getPos().x, self.getPos().y)))
    
    def walkable(self):
        return self.__inserted
    
    def moveable(self):
        return (self.__inserted == False)
    
    def insert(self):
        self.__inserted = True

class EntityBoss1(Entity):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        pos = sees.PosTuple._make(pos)
        super().__init__(scene, (3, pos.x, pos.y))
        self.__inserted = False
        self.__killed = False
    
    def _createDrawableSecond(self, tex):
        drawable = sees.AnimatedSprite(tex, sees.SpriteSize.SPR_32x32, (0, 192), (1, self.getPos().x, self.getPos().y))
        drawable.addTexPosition((32, 192))
        self._drawable = self._scene.addDrawable(drawable)
    
    def blinks(self):
        return True
    
    def moveable(self):
        return False
    
    def changeSprite(self):
        if not self.__killed:
            drawable = self._scene.getDrawable(self._drawable)
            if (drawable.getState() == 1):
                drawable.setState(0)
            else:
                drawable.setState(1)
    
    def kill(self):
        self._scene.removeDrawable(self._drawable)
        self.__killed = True

class AirCannon(Entity):
    def __init__(self, scene: Sc, pos: sees.PosTuple):
        pos = sees.PosTuple._make(pos)
        super().__init__(scene, (0, pos.x, pos.y))
        self._air = None
        facingPos = sees.PosTuple._make(pos)
        facingPos = (facingPos.x, facingPos.y - 16)
        self._facingPos = facingPos

    def createDrawable(self):
        tex = pygame.image.load(".//Sprites//AssetSet.png").convert_alpha()
        drawable = sees.AnimatedSprite(tex, sees.SpriteSize.SPR_16x16, (0, 160), (1, self.getPos().x, self.getPos().y))
        drawable.addTexPosition((16, 160))
        self._drawable = self._scene.addDrawable(drawable)
    
    def blinks(self):
        return True
    
    def walkable(self):
        return False
    
    def moveable(self):
        return False
    
    def changeSprite(self):
        drawable = self._scene.getDrawable(self._drawable)
        if (drawable.getState() == 1):
            drawable.setState(0)
        else:
            drawable.setState(1)

    def enableAir(self):
        self._air = EntityWind(self._scene, self._facingPos, T.TileFacing.NORTH, True, False)
        self._air.createDrawable()
    
    def disableAir(self):
        self._air.removeDrawable()