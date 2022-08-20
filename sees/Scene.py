import pygame
from enum import Enum
import sees
from sees.TupleEnumTypes import SceneState, PosLayerTuple, Resolution
from sees import Drawables
from sees.Input import InputBindings
from typing import NamedTuple
from collections import defaultdict

class Scene:
    def __init__(self, res: Resolution, framerate: int):
        self.__posX: int = 0
        self.__posY: int = 0
        self.__res = res
        if framerate < 1 :
            framerate = 1
        self.__framerate = framerate
        self.__inputs: InputBindings = None
        self.__prevTime: int = 0
        self.__bg1: Drawables.Background = None
        self.__bg2: Drawables.Background = None
        self.__drawables = defaultdict(int)
        self.__state: SceneState = SceneState.RUN
        self._nextScene: Scene = None
        self.__resize: bool = False
        self.__newsize = None
        self._window = None
        self.__registerInput = True
    
    def setWindow(self, window):
        self._window = window
    
    def getWindow(self):
        return self._window
    
    def registerInput(self):
        self.__registerInput = True
    
    def stopRegisterInput(self):
        self.__registerInput = False
    
    def getRegisterInput(self):
        return self.__registerInput
    
    def logic(self):
        return
    
    def redraw(self):
        self._window.getSurface().fill((0, 0, 0))
        if (self._window != None):
            if self.__bg1 != None:
                self.__bg1.draw(self._window.getSurface())
            if self.__bg2 != None:
                self.__bg2.draw(self._window.getSurface())
            for l in range(0, 4):
                for drawable in self.__drawables.values():
                    if drawable.getPos().l == l:
                        drawable.draw(self._window.getSurface())
        self._window.update()
    
    def render(self):
        if (self._window != None):
            currTime: int = pygame.time.get_ticks()
            timeElapsed: int = currTime - self.__prevTime
            if timeElapsed < (1000 / self.__framerate):
                pygame.time.wait(int((1000 / self.__framerate) - timeElapsed))
                currTime = pygame.time.get_ticks()
                timeElapsed = currTime - self.__prevTime
            self.__prevTime = currTime
            if (self._window != None):
                if self.__bg1 != None:
                    self.__bg1.draw(self._window.getSurface())
                if self.__bg2 != None:
                    self.__bg2.draw(self._window.getSurface())
                for l in range(0, 4):
                    for drawable in self.__drawables.values():
                        if drawable.getPos().l == l:
                            drawable.draw(self._window.getSurface())
            self.logic()
    
    def controls(self):
        eventlist = pygame.event.get()
        for event in eventlist:
            if event.type == pygame.QUIT:
                self.__state = SceneState.QUIT
            elif event.type == pygame.VIDEORESIZE:
                self.__resize = True
                self.__newsize = (event.w, event.h)
            elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if self.__inputs != None:
                    for inp in self.__inputs.getInputKeys().values():
                        if inp.getKey() == event.key:
                            if event.type == pygame.KEYDOWN:
                                inp.setValue(1)
                            else:
                                inp.setValue(0)
            elif event.type == pygame.JOYBUTTONDOWN or event.type == pygame.JOYBUTTONUP:
                if self.__inputs != None:
                    for inp in self.__inputs.getInputButtons().values():
                        if inp.getBtn().btn == event.button and inp.getBtn().ctrler == event.joy:
                            inp.setValue(1 if event.type == pygame.JOYBUTTONDOWN else 0)
            elif event.type == pygame.JOYAXISMOTION:
                if self.__inputs != None:
                    for inp in self.__inputs.getInputAxes().values():
                        if inp.getAxis().axis == event.axis and inp.getAxis().ctrler == event.joy:
                            inp.setValue(event.value)
            if self.__inputs != None:
                for inp in self.__inputs.getInputKeys().values():
                    inp.exec(self)
                for inp in self.__inputs.getInputButtons().values():
                    inp.exec(self)
                for inp in self.__inputs.getInputAxes().values():
                    inp.exec(self)
    
    def createDrawables(self):
        return
    
    def addDrawable(self, obj: Drawables.Drawable):
        index = max(self.__drawables.keys()) + 1 if len(self.__drawables) > 0 else 1
        self.__drawables[index] = obj
        obj.setScene(self)
        return index
    
    def setDrawable(self, index: int, obj: Drawables.Drawable):
        if index in self.__drawables:
            self.__drawables[index] = obj
    
    def getDrawable(self, index: int):
        return self.__drawables[index]
    
    def getDrawables(self):
        return self.__drawables
    
    def removeDrawable(self, index: int):
        self.__drawables.pop(index, None)
    
    def getPosX(self):
        return self.__posX
    
    def setPosX(self, pos: int):
        self.__posX = pos
    
    def getPosY(self):
        return self.__posY
    
    def setPosY(self, pos: int):
        self.__posY = pos
    
    def getRes(self):
        return self.__res
    
    def getFramerate(self):
        return self.__framerate
    
    def setFramerate(self, framerate: int):
        if framerate < 1 :
            framerate = 1
        self.__framerate = framerate
    
    def getInputs(self):
        return self.__inputs
    
    def setInputs(self, inputs: InputBindings):
        self.__inputs = inputs
        if self.__inputs != None:
            for inp in self.__inputs.getInputKeys().values():
                inp.setValue(0)
    
    def getBg1(self):
        return self.__bg1
    
    def setBg1(self, bg: Drawables.Background):
        self.__bg1 = bg
        bg.setScene(self)
    
    def getBg2(self):
        return self.__bg2
    
    def setBg2(self, bg: Drawables.Background):
        self.__bg2 = bg
        bg.setScene(self)
    
    def getState(self):
        return self.__state
    
    def setState(self, state: SceneState):
        self.__state = state
    
    def getNextScene(self):
        return self._nextScene
    
    def mustResize(self):
        return self.__resize
    
    def newSize(self):
        return self.__newsize
    
    def wasResized(self):
        self.__resize = False
        self.__newsize = None