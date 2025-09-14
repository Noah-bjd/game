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

def screen_shatter_effect(surface, intensity=5):
    """
    Simulates screen shattering like broken glass
    """
    width, height = surface.get_size()
    
    for _ in range(intensity):
        # Create fracture lines
        start_x = random.randint(0, width)
        start_y = random.randint(0, height)
        
        # Draw fracture lines in random directions
        for i in range(random.randint(3, 8)):
            angle = random.uniform(0, 2 * math.pi)
            length = random.randint(20, 200)
            end_x = start_x + int(math.cos(angle) * length)
            end_y = start_y + int(math.sin(angle) * length)
            
            # Clamp to screen bounds
            end_x = max(0, min(width - 1, end_x))
            end_y = max(0, min(height - 1, end_y))
            
            # Draw the fracture line
            color = (random.randint(200, 255), random.randint(200, 255), random.randint(200, 255))
            pygame.draw.line(surface, color, (start_x, start_y), (end_x, end_y), 1)
            
            # Offset fragments on either side of the fracture
            if random.random() < 0.3:
                offset_x = random.randint(-5, 5)
                offset_y = random.randint(-5, 5)
                fragment_size = random.randint(10, 50)
                
                frag_x = max(0, min(width - fragment_size, start_x + offset_x))
                frag_y = max(0, min(height - fragment_size, start_y + offset_y))
                
                try:
                    fragment = surface.subsurface(pygame.Rect(frag_x, frag_y, fragment_size, fragment_size)).copy()
                    surface.blit(fragment, (frag_x + offset_x * 2, frag_y + offset_y * 2))
                except:
                    pass