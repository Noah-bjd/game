import pygame
import random
import numpy as np

class DatamoshGlitch:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.frame_buffer = []  # Store previous frames for datamoshing
        self.corruption_map = np.zeros((height, width), dtype=float)
        self.glitch_intensity = 0
        
    def add_frame(self, surface):
        """Store frame for datamoshing reference"""
        frame_copy = surface.copy()
        self.frame_buffer.append(frame_copy)
        # Keep only last 5 frames to prevent memory issues
        if len(self.frame_buffer) > 5:
            self.frame_buffer.pop(0)
    
    def datamosh_corruption(self, surface, intensity=15):
        """
        Simulates real datamoshing by corrupting motion vectors and I-frames
        """
        if len(self.frame_buffer) < 2:
            return
            
        width, height = surface.get_size()
        
        # Corrupt random blocks with previous frame data (simulates P-frame corruption)
        for _ in range(intensity):
            if random.random() < 0.7:  # 70% chance for block corruption
                # Random block size (simulates macroblocks)
                block_w = random.choice([8, 16, 32])  # Common video block sizes
                block_h = random.choice([8, 16, 32])
                
                x = random.randint(0, max(0, width - block_w))
                y = random.randint(0, max(0, height - block_h))
                
                # Get corrupted data from previous frames
                source_frame = random.choice(self.frame_buffer[:-1])
                
                # Motion vector corruption - offset where we sample from
                offset_x = random.randint(-50, 50)
                offset_y = random.randint(-50, 50)
                
                src_x = max(0, min(width - block_w, x + offset_x))
                src_y = max(0, min(height - block_h, y + offset_y))
                
                try:
                    corrupted_block = source_frame.subsurface(
                        pygame.Rect(src_x, src_y, block_w, block_h)
                    ).copy()
                    surface.blit(corrupted_block, (x, y))
                except:
                    pass
    
    def smear_effect(self, surface, intensity=8):
        """
        Creates the characteristic datamosh smearing effect
        """
        width, height = surface.get_size()
        
        for _ in range(intensity):
            # Horizontal smearing (common in datamoshing)
            if random.random() < 0.6:
                y = random.randint(0, height - 1)
                smear_length = random.randint(20, 200)
                source_x = random.randint(0, max(1, width - smear_length))
                
                try:
                    smear_rect = pygame.Rect(source_x, y, smear_length, 1)
                    smear_line = surface.subsurface(smear_rect).copy()
                    
                    # Repeat the smear across multiple lines
                    smear_height = random.randint(1, 8)
                    for i in range(smear_height):
                        if y + i < height:
                            surface.blit(smear_line, (source_x, y + i))
                except:
                    pass
            
            # Vertical smearing
            else:
                x = random.randint(0, width - 1)
                smear_length = random.randint(15, 100)
                source_y = random.randint(0, max(1, height - smear_length))
                
                try:
                    smear_rect = pygame.Rect(x, source_y, 1, smear_length)
                    smear_line = surface.subsurface(smear_rect).copy()
                    
                    # Repeat the smear across multiple columns
                    smear_width = random.randint(1, 5)
                    for i in range(smear_width):
                        if x + i < width:
                            surface.blit(smear_line, (x + i, source_y))
                except:
                    pass
    
    def digital_snow(self, surface, intensity=100):
        """
        Creates scary digital snow effect
        """
        width, height = surface.get_size()
        
        for _ in range(intensity):
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            
            # Different types of digital noise
            noise_type = random.choice(["pixel", "line", "block"])
            
            if noise_type == "pixel":
                # Single pixel noise
                color = random.choice([
                    (255, 255, 255),  # White static
                    (0, 0, 0),        # Black static
                    (random.randint(200, 255), 0, 0),  # Red corruption
                    (0, random.randint(200, 255), random.randint(200, 255))  # Cyan
                ])
                pygame.draw.rect(surface, color, (x, y, 1, 1))
                
            elif noise_type == "line":
                # Horizontal static line
                length = random.randint(5, 30)
                color = (random.randint(150, 255), random.randint(150, 255), random.randint(150, 255))
                end_x = min(width, x + length)
                pygame.draw.line(surface, color, (x, y), (end_x, y))
                
            elif noise_type == "block":
                # Small corruption block
                size = random.randint(2, 8)
                color = random.choice([
                    (255, 0, 255),    # Magenta corruption
                    (0, 255, 255),    # Cyan corruption
                    (255, 255, 0),    # Yellow corruption
                    (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
                ])
                pygame.draw.rect(surface, color, (x, y, size, size))
    
    def color_channel_corruption(self, surface):
        """
        Corrupts color channels like real compression artifacts
        """
        if random.random() < 0.3:  # 30% chance per frame
            width, height = surface.get_size()
            
            # Create channel shift
            shift_x = random.randint(-5, 5)
            shift_y = random.randint(-2, 2)
            
            # Get surface as array for manipulation
            try:
                temp_surf = surface.copy()
                
                # Create color channel separation effect
                red_surf = surface.copy()
                blue_surf = surface.copy()
                
                # Shift red channel
                surface.blit(red_surf, (shift_x, shift_y), special_flags=pygame.BLEND_ADD)
                
                # Shift blue channel opposite direction
                surface.blit(blue_surf, (-shift_x, -shift_y), special_flags=pygame.BLEND_ADD)
                
            except:
                pass

def scary_datamosh_glitch(surface, glitch_obj, intensity=20):
    """
    Main function to apply scary datamoshing glitch effect
    
    Parameters:
    - surface: the main display surface
    - glitch_obj: DatamoshGlitch instance
    - intensity: overall glitch strength
    """
    # Store current frame
    glitch_obj.add_frame(surface)
    
    # Apply effects in order of real datamoshing corruption
    glitch_obj.datamosh_corruption(surface, intensity // 2)
    glitch_obj.smear_effect(surface, intensity // 3)
    glitch_obj.digital_snow(surface, intensity * 3)
    glitch_obj.color_channel_corruption(surface)
    
    # Random scary color overlays
    if random.random() < 0.2:  # 20% chance
        width, height = surface.get_size()
        overlay_color = random.choice([
            (100, 0, 0, 40),      # Dark red
            (0, 100, 0, 30),      # Sickly green
            (50, 0, 50, 35),      # Dark purple
            (0, 0, 0, 60),        # Darkness flicker
        ])
        overlay = pygame.Surface((width, height), pygame.SRCALPHA)
        overlay.fill(overlay_color)
        surface.blit(overlay, (0, 0))

# Example usage:
# glitch_processor = DatamoshGlitch(screen)  # Pass the screen surface directly
# 
# # In your game loop:
# scary_datamosh_glitch(screen, glitch_processor, intensity=25)