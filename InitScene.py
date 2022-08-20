import pygame
import Walls
from Walls import WallType
import Tile as T
import GameScene as GS
import DemoScene as DS
import SceneLevel1_2 as SL1_2
from sees.TupleEnumTypes import SceneState

class InitScene(GS.GameScene):
    def __init__(self):
        super().__init__((96, 96), (160, 80), (128, 80), (128, 128), T.TileFacing.SOUTH)
        self.level = "0-1"
        self.addWall((64, 48),Walls.WallType.TOP_LEFT, True)
        self.addWall((80, 48),Walls.WallType.TOP, True)
        self.addWall((96, 48),Walls.WallType.TOP, True)
        self.addWall((112, 48),Walls.WallType.TOP, True)
        self.addWall((128, 48),Walls.WallType.TOP, True)
        self.addWall((144, 48),Walls.WallType.TOP, True)
        self.addWall((160, 48),Walls.WallType.TOP, True)
        self.addWall((176, 48),Walls.WallType.TOP_RIGHT, True)
        self.addWall((176,64), Walls.WallType.RIGHT, True)
        self.addWall((176,80), Walls.WallType.RIGHT, True)
        self.addWall((176,96), Walls.WallType.RIGHT, True)
        self.addWall((176,112),Walls.WallType.RIGHT, True)
        self.addWall((176,128), Walls.WallType.BOTTOM_RIGHT, True)
        self.addWall((160,128), Walls.WallType.BOTTOM, True)
        self.addWall((144,128), Walls.WallType.BOTTOM, True)
        self.addWall((112,128), Walls.WallType.BOTTOM, True)
        self.addWall((96,128), Walls.WallType.BOTTOM, True)
        self.addWall((80,128), Walls.WallType.BOTTOM, True)
        self.addWall((64,128) , Walls.WallType.BOTTOM_LEFT, True)
        self.addWall((64,64), Walls.WallType.LEFT, True)
        self.addWall((64,80), Walls.WallType.LEFT, True)
        self.addWall((64,96), Walls.WallType.LEFT, True)
        self.addWall((64,112), Walls.WallType.LEFT, True)

        self.addGround((80,64))
        self.addGround((80,80))
        self.addGround((80,96))
        self.addGround((80,112))
        self.addGround((96,64))
        self.addGround((96,80))
        self.addGround((96,96))
        self.addGround((96,112))
        self.addGround((112,64))
        self.addGround((112,80))
        self.addGround((112,96))
        self.addGround((112,112))
        self.addGround((128,64))
        self.addGround((128,80))
        self.addGround((128,96))
        self.addGround((128,112))
        self.addGround((144,64))
        self.addGround((144,80))
        self.addGround((144,96))
        self.addGround((144,112))
        self.addGround((160,64))
        self.addGround((160,80))
        self.addGround((160,96))
        self.addGround((160,112))

        self.addDecoration((80, 80), GS.DecoTypes.BUREAU_DROITE)
        self.addDecoration((176, 112), GS.DecoTypes.AFFICHE_ROUGE_PENCHEE)
        self.addDecoration((96, 48), GS.DecoTypes.AFFICHE_ROUGE)
        self.addDecoration((144, 48), GS.DecoTypes.ARMOIRE_OUVERTE_HAUT)
        self.addDecoration((144, 64), GS.DecoTypes.ARMOIRE_OUVERTE_BAS)
        self.addDecoration((112, 48), GS.DecoTypes.ARMOIRE_FERMEE_HAUT)
        self.addDecoration((112, 64), GS.DecoTypes.ARMOIRE_FERMEE_BAS)
    
    def restartScene(self):
        Sound= pygame.mixer.Sound("SoundTrack/Traverser_une_porte.wav")
        Sound.play()
        self.musicOff()
        nextScene = InitScene()
        nextScene.setInputs(self.getInputs())
        self._nextScene = nextScene
        self.setState(SceneState.CHANGE_SCENE)

    def mapLogic(self):
        if self._player.isColliding(self._door):
            Sound= pygame.mixer.Sound("SoundTrack/Porte_ouvert.wav")
            Sound.play()
            self.musicOff()
            nextScene = DS.DemoScene()
            nextScene.setInputs(self.getInputs())
            self._nextScene = nextScene
            self.setState(SceneState.CHANGE_SCENE)