import pygame
import random

def flick(surface, intensity=10):
    """
    Applies a fullscreen glitch effect by shifting screen slices in various directions.
    
    Parameters:
    - surface: the main display surface
    - intensity: number of glitch elements per frame
    """
    width, height = surface.get_size()

    for _ in range(intensity):
        glitch_type = random.choice(["horizontal", "vertical", "square"])

        if glitch_type == "horizontal":
            # Horizontal line slice (shifted left/right)
            slice_height = random.randint(5, 30)
            y = random.randint(0, height - slice_height)
            rect = pygame.Rect(0, y, width, slice_height)
            piece = surface.subsurface(rect).copy()
            offset = random.randint(-30, 30)
            surface.blit(piece, (offset, y))

        elif glitch_type == "vertical":
            # Vertical slice (shifted up/down)
            slice_width = random.randint(5, 30)
            x = random.randint(0, width - slice_width)
            rect = pygame.Rect(x, 0, slice_width, height)
            piece = surface.subsurface(rect).copy()
            offset = random.randint(-30, 30)
            surface.blit(piece, (x, offset))

        elif glitch_type == "square":
            # Square or rectangular block (moved in any direction)
            block_width = random.randint(10, 80)
            block_height = random.randint(10, 80)
            x = random.randint(0, width - block_width)
            y = random.randint(0, height - block_height)
            rect = pygame.Rect(x, y, block_width, block_height)
            piece = surface.subsurface(rect).copy()
            dx = random.randint(-30, 30)
            dy = random.randint(-30, 30)
            surface.blit(piece, (x + dx, y + dy))

        # Optional colored overlay glitch bar
        if random.random() < 0.3:
            overlay_color = random.choice([
                (255, 0, 0, 30),       # Red tint
                (0, 255, 255, 30),     # Cyan
                (255, 255, 255, 20),   # White flicker
                (0, 0, 255, 30),       # Blue
                (255, 0, 255, 25)      # Magenta
            ])
            overlay = pygame.Surface((width, height), pygame.SRCALPHA)
            overlay.fill(overlay_color)
            surface.blit(overlay, (0, 0))
