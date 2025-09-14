import random
import pygame
import math
def screen_tear_glitch(surface, intensity=10):
    """
    Creates realistic screen tearing effects
    """
    width, height = surface.get_size()
    
    for _ in range(intensity):
        # Random horizontal tear line
        tear_y = random.randint(0, height - 1)
        tear_offset = random.randint(-50, 50)
        
        # Copy a horizontal strip and shift it
        strip_height = random.randint(1, 10)
        try:
            strip = surface.subsurface(pygame.Rect(0, tear_y, width, strip_height)).copy()
            surface.blit(strip, (tear_offset, tear_y))
        except:
            pass

