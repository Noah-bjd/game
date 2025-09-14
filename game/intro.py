import pygame
import random
from tools import run_at_time
from effects.glitch_func import (
    BlockGlitch,
    DatamoshGlitch,
    intense_block_glitch,
    scary_datamosh_glitch,
    flick, rgb_split_glitch, ghosting_effect, wave_distortion,
    jump_scare_glitch,
    screen_tear_glitch
)

def intro(screen, img) -> bool:
    w_width, w_height = screen.get_size()
    block = BlockGlitch(w_width, w_height)
    datamosh = DatamoshGlitch(w_width, w_height)
    
    total_duration = 12.0  # Extended total crash sequence duration in seconds
    elapsed_time = 0.0
    
    # Load a scary image for jump scares (optional)
    try:
        scare_img = pygame.image.load("scary_image.png").convert_alpha()
    except:
        scare_img = None
    
    # PHASE 1: Subtle beginnings - occasional small glitches (0-2 seconds)


    
    return True