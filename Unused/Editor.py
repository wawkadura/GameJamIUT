import pygame
import sees
import EditorScene as ES
import sees.Scene as Sc

def MoveLeft(scene: Sc.Scene):
    sel = scene.getSelector()
    pos = sel.getPos()
    if (pos.x > 0):
        sel.setPos((pos.x - 16, pos.y))

def MoveRight(scene: Sc.Scene):
    sel = scene.getSelector()
    pos = sel.getPos()
    if (pos.x < 240):
        sel.setPos((pos.x + 16, pos.y))

def MoveUp(scene: Sc.Scene):
    sel = scene.getSelector()
    pos = sel.getPos()
    if (pos.y > 0):
        sel.setPos((pos.x, pos.y - 16))

def MoveDown(scene: Sc.Scene):
    sel = scene.getSelector()
    pos = sel.getPos()
    if (pos.y < 208):
        sel.setPos((pos.x, pos.y + 16))

def CycleTileLeft(scne: Sc.Scene):
    pos = scene.getSelector().getPos()

def ToggleTile(scene: Sc.Scene):
    return


scene = ES.Editor()
win = sees.Window(scene)

inputs = sees.Input.InputBindings()
moveLeftInput = sees.Input.InputKey("Se déplacer à gauche", MoveLeft, pygame.K_a)
inputs.setInput("moveLeft", moveLeftInput)
moveRightInput = sees.Input.InputKey("Se déplacer à droite", MoveRight, pygame.K_d)
inputs.setInput("moveRight", moveRightInput)
moveUpInput = sees.Input.InputKey("Se déplacer en haut", MoveUp, pygame.K_w)
inputs.setInput("moveUp", moveUpInput)
moveDownInput = sees.Input.InputKey("Se déplacer en bas", MoveDown, pygame.K_s)
inputs.setInput("moveDown", moveDownInput)
scene.setInputs(inputs)
win.loop()

pygame.quit()