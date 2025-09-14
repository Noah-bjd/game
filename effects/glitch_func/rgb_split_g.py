import pygame
import random
def rgb_split_glitch(surface, intensity=10):
    """
    Separates RGB channels for a psychedelic, unsettling effect
    """
    width, height = surface.get_size()
    
    # Create separate surfaces for each channel
    r_channel = surface.copy()
    g_channel = surface.copy()
    b_channel = surface.copy()
    
    # Apply color filters to isolate channels
    r_filter = pygame.Surface((width, height), pygame.SRCALPHA)
    r_filter.fill((255, 0, 0, 100))
    r_channel.blit(r_filter, (0, 0))
    
    g_filter = pygame.Surface((width, height), pygame.SRCALPHA)
    g_filter.fill((0, 255, 0, 100))
    g_channel.blit(g_filter, (0, 0))
    
    b_filter = pygame.Surface((width, height), pygame.SRCALPHA)
    b_filter.fill((0, 0, 255, 100))
    b_channel.blit(b_filter, (0, 0))
    
    # Shift channels with random offsets
    r_offset_x = random.randint(-intensity, intensity)
    r_offset_y = random.randint(-intensity // 2, intensity // 2)
    
    g_offset_x = random.randint(-intensity, intensity)
    g_offset_y = random.randint(-intensity // 2, intensity // 2)
    
    b_offset_x = random.randint(-intensity, intensity)
    b_offset_y = random.randint(-intensity // 2, intensity // 2)
    
    # Apply the shifted channels
    surface.blit(r_channel, (r_offset_x, r_offset_y))
    surface.blit(g_channel, (g_offset_x, g_offset_y))
    surface.blit(b_channel, (b_offset_x, b_offset_y))

def color_inversion_glitch(surface, probability=0.3):
    """
    Randomly inverts colors in parts of the screen
    """
    if random.random() < probability:
        width, height = surface.get_size()
        
        # Create an inverted version
        inverted = surface.copy()
        inverted.fill((255, 255, 255, 255), special_flags=pygame.BLEND_RGB_SUB)
        
        # Apply inverted parts randomly
        for _ in range(random.randint(3, 10)):
            x = random.randint(0, width - 50)
            y = random.randint(0, height - 50)
            w = random.randint(10, 100)
            h = random.randint(10, 100)
            
            try:
                inverted_part = inverted.subsurface(pygame.Rect(x, y, w, h))
                surface.blit(inverted_part, (x, y))
            except:
                pass