import pygame
import sees
import sees.Scene as Sc
import Walls
import Entity as E
import Tile as T
from enum import Enum
from sees.TupleEnumTypes import SceneState
import Menu as M

class DecoTypes(Enum):
    AFFICHE_ROUGE = 1
    DOUBLE_PAPIER = 2
    FLAQUE = 3
    SIMPLE_PAPIER = 4
    ARMOIRE_FERMEE_HAUT = 5
    ARMOIRE_FERMEE_BAS = 6
    ARMOIRE_OUVERTE_HAUT = 7
    ARMOIRE_OUVERTE_BAS = 8
    ARMOIRE_DOS_HAUT = 9
    ARMOIRE_DOS_BAS = 10
    CARTONS = 11
    AFFICHE_ROUGE_PENCHEE = 12
    CHAISE = 13
    BUREAU_DOS = 14
    BUREAU_DROITE = 15
    BUREAU_GAUCHE = 16
    BUREAU_FACE = 17

class GameScene(Sc.Scene):
    def __init__(self, playerPos: sees.PosTuple, boxButtonPos: sees.PosTuple, endboxPos: sees.PosTuple, exitPos: sees.PosTuple, exitOrientation: T.TileFacing):
        super().__init__(sees.Resolution.RES_256x224, 60)
        self._tiles = []
        self._blocking = []
        self._blinking = []
        self._holes = []
        self._buttons = []
        self._moveable = []
        self._aircannons = []
        self._playMusic=False
        self._frame = 0
        self._player = E.EntityPlayer(self, playerPos)
        self._door = E.ExitDoor(self, exitPos, exitOrientation)
        self._boxbutton = T.BoxButton(self, boxButtonPos)
        self._endbox = E.EntityCube(self, endboxPos)
        
    def createDrawables(self):
        self._backgroundSound = self.getBackgroundSound(self.getLevel())
        self._backgroundSound.set_volume(0.8)
        self._backgroundSound.play(loops=-1, maxtime=0, fade_ms=0)
        self._player.createDrawable()
        self._tiles.append(self._door)
        self._blinking.append(self._door)
        self._blocking.append(self._door)
        self._tiles.append(self._boxbutton)
        self._blinking.append(self._boxbutton)
        self._tiles.append(self._endbox)
        self._blinking.append(self._endbox)
        self._blocking.append(self._endbox)
        self._moveable.append(self._endbox)
        for tile in self._tiles:
            tile.createDrawable()
    
    def getBlockingTiles(self):
        return self._blocking
    
    def musicOff(self):
        self._backgroundSound.stop()

    def getMoveableTiles(self):
        return self._moveable
    
    def getHoles(self):
        return self._holes

    def restartScene(self):
        return

    def logic(self):
        self._frame = self._frame + 1
        for tile in self._blinking:
            if tile.blinks() == True and self._frame == 30:
                tile.changeSprite()
        for button in self._buttons:
            if self._player.isColliding(button) and button.isPushed() == False:
                Sound= pygame.mixer.Sound("SoundTrack/Bouton_1.wav")
                Sound.play()
                button.push()
        if self._boxbutton.isColliding(self._endbox) and self._door.getOpened() == False:
            Sound= pygame.mixer.Sound("SoundTrack/Accomplished_3.wav")
            Sound.play()
            self._door.setOpened(True)

        elif self._boxbutton.isColliding(self._endbox) == False and self._door.getOpened():
            self._door.setOpened(False)
        if self._frame == 30:
            self._frame = 0
        self.mapLogic()
    
    def ReturnToMenu(self):
        self._nextScene = M.Menu()
        self.musicOff()
        self.setState(SceneState.CHANGE_SCENE)
    
    def mapLogic(self):
        return

    def getPlayer(self):
        return self._player

    def getLevel(self):
        return self.level
    
    def getExitDoor(self):
        return self._exit
    
    def playerCanMove(self):
        canMove = True
        i = 0
        while canMove and i < len(self._blocking):
            tile = self._blocking[i]
            if self._player.isCollidingFace(tile) and tile.walkable() == False:
                canMove = False
            i += 1
        return canMove

    def getBackgroundSound(self, level):
        if level=="0-1":
            return pygame.mixer.Sound("SoundTrack/Main_theme_1.ogg")
        if level=="1-1":
            return pygame.mixer.Sound("SoundTrack/Main_theme_1.ogg")
        if level=="1-2":
            return pygame.mixer.Sound("SoundTrack/Main_theme_1.ogg")
        if level=="1-3":
            return pygame.mixer.Sound("SoundTrack/Final_boss.ogg")
        if level=="1-3-2":
            return pygame.mixer.Sound("SoundTrack/Final_boss.ogg")
        if level=="1-3-3":
            return pygame.mixer.Sound("SoundTrack/Final_boss.ogg")
    
    
    def addWall(self, pos: sees.PosTuple, orientation: Walls.WallType, inner: bool):
        wall = None
        if orientation == Walls.WallType.TOP_LEFT:
            if inner:
                wall = Walls.WallTopLeftIn(self, pos)
            else:
                wall = Walls.WallTopLeftOut(self, pos)
        elif orientation == Walls.WallType.TOP_RIGHT:
            if inner:
                wall = Walls.WallTopRightIn(self, pos)
            else:
                wall = Walls.WallTopRightOut(self, pos)
        elif orientation == Walls.WallType.BOTTOM_LEFT:
            if inner:
                wall = Walls.WallBottomLeftIn(self, pos)
            else:
                wall = Walls.WallBottomLeftOut(self, pos)
        elif orientation == Walls.WallType.BOTTOM_RIGHT:
            if inner:
                wall = Walls.WallBottomRightIn(self, pos)
            else:
                wall = Walls.WallBottomRightOut(self, pos)
        elif orientation == Walls.WallType.TOP:
            wall = Walls.WallTop(self, pos)
        elif orientation == Walls.WallType.BOTTOM:
            wall = Walls.WallBottom(self, pos)
        elif orientation == Walls.WallType.LEFT:
            wall = Walls.WallLeft(self, pos)
        elif orientation == Walls.WallType.RIGHT:
            wall = Walls.WallRight(self, pos)
        self._tiles.append(wall)
        self._blocking.append(wall)
    
    def addGround(self, pos: sees.PosTuple):
        self._tiles.append(T.Ground(self, pos))
    
    def addHole(self, pos: sees.PosTuple):
        hole = T.Hole(self, pos)
        self._tiles.append(hole)
        self._holes.append(hole)
        self._blocking.append(hole)
    
    def addWallBlock(self, pos: sees.PosTuple):
        wall = Walls.WallBlock(self, pos)
        self._tiles.append(wall)
        self._blocking.append(wall)
    
    def addEntryDoor(self, pos: sees.PosTuple,  orientation: T.TileFacing):
        door = T.EntryDoor(self, pos, orientation)
        self._tiles.append(door)
        self._blocking.append(door)
    
    def addBarrierAndButton(self, posButton: sees.PosTuple, posBarrier: sees.PosTuple, barrierVertical: bool):
        barrier = E.LightBarrier(self, posBarrier, barrierVertical)
        self._tiles.append(barrier)
        self._blocking.append(barrier)
        self._blinking.append(barrier)
        button = E.OnePushButton(self, posButton, barrier)
        self._tiles.append(button)
        self._buttons.append(button)
    
    def addSecondaryCube(self, pos: sees.PosTuple):
        cube = E.EntitySecondaryCube(self, pos)
        self._tiles.append(cube),
        self._blocking.append(cube)
        self._moveable.append(cube)

    def addAirCannon(self, pos: sees.PosTuple):
        aircanon = E.AirCannon(self, pos)
        self._tiles.append(aircanon)
        self._blocking.append(aircanon)
        self._blinking.append(aircanon)
        self._aircannons.append(aircanon)  

    def addDecoration(self, pos: sees.PosTuple, decoType: DecoTypes):
        if decoType == DecoTypes.AFFICHE_ROUGE:
            self._tiles.append(T.AfficheRouge(self, pos))
        elif decoType == DecoTypes.DOUBLE_PAPIER:
            self._tiles.append(T.DoublePapier(self, pos))
        elif decoType == DecoTypes.FLAQUE:
            self._tiles.append(T.Flaque(self, pos))
        elif decoType == DecoTypes.SIMPLE_PAPIER:
            self._tiles.append(T.SimplePapier(self, pos))
        elif decoType == DecoTypes.ARMOIRE_FERMEE_HAUT:
            tile = T.ArmoirFermerHaut(self, pos)
            self._tiles.append(tile)
            self._blocking.append(tile)
        elif decoType == DecoTypes.ARMOIRE_FERMEE_BAS:
            self._tiles.append(T.ArmoirFermerBas(self, pos))
        elif decoType == DecoTypes.ARMOIRE_OUVERTE_HAUT:
            tile = T.ArmoirOuvertHaut(self, pos)
            self._tiles.append(tile)
            self._blocking.append(tile)
        elif decoType == DecoTypes.ARMOIRE_OUVERTE_BAS:
            self._tiles.append(T.ArmoirOuvertBas(self, pos))
        elif decoType == DecoTypes.ARMOIRE_DOS_HAUT:
            tile = T.ArmoirDosHaut(self, pos)
            self._tiles.append(tile)
            self._blocking.append(tile)
        elif decoType == DecoTypes.ARMOIRE_DOS_BAS:
            self._tiles.append(T.ArmoirDosBas(self, pos))
        elif decoType == DecoTypes.CARTONS:
            self._tiles.append(T.Cartons(self, pos))
        elif decoType == DecoTypes.AFFICHE_ROUGE_PENCHEE:
            self._tiles.append(T.AffichageRougePencher(self, pos))
        elif decoType == DecoTypes.CHAISE:
            tile = T.Chaise(self, pos)
            self._tiles.append(tile)
            self._blocking.append(tile)
        elif decoType == DecoTypes.BUREAU_DOS:
            tile = T.BureauDos(self, pos)
            self._tiles.append(tile)
            self._blocking.append(tile)
        elif decoType == DecoTypes.BUREAU_DROITE:
            tile = T.BureauDroite(self, pos)
            self._tiles.append(tile)
            self._blocking.append(tile)
            self._blinking.append(tile)
        elif decoType == DecoTypes.BUREAU_GAUCHE:
            tile = T.BureauGauche(self, pos)
            self._tiles.append(tile)
            self._blocking.append(tile)
            self._blinking.append(tile)
        elif decoType == DecoTypes.BUREAU_FACE:
            tile = T.BureauFace(self, pos)
            self._tiles.append(tile)
            self._blocking.append(tile)
            self._blinking.append(tile)
            