import pygame
import random
import math

class BlockGlitch:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.frame_buffer = []
        self.corrupted_blocks = []  # Track persistent corrupted blocks
        self.block_sizes = [8, 16, 32, 64, 128]  # Common block sizes
        
    def add_frame(self, surface):
        """Store frame for block corruption"""
        frame_copy = surface.copy()
        self.frame_buffer.append(frame_copy)
        if len(self.frame_buffer) > 6:
            self.frame_buffer.pop(0)
    
    def macroblocks_corruption(self, surface, intensity=20):
        """Simulates video codec macroblock corruption"""
        for _ in range(intensity):
            # Use realistic video block sizes
            block_size = random.choice(self.block_sizes)
            
            # Align to block boundaries (like real video codecs)
            x = (random.randint(0, self.width // block_size - 1)) * block_size
            y = (random.randint(0, self.height // block_size - 1)) * block_size
            
            # Ensure we don't go out of bounds
            if x + block_size > self.width:
                x = self.width - block_size
            if y + block_size > self.height:
                y = self.height - block_size
                
            block_type = random.choice(["displaced", "corrupted", "missing", "repeated", "inverted"])
            
            if block_type == "displaced" and len(self.frame_buffer) > 1:
                # Block from wrong position (motion vector error)
                source_frame = random.choice(self.frame_buffer[:-1])
                
                # Sample from random location
                src_x = random.randint(0, max(0, self.width - block_size))
                src_y = random.randint(0, max(0, self.height - block_size))
                
                try:
                    displaced_block = source_frame.subsurface(
                        pygame.Rect(src_x, src_y, block_size, block_size)
                    ).copy()
                    surface.blit(displaced_block, (x, y))
                except:
                    pass
                    
            elif block_type == "corrupted":
                # Corrupt the block with digital noise
                try:
                    block_rect = pygame.Rect(x, y, block_size, block_size)
                    block = surface.subsurface(block_rect).copy()
                    
                    # Add digital corruption
                    for i in range(block_size):
                        for j in range(block_size):
                            if random.random() < 0.3:  # 30% corruption rate
                                corrupted_color = random.choice([
                                    (255, 0, 255),    # Magenta
                                    (0, 255, 255),    # Cyan
                                    (255, 255, 0),    # Yellow
                                    (0, 0, 0),        # Black
                                    (255, 255, 255),  # White
                                ])
                                block.set_at((i, j), corrupted_color)
                    
                    surface.blit(block, (x, y))
                except:
                    pass
                    
            elif block_type == "missing":
                # Missing block (solid color)
                missing_color = random.choice([
                    (128, 128, 128),  # Gray (typical missing block)
                    (0, 0, 0),        # Black
                    (0, 255, 0),      # Green (chroma key)
                ])
                pygame.draw.rect(surface, missing_color, (x, y, block_size, block_size))
                
            elif block_type == "repeated":
                # Repeat a small section across the whole block
                try:
                    repeat_size = block_size // 4
                    if repeat_size > 0:
                        small_block = surface.subsurface(
                            pygame.Rect(x, y, repeat_size, repeat_size)
                        ).copy()
                        
                        # Tile it across the block
                        for tile_x in range(0, block_size, repeat_size):
                            for tile_y in range(0, block_size, repeat_size):
                                surface.blit(small_block, (x + tile_x, y + tile_y))
                except:
                    pass
                    
            elif block_type == "inverted":
                # Invert colors in the block
                try:
                    block_rect = pygame.Rect(x, y, block_size, block_size)
                    inverted = surface.subsurface(block_rect).copy()
                    
                    # Invert each pixel
                    for i in range(block_size):
                        for j in range(block_size):
                            try:
                                r, g, b = inverted.get_at((i, j))[:3]
                                inverted.set_at((i, j), (255-r, 255-g, 255-b))
                            except:
                                pass
                    
                    surface.blit(inverted, (x, y))
                except:
                    pass
    
    def block_streaming_errors(self, surface, intensity=12):
        """Simulates streaming/transmission block errors"""
        for _ in range(intensity):
            # Horizontal block strips (like streaming errors)
            strip_height = random.choice([8, 16, 32])
            y = random.randint(0, self.height - strip_height)
            
            error_type = random.choice(["shift", "duplicate", "noise", "freeze"])
            
            if error_type == "shift":
                # Horizontal shift of the entire strip
                try:
                    strip = surface.subsurface(
                        pygame.Rect(0, y, self.width, strip_height)
                    ).copy()
                    
                    # Shift left or right
                    shift = random.randint(-50, 50)
                    surface.blit(strip, (shift, y))
                    
                    # Fill the gap with corrupted data
                    if shift > 0:
                        # Fill left gap
                        gap_color = random.choice([(205, 150, 255), (10, 255, 255), (0, 0, 0)])
                        pygame.draw.rect(surface, gap_color, (0, y, shift, strip_height))
                    elif shift < 0:
                        # Fill right gap
                        gap_color = random.choice([(255, 220, 255), (70, 25, 255), (0, 0, 0)])
                        pygame.draw.rect(surface, gap_color, (self.width + shift, y, -shift, strip_height))
                except:
                    pass
                    
            elif error_type == "duplicate":
                # Duplicate strip from elsewhere
                if len(self.frame_buffer) > 0:
                    source_frame = random.choice(self.frame_buffer)
                    source_y = random.randint(0, self.height - strip_height)
                    
                    try:
                        dup_strip = source_frame.subsurface(
                            pygame.Rect(0, source_y, self.width, strip_height)
                        ).copy()
                        surface.blit(dup_strip, (0, y))
                    except:
                        pass
                        
            elif error_type == "noise":
                # Pure noise strip
                for x in range(0, self.width, 4):
                    for row in range(strip_height):
                        noise_color = (
                            random.randint(0, 255),
                            random.randint(100, 255),
                            random.randint(0, 255)
                        )
                        pygame.draw.rect(surface, noise_color, (x, y + row, 4, 1))
                        
            elif error_type == "freeze" and len(self.frame_buffer) > 2:
                # Frozen strip from old frame
                old_frame = self.frame_buffer[0]  # Oldest frame
                try:
                    frozen_strip = old_frame.subsurface(
                        pygame.Rect(0, y, self.width, strip_height)
                    ).copy()
                    surface.blit(frozen_strip, (0, y))
                except:
                    pass
    
    def compression_artifacts(self, surface, intensity=15):
        """Simulates JPEG/video compression artifacts"""
        for _ in range(intensity):
            # 8x8 DCT blocks (JPEG standard)
            block_size = 8
            x = (random.randint(0, self.width // block_size - 1)) * block_size
            y = (random.randint(0, self.height // block_size - 1)) * block_size
            
            artifact_type = random.choice(["dct_ringing", "quantization", "blocking"])
            
            if artifact_type == "dct_ringing":
                # Create ringing artifacts (oscillating patterns)
                try:
                    for i in range(block_size):
                        for j in range(block_size):
                            # Create oscillating pattern
                            wave = math.sin(i * 0.8) * math.sin(j * 0.8)
                            intensity_val = int(wave * 30 + 128)
                            intensity_val = max(0, min(255, intensity_val))
                            
                            color = (intensity_val, intensity_val, intensity_val)
                            surface.set_at((x + i, y + j), color)
                except:
                    pass
                    
            elif artifact_type == "quantization":
                # Posterization effect (reduced color depth)
                try:
                    block_rect = pygame.Rect(x, y, block_size, block_size)
                    block = surface.subsurface(block_rect).copy()
                    
                    for i in range(block_size):
                        for j in range(block_size):
                            r, g, b = block.get_at((i, j))[:3]
                            # Quantize to fewer levels
                            r = (r // 32) * 32
                            g = (g // 32) * 64
                            b = (b // 32) * 32
                            block.set_at((i, j), (r, g, b))
                    
                    surface.blit(block, (x, y))
                except:
                    pass
                    
            elif artifact_type == "blocking":
                # Visible block boundaries
                block_color = random.choice([
                    (255, 0, 0),      # Red
                    (0, 255, 0),      # Green
                    (0, 0, 255),      # Blue
                    (255, 255, 255),  # White
                ])
                # Draw block outline
                pygame.draw.rect(surface, block_color, (x, y, block_size, block_size), 1)

def intense_block_glitch(surface, glitch_obj, intensity=25):
    """
    Main function to apply intense block glitch effects
    
    Parameters:
    - surface: the main display surface
    - glitch_obj: BlockGlitch instance
    - intensity: overall glitch intensity
    """
    # Store current frame
    glitch_obj.add_frame(surface)
    
    # Apply block corruption effects
    glitch_obj.macroblocks_corruption(surface, intensity)
    glitch_obj.block_streaming_errors(surface, intensity // 2)
    glitch_obj.compression_artifacts(surface, intensity // 2)
    
    # Random color channel corruption for blocks
    if random.random() < 0.2:
        # Create color channel separation on block boundaries
        block_size = random.choice(glitch_obj.block_sizes)
        for _ in range(intensity // 4):
            x = (random.randint(0, glitch_obj.width // block_size - 1)) * block_size
            y = (random.randint(0, glitch_obj.height // block_size - 1)) * block_size
            
            try:
                block_rect = pygame.Rect(x, y, block_size, block_size)
                red_block = surface.subsurface(block_rect).copy()
                blue_block = surface.subsurface(block_rect).copy()
                
                # Shift channels
                shift = random.randint(-3, 3)
                surface.blit(red_block, (x + shift, y), special_flags=pygame.BLEND_ADD)
                surface.blit(blue_block, (x - shift, y), special_flags=pygame.BLEND_ADD)
            except:
                pass

# Example usage:
# block_processor = BlockGlitch(screen_width, screen_height)
# 
# # In your game loop:
# intense_block_glitch(screen, block_processor, intensity=30)