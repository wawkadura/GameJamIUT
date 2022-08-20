import pygame
from Walls import WallType
import Tile as T
import GameScene as GS
import SceneLevel1_2 as SL1_2
from sees.TupleEnumTypes import SceneState

class DemoScene(GS.GameScene):
    def __init__(self):
        super().__init__((64, 128), (160, 48), (128, 128), (144, 32), T.TileFacing.NORTH)
        self.level = "1-1"
        self.addWall((112, 32),WallType.TOP_LEFT, True)
        self.addWall((128, 32),WallType.TOP, True)
        self.addWall((160, 32),WallType.TOP, True)
        self.addWall((176, 32),WallType.TOP_RIGHT, True)
        self.addWall((112, 48),WallType.LEFT, True)
        self.addGround((128, 48))
        self.addGround((144, 48))
        self.addWall((176, 48), WallType.RIGHT, True)
        self.addWall((112, 64), WallType.LEFT, True)
        self.addGround((128, 64))
        self.addGround((144, 64))
        self.addGround((160, 64))
        self.addWall((176, 64), WallType.TOP_RIGHT, False)
        self.addWall((192, 64), WallType.TOP_RIGHT, True)
        self.addWall((112, 80), WallType.LEFT, True)
        self.addGround((128, 80))
        self.addWallBlock((144, 80))
        self.addGround((176, 80))
        self.addWall((192, 80), WallType.RIGHT, True)
        self.addWall((48, 96), WallType.TOP_LEFT, True)
        self.addWall((64, 96), WallType.TOP, True)
        self.addWall((80, 96), WallType.TOP, True)
        self.addWall((96, 96), WallType.TOP, True)
        self.addWall((112,96), WallType.TOP_LEFT, False)
        self.addGround((128, 96))
        self.addHole((160, 80))
        self.addGround((144, 96))
        self.addGround((160, 96))
        self.addWallBlock((176, 80))
        self.addGround((176, 96))
        self.addWall((192, 96), WallType.RIGHT, True)
        self.addWall((48, 112), WallType.LEFT, True)
        self.addGround((64, 112))
        self.addGround((80, 112))
        self.addGround((96, 112))
        self.addGround((112, 112))
        self.addGround((128, 112))
        self.addGround((144, 112))
        self.addGround((160, 112))
        self.addGround((176, 112))
        self.addWall((192, 112), WallType.RIGHT, True)
        self.addWall((48, 128), WallType.LEFT, True)
        self.addGround((64, 128))
        self.addGround((80, 128))
        self.addGround((96, 128))
        self.addGround((112, 128))
        self.addGround((128, 128))
        self.addGround((144, 128))
        self.addGround((160, 128))
        self.addGround((176, 128))
        self.addWall((192, 128), WallType.RIGHT, True)
        self.addWall((48, 144), WallType.LEFT, True)
        self.addGround((64, 144))
        self.addGround((80, 144))
        self.addGround((96, 144))
        self.addGround((112, 144))
        self.addGround((128, 144))
        self.addGround((144, 144))
        self.addGround((160, 144))
        self.addGround((176, 144))
        self.addWall((192, 144), WallType.RIGHT, True)
        self.addWall((48, 160), WallType.BOTTOM_LEFT, True)
        self.addWall((64, 160), WallType.BOTTOM, True)
        self.addWall((80, 160), WallType.BOTTOM, True)
        self.addWall((96, 160), WallType.BOTTOM, True)
        self.addWall((112, 160), WallType.BOTTOM, True)
        self.addWall((128, 160), WallType.BOTTOM, True)
        self.addWall((144, 160), WallType.BOTTOM, True)
        self.addWall((160, 160), WallType.BOTTOM, True)
        self.addWall((176, 160), WallType.BOTTOM, True)
        self.addWall((192, 160), WallType.BOTTOM_RIGHT, True)

        self.addBarrierAndButton((176, 144), (128, 80), False)

        self.addDecoration((160,80), GS.DecoTypes.ARMOIRE_OUVERTE_HAUT)
        self.addDecoration((160,96), GS.DecoTypes.ARMOIRE_OUVERTE_BAS)
        self.addDecoration((176,80), GS.DecoTypes.ARMOIRE_FERMEE_HAUT)
        self.addDecoration((176,96), GS.DecoTypes.ARMOIRE_FERMEE_BAS)

        self.addDecoration((144, 96), GS.DecoTypes.BUREAU_FACE)
        self.addDecoration((176, 112), GS.DecoTypes.BUREAU_GAUCHE)
        self.addDecoration((176, 128), GS.DecoTypes.BUREAU_GAUCHE)
        self.addDecoration((192, 128), GS.DecoTypes.AFFICHE_ROUGE_PENCHEE)
        self.addDecoration((96, 96), GS.DecoTypes.AFFICHE_ROUGE)
        self.addDecoration((80, 96), GS.DecoTypes.ARMOIRE_OUVERTE_HAUT)
        self.addDecoration((64, 96), GS.DecoTypes.ARMOIRE_FERMEE_HAUT)
        self.addDecoration((80, 112), GS.DecoTypes.ARMOIRE_OUVERTE_BAS)
        self.addDecoration((64, 112), GS.DecoTypes.ARMOIRE_FERMEE_BAS)
        self.addDecoration((128, 32), GS.DecoTypes.ARMOIRE_FERMEE_HAUT)
        self.addDecoration((128, 48), GS.DecoTypes.ARMOIRE_FERMEE_BAS)
        self.addEntryDoor((48,128),T.TileFacing.WEST)
    
    def restartScene(self):
        Sound= pygame.mixer.Sound("SoundTrack/Traverser_une_porte.wav")
        Sound.play()
        self.musicOff()
        nextScene = DemoScene()
        nextScene.setInputs(self.getInputs())
        self._nextScene = nextScene
        self.setState(SceneState.CHANGE_SCENE)

    def mapLogic(self):
        if self._player.isColliding(self._door):
            Sound= pygame.mixer.Sound("SoundTrack/Porte_ouvert.wav")
            Sound.play()
            self.musicOff()
            nextScene = SL1_2.SceneLevel1_2()
            nextScene.setInputs(self.getInputs())
            self._nextScene = nextScene
            self.setState(SceneState.CHANGE_SCENE)