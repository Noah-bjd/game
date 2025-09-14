import pygame
import random
import numpy as np
import math


class DatamoshGlitch:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.frame_buffer = []  # Store previous frames for datamoshing
        self.corruption_map = np.zeros((height, width), dtype=float)
        self.glitch_intensity = 0
        self.crash_progress = 0  # 0 to 1, tracks how far into the crash we are
        
    def add_frame(self, surface):
        """Store frame for datamoshing reference"""
        frame_copy = surface.copy()
        self.frame_buffer.append(frame_copy)
        # Keep only last 3 frames to prevent memory issues
        if len(self.frame_buffer) > 3:
            self.frame_buffer.pop(0)
    
    def update_crash_progress(self, progress):
        """Update how far into the crash sequence we are (0.0 to 1.0)"""
        self.crash_progress = max(0.0, min(1.0, progress))
    
    def datamosh_corruption(self, surface, intensity=15):
        """
        Simulates real datamoshing by corrupting motion vectors and I-frames
        """
        if len(self.frame_buffer) < 2:
            return
            
        width, height = surface.get_size()
        
        # Increase corruption based on crash progress
        intensity = int(intensity * (0.5 + self.crash_progress * 1.5))
        
        # Corrupt random blocks with previous frame data (simulates P-frame corruption)
        for _ in range(intensity):
            if random.random() < 0.7:  # 70% chance for block corruption
                # Random block size (simulates macroblocks)
                block_w = random.choice([8, 16, 32, 64])  # Common video block sizes
                block_h = random.choice([8, 16, 32, 64])
                
                x = random.randint(0, max(0, width - block_w))
                y = random.randint(0, max(0, height - block_h))
                
                # Get corrupted data from previous frames
                source_frame = random.choice(self.frame_buffer[:-1])
                
                # Motion vector corruption - offset where we sample from
                offset_x = random.randint(-int(50 * self.crash_progress), int(50 * self.crash_progress))
                offset_y = random.randint(-int(50 * self.crash_progress), int(50 * self.crash_progress))
                
                src_x = max(0, min(width - block_w, x + offset_x))
                src_y = max(0, min(height - block_h, y + offset_y))
                
                try:
                    corrupted_block = source_frame.subsurface(
                        pygame.Rect(src_x, src_y, block_w, block_h)
                    ).copy()
                    
                    # Add some distortion to the block
                    if random.random() < 0.3:
                        # Scale the block slightly
                        scaled_w = max(1, block_w + random.randint(-4, 4))
                        scaled_h = max(1, block_h + random.randint(-4, 4))
                        corrupted_block = pygame.transform.scale(corrupted_block, (scaled_w, scaled_h))
                    
                    surface.blit(corrupted_block, (x, y))
                except:
                    pass
    
    def smear_effect(self, surface, intensity=8):
        """
        Creates the characteristic datamosh smearing effect
        """
        width, height = surface.get_size()
        
        # Increase smearing based on crash progress
        intensity = int(intensity * (0.5 + self.crash_progress * 2))
        
        for _ in range(intensity):
            # Horizontal smearing (common in datamoshing)
            if random.random() < 0.6:
                y = random.randint(0, height - 1)
                smear_length = random.randint(20, int(200 * (0.5 + self.crash_progress)))
                source_x = random.randint(0, max(1, width - smear_length))
                
                try:
                    smear_rect = pygame.Rect(source_x, y, smear_length, 1)
                    smear_line = surface.subsurface(smear_rect).copy()
                    
                    # Repeat the smear across multiple lines
                    smear_height = random.randint(1, int(8 * (1 + self.crash_progress)))
                    for i in range(smear_height):
                        if y + i < height:
                            surface.blit(smear_line, (source_x, y + i))
                except:
                    pass
            
            # Vertical smearing
            else:
                x = random.randint(0, width - 1)
                smear_length = random.randint(15, int(100 * (0.5 + self.crash_progress)))
                source_y = random.randint(0, max(1, height - smear_length))
                
                try:
                    smear_rect = pygame.Rect(x, source_y, 1, smear_length)
                    smear_line = surface.subsurface(smear_rect).copy()
                    
                    # Repeat the smear across multiple columns
                    smear_width = random.randint(1, int(5 * (1 + self.crash_progress)))
                    for i in range(smear_width):
                        if x + i < width:
                            surface.blit(smear_line, (x + i, source_y))
                except:
                    pass
    
    def digital_snow(self, surface, intensity=100):
        """
        Creates scary digital snow effect - more intense as crash progresses
        """
        width, height = surface.get_size()
        
        # Increase snow intensity based on crash progress
        intensity = int(intensity * (1 + self.crash_progress * 3))
        
        for _ in range(intensity):
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            
            # Different types of digital noise
            noise_type = random.choice(["pixel", "line", "block", "text"])
            
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
                length = random.randint(5, int(30 * (1 + self.crash_progress)))
                color = (random.randint(150, 255), random.randint(150, 255), random.randint(150, 255))
                end_x = min(width, x + length)
                pygame.draw.line(surface, color, (x, y), (end_x, y))
                
            elif noise_type == "block":
                # Small corruption block
                size = random.randint(2, int(8 * (1 + self.crash_progress)))
                color = random.choice([
                    (255, 0, 255),    # Magenta corruption
                    (0, 255, 255),    # Cyan corruption
                    (255, 255, 0),    # Yellow corruption
                    (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
                ])
                pygame.draw.rect(surface, color, (x, y, size, size))
                
            elif noise_type == "text" and self.crash_progress > 0.7:
                # Add error text fragments during severe crash
                error_texts = ["ERROR", "FAIL", "0x", "CRASH", "MEM", "NULL", "EXCEPTION"]
                text = random.choice(error_texts)
                font = pygame.font.SysFont("monospace", random.randint(8, 16))
                text_surface = font.render(text, True, (255, 0, 0))
                surface.blit(text_surface, (x, y))
    
    def color_channel_corruption(self, surface):
        """
        Corrupts color channels like real compression artifacts
        """
        # Increase chance based on crash progress
        if random.random() < (0.3 + self.crash_progress * 0.5):
            width, height = surface.get_size()
            
            # Create channel shift
            shift_x = random.randint(-int(5 * (1 + self.crash_progress)), 
                                    int(5 * (1 + self.crash_progress)))
            shift_y = random.randint(-int(2 * (1 + self.crash_progress)), 
                                    int(2 * (1 + self.crash_progress)))
            
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
    
    def screen_tearing(self, surface, intensity=5):
        """
        Simulates screen tearing effect common in system crashes
        """
        if random.random() < (0.2 + self.crash_progress * 0.6):
            width, height = surface.get_size()
            
            # Create horizontal tears
            for _ in range(int(intensity * (1 + self.crash_progress))):
                tear_y = random.randint(0, height - 1)
                tear_offset = random.randint(-20, 20)
                
                # Copy a horizontal strip and shift it
                strip_height = random.randint(1, 5)
                try:
                    strip = surface.subsurface(pygame.Rect(0, tear_y, width, strip_height)).copy()
                    surface.blit(strip, (tear_offset, tear_y))
                except:
                    pass

    def system_error_overlay(self, surface):
        """
        Adds system error message overlays during severe crashes
        """
        if self.crash_progress > 0.8 and random.random() < 0.4:
            width, height = surface.get_size()
            
            # Create a semi-transparent overlay
            overlay = pygame.Surface((width, height), pygame.SRCALPHA)
            overlay_color = (30, 0, 0, 100)  # Dark red tint
            overlay.fill(overlay_color)
            surface.blit(overlay, (0, 0))
            
            # Add error text
            error_messages = [
                "SYSTEM FAILURE",
                "KERNEL PANIC",
                "MEMORY ACCESS VIOLATION",
                "CRITICAL ERROR",
                "UNRECOVERABLE FAULT"
            ]
            
            font = pygame.font.SysFont("monospace", 24)
            error_text = random.choice(error_messages)
            text_surface = font.render(error_text, True, (255, 50, 50))
            
            # Position text randomly on screen
            text_x = random.randint(20, width - text_surface.get_width() - 20)
            text_y = random.randint(20, height - text_surface.get_height() - 20)
            surface.blit(text_surface, (text_x, text_y))


def scary_datamosh_glitch(surface, glitch_obj, intensity=20, progress=0.0):
    """
    Main function to apply scary datamoshing glitch effect
    
    Parameters:
    - surface: the main display surface
    - glitch_obj: DatamoshGlitch instance
    - intensity: overall glitch strength
    - progress: how far into the crash sequence we are (0.0 to 1.0)
    """
    # Update crash progress
    glitch_obj.update_crash_progress(progress)
    
    # Store current frame
    glitch_obj.add_frame(surface)
    
    # Apply effects in order of real datamoshing corruption
    glitch_obj.datamosh_corruption(surface, intensity // 2)
    glitch_obj.smear_effect(surface, intensity // 3)
    glitch_obj.digital_snow(surface, intensity * 3)
    glitch_obj.color_channel_corruption(surface)
    glitch_obj.screen_tearing(surface, intensity // 4)
    glitch_obj.system_error_overlay(surface)
    
    # Random scary color overlays - more frequent as crash progresses
    if random.random() < (0.2 + progress * 0.6):
        width, height = surface.get_size()
        overlay_color = random.choice([
            (100, 0, 0, 40),      # Dark red
            (0, 100, 0, 30),      # Sickly green
            (50, 0, 50, 35),      # Dark purple
            (0, 0, 0, 60),        # Darkness flicker
            (100, 100, 0, 25),    # Yellowish
        ])
        overlay = pygame.Surface((width, height), pygame.SRCALPHA)
        overlay.fill(overlay_color)
        surface.blit(overlay, (0, 0))