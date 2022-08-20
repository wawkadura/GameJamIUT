import pygame
import InitScene as IS
import sees
import SceneLevelBoss2
import sees.Scene as Sc
from sees.TupleEnumTypes import SceneState
import Credits as Cr
import Tile

class Menu(Sc.Scene):
    def __init__(self):
        super().__init__(sees.Resolution.RES_256x224, 60)
        self._buttons = []
        self._selected = 0
        inputs = sees.Input.InputBindings()
        quitFunc = lambda scene: scene.quitGame()
        quitInput = sees.Input.InputKey("Quitter le jeu", quitFunc, pygame.K_ESCAPE)
        inputs.setInput("quit", quitInput)
        selectUpFunc = lambda scene: scene.selectUp()
        selectUpInput = sees.Input.InputKey("Sélectionner le bouton supérieur", selectUpFunc, pygame.K_w)
        selectUpInput2 = sees.Input.InputKey("Sélectionner le bouton supérieur", selectUpFunc, pygame.K_UP)
        inputs.setInput("selectUp", selectUpInput)
        inputs.setInput("selectUp2", selectUpInput2)
        selectDownFunc = lambda scene: scene.selectDown()
        selectDownInput = sees.Input.InputKey("Sélectionner le bouton inférieur", selectDownFunc, pygame.K_s)
        selectDownInput2 = sees.Input.InputKey("Sélectionner le bouton inférieur", selectDownFunc, pygame.K_DOWN)
        inputs.setInput("selectDown", selectDownInput)
        inputs.setInput("selectDown2", selectDownInput2)
        selectFunc = lambda scene: scene.action()
        selectInput = sees.Input.InputKey("Appuyer sur le bouton", selectFunc, pygame.K_RETURN)
        inputs.setInput("select", selectInput)
        self.setInputs(inputs)
        self._buttons.append(MenuButton(self, (96, 112), (0, 0)))
        self._buttons.append(MenuButton(self, (96, 144), (0, 32)))
        
    def createDrawables(self):
        tex = pygame.image.load(".//Sprites//Menu.png").convert_alpha()
        bg = sees.Background(tex, sees.Resolution.RES_256x224, (0, 0))
        self.setBg1(bg)
        self._backgroundSound= pygame.mixer.Sound("SoundTrack/Opening.wav")
        self._backgroundSound.play(loops=-1, maxtime=0, fade_ms=0)
        for btn in self._buttons:
            btn.createDrawable()
        self._buttons[0].select()

    def logic(self):
        return
    
    def action(self):
        
        Sound= pygame.mixer.Sound("SoundTrack/Vent_2.wav")
        Sound.play()
        if self._selected == 0:
            self._backgroundSound.stop()
            nextScene = IS.InitScene()
            inputs = sees.Input.InputBindings()
            moveLeftInput = sees.Input.InputKey("Se déplacer à gauche", MoveLeft, pygame.K_a)
            moveLeftInput2 = sees.Input.InputKey("Se déplacer à gauche", MoveLeft, pygame.K_LEFT)
            inputs.setInput("moveLeft", moveLeftInput)
            inputs.setInput("moveLeft2", moveLeftInput2)
            moveRightInput = sees.Input.InputKey("Se déplacer à droite", MoveRight, pygame.K_d)
            moveRightInput2 = sees.Input.InputKey("Se déplacer à droite", MoveRight, pygame.K_RIGHT)
            inputs.setInput("moveRight", moveRightInput)
            inputs.setInput("moveRight2", moveRightInput2)
            moveUpInput = sees.Input.InputKey("Se déplacer en haut", MoveUp, pygame.K_w)
            moveUpInput2 = sees.Input.InputKey("Se déplacer en haut", MoveUp, pygame.K_UP)
            inputs.setInput("moveUp", moveUpInput)
            inputs.setInput("moveUp2", moveUpInput2)
            moveDownInput = sees.Input.InputKey("Se déplacer en bas", MoveDown, pygame.K_s)
            moveDownInput2 = sees.Input.InputKey("Se déplacer en bas", MoveDown, pygame.K_DOWN)
            inputs.setInput("moveDown", moveDownInput)
            inputs.setInput("moveDown2", moveDownInput2)
            pushPower = sees.Input.InputKey("Pouvoir de repousement", PushPower, pygame.K_SPACE)
            inputs.setInput("pushPower", pushPower)
            pullPower = sees.Input.InputKey("Pouvoir d'attraction", PullPower, pygame.K_LSHIFT)
            pullPower2 = sees.Input.InputKey("Pouvoir d'attraction", PullPower, pygame.K_u)
            inputs.setInput("pullPower", pullPower)
            inputs.setInput("pullPower2", pullPower2)
            restartSceneFunc = lambda scene: scene.restartScene()
            restartSceneInput = sees.Input.InputKey("Redémarrer le niveau", restartSceneFunc, pygame.K_BACKSPACE)
            inputs.setInput("restartScene", restartSceneInput)
            quitFunc = lambda scene: scene.ReturnToMenu()
            quitInput = sees.Input.InputKey("Retour au menu principal", quitFunc, pygame.K_ESCAPE)
            inputs.setInput("quit", quitInput)
            nextScene.setInputs(inputs)
            self._nextScene = nextScene
            self.setState(SceneState.CHANGE_SCENE)
        elif self._selected == 1:
            self._backgroundSound.stop()
            self._nextScene = Cr.Credits()
            self.setState(SceneState.CHANGE_SCENE)
    
    def quitGame(self):
        self.setState(SceneState.QUIT)
    
    def selectUp(self):
        Sound= pygame.mixer.Sound("SoundTrack/Menu_de_Selection.wav")
        Sound.play()
        if self._selected > 0:
            self._buttons[self._selected].unselect()
            self._selected -= 1
            self._buttons[self._selected].select()
    
    def selectDown(self):
        Sound= pygame.mixer.Sound("SoundTrack/Menu_de_Selection.wav")
        Sound.play()
        if self._selected < (len(self._buttons) - 1):
            self._buttons[self._selected].unselect()
            self._selected += 1
            self._buttons[self._selected].select()

