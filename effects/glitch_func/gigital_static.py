import pygame
import random
def digital_static(surface, intensity=100):
    """
    Creates TV static-like noise across the screen
    """
    width, height = surface.get_size()
    
    for _ in range(intensity):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        size = random.randint(1, 3)
        
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pygame.draw.rect(surface, color, (x, y, size, size))

def scanline_glitch(surface, intensity=5):
    """
    Creates broken scanline effects
    """
    width, height = surface.get_size()
    
    for _ in range(intensity):
        y = random.randint(0, height - 1)
        scanline_height = random.randint(1, 3)
        
        # Darken or lighten the scanline
        if random.random() < 0.5:
            # Dark scanline
            scanline = pygame.Surface((width, scanline_height))
            scanline.set_alpha(150)
            scanline.fill((0, 0, 0))
            surface.blit(scanline, (0, y))
        else:
            # Bright scanline
            scanline = pygame.Surface((width, scanline_height))
            scanline.set_alpha(100)
            scanline.fill((255, 255, 255))
            surface.blit(scanline, (0, y))
            
        # Occasionally offset the scanline
        if random.random() < 0.3:
            offset = random.randint(-20, 20)
            try:
                line_content = surface.subsurface(pygame.Rect(0, y, width, scanline_height)).copy()
                surface.blit(line_content, (offset, y))
            except:
                pass