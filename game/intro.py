import pygame
from datetime import datetime, timedelta
from effects.glitch_func import BlockGlitch, DatamoshGlitch, intense_block_glitch, scary_datamosh_glitch
from effects.glitch_func import flick
from tools import run_at_time
import random

def intro(screen) -> bool:
    w_width, w_height = screen.get_size()
    glitch_processor = BlockGlitch(w_width, w_height)
    run_at_time(
        screen,
        intense_block_glitch,
        args=(glitch_processor,),
        kwargs={"intensity": random.randint(20, 60)},
        duration=1,
    )

    return True
    