class MenuButton:
    def __init__(self, scene: Sc, pos: sees.PosTuple, texPos: sees.PosTuple):
        self._scene = scene
        self._drawable = None
        pos = sees.PosTuple._make(pos)
        self.__pos = pos
        self.__texPos = texPos

    def createDrawable(self):
        tex = pygame.image.load(".//Sprites//HUD.png").convert_alpha()
        drawable = sees.AnimatedDrawable(tex, (64, 32), self.__texPos, (2, self.__pos.x, self.__pos.y))
        drawable.addTexPosition((self.__texPos[0] + 64, self.__texPos[1]))
        self._drawable = self._scene.addDrawable(drawable)

    def select(self):
        self._scene.getDrawable(self._drawable).setState(1)
    
    def unselect(self):
        self._scene.getDrawable(self._drawable).setState(0)
    
    def getDrawable(self):
        return self._drawable

def MoveLeft(scene: Sc.Scene):
    Sound= pygame.mixer.Sound("SoundTrack/Pied_3.wav")
    Sound.play()
    scene.getPlayer().move(Tile.TileFacing.WEST)

def MoveRight(scene: Sc.Scene):
    Sound= pygame.mixer.Sound("SoundTrack/Pied_3.wav")
    Sound.play()
    scene.getPlayer().move(Tile.TileFacing.EAST)

def MoveUp(scene: Sc.Scene):
    Sound= pygame.mixer.Sound("SoundTrack/Pied_3.wav")
    Sound.play()
    scene.getPlayer().move(Tile.TileFacing.NORTH)

def MoveDown(scene: Sc.Scene):
    Sound= pygame.mixer.Sound("SoundTrack/Pied_3.wav")
    Sound.play()
    scene.getPlayer().move(Tile.TileFacing.SOUTH)

def PushPower(scene: Sc.Scene):
    Sound= pygame.mixer.Sound("SoundTrack/Vent_pull_push.wav")
    Sound.play()
    Sound= pygame.mixer.Sound("SoundTrack/Girl_2.wav")
    Sound.play()
    scene.getPlayer().powerRepulse()

def PullPower(scene: Sc.Scene):
    Sound= pygame.mixer.Sound("SoundTrack/Vent_Pull_1.ogg")
    Sound.play()
    Sound= pygame.mixer.Sound("SoundTrack/Girl_5.wav")
    Sound.play()
    scene.getPlayer().powerAttract()