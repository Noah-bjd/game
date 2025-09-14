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
