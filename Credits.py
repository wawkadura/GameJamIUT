import pygame
import sees
import sees.Scene as Sc
import Menu as M
from sees.TupleEnumTypes import SceneState

class Credits(Sc.Scene):
    def __init__(self):
        super().__init__(sees.Resolution.RES_256x224, 60)
        inputs = sees.Input.InputBindings()
        quitFunc = lambda scene: scene.returnToMenu()
        quitInput = sees.Input.InputKey("Retour au menu principal", quitFunc, pygame.K_ESCAPE)
        inputs.setInput("quit", quitInput)
        self.setInputs(inputs)
        
    def createDrawables(self):
        tex = pygame.image.load(".//Sprites//Credit.png").convert_alpha()
        bg = sees.Background(tex, sees.Resolution.RES_256x224, (0, 0))
        self.setBg1(bg)

    def logic(self):
        return
    
    def returnToMenu(self):
        self._nextScene = M.Menu()
        self.setState(SceneState.CHANGE_SCENE)