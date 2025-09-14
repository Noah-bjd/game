import pygame
import random
import math
def wave_distortion(surface, amplitude=5, frequency=0.05):
    """
    Creates a wave-like distortion across the screen
    """
    width, height = surface.get_size()
    temp_surface = surface.copy()
    
    for y in range(height):
        offset = int(math.sin(y * frequency) * amplitude)
        try:
            source_line = temp_surface.subsurface(pygame.Rect(0, y, width, 1))
            surface.blit(source_line, (offset, y))
        except:
            pass

