import pygame
import random
from tools import run_at_time
from effects.glitch_func import (
    BlockGlitch,
    DatamoshGlitch,
    intense_block_glitch,
    scary_datamosh_glitch,
    flick, screen_tear_glitch, rgb_split_glitch, ghosting_effect, error_message_glitch, wave_distortion,
    jump_scare_glitch,
     binary_rain_effect
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
    for _ in range(4):
        progress = elapsed_time / total_duration
        run_at_time(
            screen, img,
            intense_block_glitch,
            args=(block,),
            kwargs={"intensity": random.randint(3, 15)},
            duration=random.uniform(0.1, 0.3),
        )
        
        # Occasional subtle digital noise
        
        elapsed_time += 0.2
    
    # PHASE 2: Increasing frequency and intensity (2-4 seconds)
    for _ in range(5):
        progress = elapsed_time / total_duration
        run_at_time(
            screen, img,
            intense_block_glitch,
            args=(block,),
            kwargs={"intensity": random.randint(10, 35)},
            duration=random.uniform(0.15, 0.25),
        )
        
        # Add scanline glitches
       
        elapsed_time += 0.2
    
    # PHASE 3: More pronounced glitches with occasional flickers (4-6 seconds)
    for _ in range(3):
        progress = elapsed_time / total_duration
        run_at_time(
            screen, img,
            intense_block_glitch,
            args=(block,),
            kwargs={"intensity": random.randint(25, 50)},
            duration=random.uniform(0.2, 0.4),
        )
        
        # Add datamosh with progression
        run_at_time(
            screen, img,
            scary_datamosh_glitch,
            args=(datamosh,),
            kwargs={"intensity": random.randint(20, 60), "progress": progress},
            duration=0.3,
        )
        
        # Add screen tearing
        run_at_time(
            screen, img,
            screen_tear_glitch,
            kwargs={"intensity": random.randint(3, 8)},
            duration=0.2,
        )
        
        # Add occasional flickers as transition to more intense effects
        if random.random() > 0.6:
            run_at_time(
                screen, img,
                flick,
                kwargs={"base_image": img, "intensity": random.randint(800, 1500)},
                duration=random.uniform(0.1, 0.3),
            )
        
        # RGB split effect starts appearing
        if random.random() < 0.4:
            run_at_time(
                screen, img,
                rgb_split_glitch,
                kwargs={"intensity": random.randint(3, 7)},
                duration=0.3,
            )
        
        elapsed_time += 0.3
    
    # PHASE 4: Transition to more intense effects with mixed glitches (6-8 seconds)
    for _ in range(2):
        progress = elapsed_time / total_duration
        run_at_time(
            screen, img,
            intense_block_glitch,
            args=(block,),
            kwargs={"intensity": random.randint(40, 70)},
            duration=random.uniform(0.3, 0.5),
        )
        
        run_at_time(
            screen, img,
            scary_datamosh_glitch,
            args=(datamosh,),
            kwargs={"intensity": random.randint(50, 120), "progress": progress},
            duration=random.uniform(0.4, 0.6),
        )
        
        # Add wave distortion
        run_at_time(
            screen, img,
            wave_distortion,
            kwargs={"amplitude": random.randint(5, 10), "frequency": random.uniform(0.02, 0.05)},
            duration=0.4,
        )
        
        # Add error messages
       
        

        
        elapsed_time += 0.5
    
    # PHASE 5: Intense effects with frequent flickers (8-10 seconds)
    for _ in range(3):
        progress = elapsed_time / total_duration
        run_at_time(
            screen, img,
            scary_datamosh_glitch,
            args=(datamosh,),
            kwargs={"intensity": random.randint(100, 200), "progress": progress},
            duration=random.uniform(0.5, 0.8),
        )
        
        run_at_time(
            screen, img,
            flick,
            kwargs={"base_image": img, "intensity": random.randint(1500, 2500)},
            duration=random.uniform(0.2, 0.4),
        )
        
        # Ghosting effect
        run_at_time(
            screen, img,
            ghosting_effect,
            kwargs={"intensity": random.randint(5, 15), "decay": random.uniform(0.6, 0.8)},
            duration=0.4,
        )
        
        
        elapsed_time += 0.7
    
    # PHASE 6: Climax - maximum intensity effects (10-12 seconds)
    # Rapid intense block glitches
    for _ in range(4):
        progress = elapsed_time / total_duration
        run_at_time(
            screen, img,
            intense_block_glitch,
            args=(block,),
            kwargs={"intensity": random.randint(80, 100)},
            duration=0.2,
        )
        
     
        
        elapsed_time += 0.2
    
    # Powerful datamosh effects
    progress = elapsed_time / total_duration
    run_at_time(
        screen, img,
        scary_datamosh_glitch,
        args=(datamosh,),
        kwargs={"intensity": random.randint(200, 280), "progress": progress},
        duration=1.0,
    )
    

    
    elapsed_time += 1.0
    
    # Final intense flickers leading to "crash"
    run_at_time(
        screen, img,
        flick,
        kwargs={"base_image": img, "intensity": 3500},
        duration=0.8,
    )
    
    # Jump scare if image available
    if scare_img:
        run_at_time(
            screen, img,
            jump_scare_glitch,
            kwargs={"scare_image": scare_img, "probability": 0.9},
            duration=0.2,
        )
    
    # Ultimate crash effect - sustained maximum intensity
    progress = 1.0  # Full crash
    run_at_time(
        screen, img,
        scary_datamosh_glitch,
        args=(datamosh,),
        kwargs={"intensity": 300, "progress": progress},
        duration=2.0,
    )
    
    # Binary rain effect (matrix style)
    run_at_time(
        screen, img,
        binary_rain_effect,
        kwargs={"intensity": 80},
        duration=2.5,
    )
    
    # Final blackout flicker
    run_at_time(
        screen, img,
        flick,
        kwargs={"base_image": img, "intensity": 5000},
        duration=3.0,
    )

    return True