import pygame
import sees
import sees.Scene as Sc
import Walls
import Entity as E
import Tile as T
import GameScene as GS
import SceneLevelBoss as SLB
from sees.TupleEnumTypes import SceneState

class SceneLevel1_2(GS.GameScene):
    def __init__(self):
        super().__init__((32, 160), (128, 80), (224, 128), (208, 0), T.TileFacing.NORTH)
        self.level = "1-2"
        self.addWall((0, 0) , Walls.WallType.TOP_LEFT, True)
        self.addWall((16,0), Walls.WallType.TOP, True)
        self.addWall((32,0), Walls.WallType.TOP, True)
        self.addWall((48,0), Walls.WallType.TOP, True)
        self.addWall((64,0), Walls.WallType.TOP, True)
        self.addWall((80,0), Walls.WallType.TOP, True)
        self.addWall((96,0), Walls.WallType.TOP, True)
        self.addWall((112,0), Walls.WallType.TOP, True)
        self.addWall((128,0), Walls.WallType.TOP, True)
        self.addWall((144,0), Walls.WallType.TOP, True)
        self.addWall((160,0), Walls.WallType.TOP, True)
        self.addWall((176,0), Walls.WallType.TOP, True)
        self.addWall((192,0), Walls.WallType.TOP, True)
        self.addWall((224,0), Walls.WallType.TOP, True)
        self.addWall((240,0) , Walls.WallType.TOP_RIGHT, True)
        self.addWall((240,16), Walls.WallType.RIGHT, True)
        self.addWall((240,32), Walls.WallType.RIGHT, True)
        self.addWall((240,48), Walls.WallType.RIGHT, True)
        self.addWall((240,64), Walls.WallType.RIGHT, True)
        self.addWall((240,80), Walls.WallType.RIGHT, True)
        self.addWall((240,96), Walls.WallType.RIGHT, True)
        self.addWall((240,112), Walls.WallType.RIGHT, True)
        self.addWall((240,128), Walls.WallType.RIGHT, True)
        self.addWall((240,144), Walls.WallType.RIGHT, True)
        self.addWall((240,160), Walls.WallType.RIGHT, True)
        self.addWall((240,176) , Walls.WallType.BOTTOM_RIGHT, True)
        self.addWall((16,176), Walls.WallType.BOTTOM, True)
        self.addWall((32,176), Walls.WallType.BOTTOM, True)
        self.addWall((48,176), Walls.WallType.BOTTOM, True)
        self.addWall((64,176), Walls.WallType.BOTTOM, True)
        self.addWall((80,176), Walls.WallType.BOTTOM, True)
        self.addWall((96,176), Walls.WallType.BOTTOM, True)
        self.addWall((112,176), Walls.WallType.BOTTOM, True)
        self.addWall((128,176), Walls.WallType.BOTTOM, True)
        self.addWall((144,176), Walls.WallType.BOTTOM, True)
        self.addWall((160,176), Walls.WallType.BOTTOM, True)
        self.addWall((176,176), Walls.WallType.BOTTOM, True)
        self.addWall((192,176), Walls.WallType.BOTTOM, True)
        self.addWall((208,176), Walls.WallType.BOTTOM, True)
        self.addWall((224,176), Walls.WallType.BOTTOM, True)
        self.addWall((0,176) , Walls.WallType.BOTTOM_LEFT, True)
        self.addWall((0,16), Walls.WallType.LEFT, True)
        self.addWall((0,32), Walls.WallType.LEFT, True)
        self.addWall((0,48), Walls.WallType.LEFT, True)
        self.addWall((0,64), Walls.WallType.LEFT, True)
        self.addWall((0,80), Walls.WallType.LEFT, True)
        self.addWall((0,96), Walls.WallType.LEFT, True)
        self.addWall((0,112), Walls.WallType.LEFT, True)
        self.addWall((0,128), Walls.WallType.LEFT, True)
        self.addWall((0,144), Walls.WallType.LEFT, True)
        self.addWall((0,160), Walls.WallType.LEFT, True)

        self.addGround((16,16))
        self.addGround((16,32))
        self.addGround((16,48))
        self.addWallBlock((16,64))
        self.addHole((16,80))
        self.addGround((16,96))
        self.addWallBlock((16,112))
        self.addGround((16,128))
        self.addGround((16,144))
        self.addGround((16,160))
        self.addGround((32,16))
        self.addGround((32,32))
        self.addGround((32,48))
        self.addWallBlock((32,64))
        self.addHole((32,80))
        self.addGround((32,96))
        self.addWallBlock((32,112))
        self.addGround((32,128))
        self.addGround((32,144))
        self.addGround((32,160))
        self.addGround((48,16))
        self.addGround((48,32))
        self.addGround((48,48))
        self.addWallBlock((48,64))
        self.addGround((48,80))
        self.addGround((48,96))
        self.addWallBlock((48,112))
        self.addGround((48,128))
        self.addGround((48,144))
        self.addGround((48,160))
        self.addGround((64,16))
        self.addGround((64,32))
        self.addGround((64,48))
        self.addGround((64,64))
        self.addGround((64,80))
        self.addGround((64,96))
        self.addWallBlock((64,112))
        self.addGround((64,128))
        self.addGround((64,144))
        self.addHole((64,160))
        self.addWallBlock((80,16))
        self.addHole((80,32))
        self.addHole((80,48))
        self.addGround((80,64))
        self.addGround((80,80))
        self.addGround((80,96))
        self.addWallBlock((80,112))
        self.addGround((80,128))
        self.addWallBlock((80,144))
        self.addWallBlock((80,160))
        self.addGround((96,16))
        self.addGround((96,32))
        self.addGround((96,48))
        self.addGround((96,64))
        self.addGround((96,80))
        self.addGround((96,96))
        self.addGround((96,112))
        self.addGround((96,128))
        self.addGround((96,144))
        self.addGround((96,160))
        self.addGround((112,16))
        self.addGround((112,32))
        self.addGround((112,48))
        self.addGround((112,64))
        self.addGround((112,80))
        self.addGround((112,96))
        self.addGround((112,112))
        self.addGround((112,128))
        self.addGround((112,144))
        self.addGround((112,160))
        self.addGround((128,16))
        self.addGround((128,32))
        self.addGround((128,48))
        self.addGround((128,64))
        self.addGround((128,80))
        self.addGround((128,96))
        self.addGround((128,112))
        self.addGround((128,128))
        self.addGround((128,144))
        self.addGround((128,160))
        self.addGround((144,16))
        self.addGround((144,32))
        self.addGround((144,48))
        self.addGround((144,64))
        self.addGround((144,80))
        self.addGround((144,96))
        self.addGround((144,112))
        self.addGround((144,128))
        self.addGround((144,144))
        self.addGround((144,160))
        self.addGround((160,16))
        self.addGround((160,32))
        self.addGround((160,48))
        self.addGround((160,64))
        self.addGround((160,80))
        self.addHole((160,96))
        self.addWallBlock((160,112))
        self.addHole((160,128))
        self.addWallBlock((160,144))
        self.addWallBlock((160,160))
        self.addWallBlock((176,16))
        self.addWallBlock((176,32))
        self.addWallBlock((176,48))
        self.addGround((176,64))
        self.addHole((176,80))
        self.addHole((176,96))
        self.addWallBlock((176,112))
        self.addGround((176,128))
        self.addGround((176,144))
        self.addGround((176,160))
        self.addGround((192,16))
        self.addGround((192,32))
        self.addWallBlock((192,48))
        self.addGround((192,64))
        self.addGround((192,80))
        self.addGround((192,96))
        self.addWallBlock((192,112))
        self.addGround((192,128))
        self.addGround((192,144))
        self.addGround((192,160))
        self.addGround((208,16))
        self.addGround((208,32))
        self.addGround((208,48))
        self.addGround((208,64))
        self.addGround((208,80))
        self.addGround((208,96))
        self.addWallBlock((208,112))
        self.addGround((208,128))
        self.addWallBlock((208,144))
        self.addHole((208,160))
        self.addHole((224,16))
        self.addHole((224,32))
        self.addWallBlock((224,48))
        self.addGround((224,64))
        self.addGround((224,80))
        self.addGround((224,96))
        self.addWallBlock((224,112))
        self.addGround((224,128))
        self.addHole((224,144))
        self.addGround((224,160))

        self.addDecoration((16,0), GS.DecoTypes.ARMOIRE_OUVERTE_HAUT)
        self.addDecoration((112,0), GS.DecoTypes.ARMOIRE_OUVERTE_HAUT)
        self.addDecoration((128,0), GS.DecoTypes.ARMOIRE_OUVERTE_HAUT)
        self.addDecoration((16,16), GS.DecoTypes.ARMOIRE_OUVERTE_BAS)
        self.addDecoration((112,16), GS.DecoTypes.ARMOIRE_OUVERTE_BAS)
        self.addDecoration((128,16), GS.DecoTypes.ARMOIRE_OUVERTE_BAS)
        self.addDecoration((32,0), GS.DecoTypes.ARMOIRE_FERMEE_HAUT)
        self.addDecoration((64,64), GS.DecoTypes.ARMOIRE_FERMEE_HAUT)
        self.addDecoration((80,64), GS.DecoTypes.ARMOIRE_FERMEE_HAUT)
        self.addDecoration((32,16), GS.DecoTypes.ARMOIRE_FERMEE_BAS)
        self.addDecoration((64,80), GS.DecoTypes.ARMOIRE_FERMEE_BAS)
        self.addDecoration((80,80), GS.DecoTypes.ARMOIRE_FERMEE_BAS)

        self.addDecoration((16,48), GS.DecoTypes.BUREAU_DOS)
        self.addDecoration((32,48), GS.DecoTypes.BUREAU_DOS)
        self.addDecoration((144,16), GS.DecoTypes.BUREAU_FACE)
        self.addDecoration((160,16), GS.DecoTypes.BUREAU_FACE)
        self.addDecoration((32,128), GS.DecoTypes.BUREAU_FACE)
        self.addDecoration((48,128), GS.DecoTypes.BUREAU_FACE)
        self.addDecoration((96,144), GS.DecoTypes.BUREAU_DROITE)
        self.addDecoration((96,160), GS.DecoTypes.BUREAU_DROITE)
        self.addDecoration((144,144), GS.DecoTypes.BUREAU_GAUCHE)
        self.addDecoration((144,160), GS.DecoTypes.BUREAU_GAUCHE)
        self.addDecoration((224,64), GS.DecoTypes.BUREAU_GAUCHE)
        self.addDecoration((224,80), GS.DecoTypes.BUREAU_GAUCHE)
        self.addDecoration((224,96), GS.DecoTypes.BUREAU_GAUCHE)

        self.addSecondaryCube((64,16))
        self.addSecondaryCube((192,160))
        self.addSecondaryCube((16,96))

        self.addDecoration((96,16), GS.DecoTypes.CARTONS)
        self.addDecoration((48,80), GS.DecoTypes.CARTONS)
        self.addDecoration((192,96), GS.DecoTypes.CARTONS)

        self.addDecoration((128,16), GS.DecoTypes.SIMPLE_PAPIER)
        self.addDecoration((48,48), GS.DecoTypes.SIMPLE_PAPIER)
        self.addDecoration((208,96), GS.DecoTypes.SIMPLE_PAPIER)

        self.addDecoration((112,144), GS.DecoTypes.CHAISE)
        self.addDecoration((160,32), GS.DecoTypes.CHAISE)

        self.addDecoration((48,0), GS.DecoTypes.DOUBLE_PAPIER)

        self.addDecoration((196,16), GS.DecoTypes.FLAQUE)

        self.addDecoration((160,0), GS.DecoTypes.AFFICHE_ROUGE)

        self.addDecoration((240,60), GS.DecoTypes.AFFICHE_ROUGE_PENCHEE)

        self.addBarrierAndButton((16,128), (80,128), True)
        self.addBarrierAndButton((16,32), (208,128), True)
        self.addBarrierAndButton((224,160), (208,48), False)
        self.addEntryDoor((32,176),T.TileFacing.SOUTH)
    
    def restartScene(self):
        Sound= pygame.mixer.Sound("SoundTrack/Traverser_une_porte.wav")
        Sound.play()
        self.musicOff()
        nextScene = SceneLevel1_2()
        nextScene.setInputs(self.getInputs())
        self._nextScene = nextScene
        self.setState(SceneState.CHANGE_SCENE)
    
    def mapLogic(self):
        if self._player.isColliding(self._door):
            Sound= pygame.mixer.Sound("SoundTrack/Porte_ouvert.wav")
            Sound.play()
            self.musicOff()
            nextScene = SLB.SceneLevelBoss()
            nextScene.setInputs(self.getInputs())
            self._nextScene = nextScene
            self.setState(SceneState.CHANGE_SCENE)