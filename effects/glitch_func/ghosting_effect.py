import pygame
import random

def ghosting_effect(surface, intensity=5, decay=0.8):
    """
    Creates a ghosting/trailing effect like persistence of vision
    """
    width, height = surface.get_size()
    
    # Create a slightly transparent copy of the current frame
    ghost = surface.copy()
    ghost.set_alpha(int(255 * decay))
    
    # Apply the ghost with a slight offset
    offset_x = random.randint(-intensity, intensity)
    offset_y = random.randint(-intensity, intensity)
    
    surface.blit(ghost, (offset_x, offset_y))

def jump_scare_glitch(surface, scare_image=None, probability=0.1):
    """
    Occasionally flashes a scary image very briefly
    """
    if random.random() < probability and scare_image:
        width, height = surface.get_size()
        
        # Scale the scare image if needed
        if scare_image.get_size() != (width, height):
            scare_image = pygame.transform.scale(scare_image, (width, height))
        
        # Flash the image very briefly
        surface.blit(scare_image, (0, 0))
        
        # Return True to indicate a jump scare occurred
        return True
    
    return False
