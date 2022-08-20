import pygame
import sees
import Menu as M

scene = M.Menu()
win = sees.Window(scene, "A-L1Z3")
icon = pygame.image.load('.//Sprites//Icon.png').convert_alpha()
pygame.display.set_icon(icon)
win.loop()

pygame.quit()