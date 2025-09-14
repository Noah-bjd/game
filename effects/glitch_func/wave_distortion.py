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

def vortex_distortion(surface, strength=0.01):
    """
    Creates a vortex-like distortion effect
    """
    width, height = surface.get_size()
    center_x, center_y = width // 2, height // 2
    temp_surface = surface.copy()
    
    for y in range(height):
        for x in range(width):
            # Calculate distance from center
            dx = x - center_x
            dy = y - center_y
            distance = math.sqrt(dx*dx + dy*dy)
            
            # Calculate angle and apply distortion
            angle = math.atan2(dy, dx)
            new_distance = distance * (1 + strength * math.sin(distance * 0.1))
            
            # Calculate new position
            new_x = int(center_x + math.cos(angle) * new_distance)
            new_y = int(center_y + math.sin(angle) * new_distance)
            
            # Clamp to screen bounds
            new_x = max(0, min(width - 1, new_x))
            new_y = max(0, min(height - 1, new_y))
            
            # Copy pixel from original position to new position
            if random.random() < 0.95:  # Add some randomness
                try:
                    pixel = temp_surface.get_at((new_x, new_y))
                    surface.set_at((x, y), pixel)
                except:
                    pass