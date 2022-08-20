from typing import NamedTuple
from enum import Enum

class InputButtonTuple(NamedTuple):
    btn: int
    ctrler: int

class InputAxisTuple(NamedTuple):
    axis: int
    ctrler: int

class SizeTuple(NamedTuple):
    w: int
    h: int

class PosTuple(NamedTuple):
    x: int
    y: int

class PosLayerTuple(NamedTuple):
    l: int
    x: int
    y: int

class SceneState(Enum):
    RUN = 0
    QUIT = 1
    CHANGE_SCENE = 2

class Resolution(Enum):
    RES_256x224 = (256, 224)
    RES_256x239 = (256, 239)
    RES_512x224 = (512, 224)
    RES_512x239 = (512, 239)
    RES_512x448 = (512, 448)
    RES_512x478 = (512, 478)

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def sizeX(self):
        return self.__x
    
    def sizeY(self):
        return self.__y

class SpriteSize(Enum):
    SPR_8x8 = 8
    SPR_16x16 = 16
    SPR_32x32 = 32
    SPR_64x64 = 64