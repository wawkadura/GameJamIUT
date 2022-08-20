import pygame
from sees import Scene
from sees.TupleEnumTypes import SceneState, SizeTuple

class Window:
    def __init__(self, scene: Scene, title: str = "Game", width: int = 800, height: int = 600):
        self.__title = title
        self.__width = width
        self.__height = height
        self.__surface = None
        self.__running: bool = True
        self.__title = title
        self.__width = width
        self.__height = height
        self.__scene = scene
        pygame.init()
        self.__window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        pygame.display.set_caption(title)
        self.__surface = pygame.Surface(scene.getRes().value, pygame.HWSURFACE)
        scene.setWindow(self)
        scene.createDrawables()
        self.scaleWindow()
    
    def scaleWindow(self):
        wScale = self.__width / self.__scene.getRes().sizeX()
        hScale = self.__height / self.__scene.getRes().sizeY()
        self.__scaledW: int = 0
        self.__scaledH: int = 0
        if self.__scene.getRes().sizeX() * hScale > self.__width:
            self.__scaledW = int(self.__scene.getRes().sizeX() * wScale)
            self.__scaledH = int(self.__scene.getRes().sizeY() * wScale)
        else:
            self.__scaledW = int(self.__scene.getRes().sizeX() * hScale)
            self.__scaledH = int(self.__scene.getRes().sizeY() * hScale)
        self.__surfaceScaled = pygame.Surface((self.__scaledW, self.__scaledH), pygame.HWSURFACE)

    def getSurface(self):
        return self.__surface
    
    def getRunning(self):
        return self.__running
    
    def setRunning(self, running: bool):
        self.__running = running
    
    def getTitle(self):
        return self.__title
    
    def setTitle(self, title: str):
        if self.__window != None:
            pygame.display.set_caption(title)
        self.__title = title
    
    def getWidth(self):
        return self.__width
    
    def getHeight(self):
        return self.__height
    
    def setSize(self, size: SizeTuple):
        sizeT = SizeTuple._make(size)
        self.__width = sizeT.w
        self.__height = sizeT.h
        if self.__window != None:
            self.__window = pygame.display.set_mode(size, pygame.RESIZABLE)
            self.scaleWindow()
    
    def update(self):
        pygame.transform.scale(self.__surface, (self.__scaledW, self.__scaledH), self.__surfaceScaled)
        windowX = (self.__width / 2) - (self.__surfaceScaled.get_width() / 2)
        windowY = (self.__height / 2) - (self.__surfaceScaled.get_height() / 2)
        self.__window.blit(self.__surfaceScaled, (windowX, windowY))
        pygame.display.flip()

    def loop(self):
        self.__running = True
        while self.__running:
            if self.__scene != None:
                if self.__scene.mustResize():
                    self.setSize(self.__scene.newSize())
                    self.__scene.wasResized()
                if self.__scene.getState() == SceneState.QUIT:
                    self.__running = False
                elif self.__scene.getState() == SceneState.CHANGE_SCENE:
                    if self.__scene.getNextScene() != None:
                        self.__scene = self.__scene.getNextScene()
                        self.__scene.setWindow(self)
                        self.__scene.createDrawables()
                    else:
                        self.__scene = None
                else:
                    self.__scene.controls()
                    self.__surface.fill((0, 0, 0))
                    self.__scene.render()
                    self.update()