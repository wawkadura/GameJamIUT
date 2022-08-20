import pygame
import types
from sees import Scene
from sees.TupleEnumTypes import InputAxisTuple, InputButtonTuple
from collections import defaultdict
from abc import ABC

class InputBase(ABC):
    def __init__(self, desc: str, action: types.FunctionType):
        self.__desc = desc
        self.__action = action
        self.__value: float = 0

    def setValue(self, value: float):
        self.__value = value
    
    def getValue(self):
        return self.__value
    
    def setDesc(self, desc: str):
        self.__desc = desc
    
    def getDesc(self):
        return self.__desc
    
    def setAction(self, action: types.FunctionType):
        self.__action = action
    
    def exec(self, scene : Scene):
        if self.__value != 0 and not scene is None:
            self.__action(scene)

class InputKey(InputBase):
    def __init__(self: str, desc: str, action: types.FunctionType, key: pygame.key):
        super().__init__(desc, action)
        self.__key = key
    
    def getKey(self):
        return self.__key
    
    def setKey(self, key: pygame.key):
        self.__key = key

class InputButton(InputBase):
    def __init__(self, desc: str, action: types.FunctionType, btn: InputButtonTuple):
        super().__init__(desc, action)
        self.__btn = InputButtonTuple._make(btn)
    
    def getBtn(self):
        return self.__btn
    
    def setBtn(self, btn: InputButtonTuple):
        self.__btn = InputButtonTuple._make(btn)

class InputAxis(InputBase):
    def __init__(self, desc: str, action: types.FunctionType, axis: InputAxisTuple):
        super().__init__(desc, action)
        self.__axis = InputAxisTuple._make(axis)
    
    def getAxis(self):
        return self.__axis
    
    def setAxis(self, axis: InputAxisTuple):
        self.__axis = InputAxisTuple._make(axis)

class InputBindings:
    def __init__(self):
        self.__inputKeys = defaultdict(str)
        self.__inputButtons = defaultdict(str)
        self.__inputAxes = defaultdict(str)
    
    def setInput(self, name: str, ctrl: InputBase):
        if (isinstance(ctrl, InputKey)):
            self.__inputKeys[name] = ctrl
        elif (isinstance(ctrl, InputButton)):
            self.__inputButtons[name] = ctrl
        elif (isinstance(ctrl, InputAxis)):
            self.__inputAxes[name] = ctrl
    
    def removeInputKey(self, name: str):
        self.__inputKeys.pop(name, None)
    
    def removeInputButton(self, name: str):
        self.__inputButtons.pop(name, None)
    
    def removeInputAxis(self, name: str):
        self.__inputAxes.pop(name, None)

    def getInputKeys(self):
        return self.__inputKeys
    
    def getInputButtons(self):
        return self.__inputButtons
    
    def getInputAxes(self):
        return self.__inputAxes