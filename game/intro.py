import pygame
import random
from tools import run_at_time
from effects.glitch_func import (
    BlockGlitch,
    DatamoshGlitch,
    intense_block_glitch,
    scary_datamosh_glitch,
    flick,
)

def intro(screen, img) -> bool:
    w_width, w_height = screen.get_size()
    block = BlockGlitch(w_width, w_height)
    datamosh = DatamoshGlitch(w_width, w_height)
    
    total_duration = 8.0  # Total crash sequence duration in seconds
    elapsed_time = 0.0
    
    # Phase 1: Subtle beginnings - occasional small glitches
    for _ in range(4):
        run_at_time(
            screen, img,
            intense_block_glitch,
            args=(block,),
            kwargs={"intensity": random.randint(3, 15)},
            duration=random.uniform(0.1, 0.3),
        )
        elapsed_time += 0.2
    
    # Phase 2: Increasing frequency and intensity
    for _ in range(5):
        progress = elapsed_time / total_duration
        run_at_time(
            screen, img,
            intense_block_glitch,
            args=(block,),
            kwargs={"intensity": random.randint(10, 35)},
            duration=random.uniform(0.15, 0.25),
        )
        elapsed_time += 0.2
    
    # Phase 3: More pronounced glitches with occasional flickers
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
        
        # Add occasional flickers as transition to more intense effects
        if random.random() > 0.6:
            run_at_time(
                screen, img,
                flick,
                kwargs={"base_image": img, "intensity": random.randint(800, 1500)},
                duration=random.uniform(0.1, 0.3),
            )
        elapsed_time += 0.3
    
    # Phase 4: Transition to more intense datamosh effects with mixed glitches
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
        elapsed_time += 0.5
    
    # Phase 5: Intense datamoshing with frequent flickers
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
        elapsed_time += 0.7
    
    # Phase 6: Climax - maximum intensity effects
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
    
    # Ultimate crash effect - sustained maximum intensity
    progress = 1.0  # Full crash
    run_at_time(
        screen, img,
        scary_datamosh_glitch,
        args=(datamosh,),
        kwargs={"intensity": 300, "progress": progress},
        duration=2.0,
    )
    
    run_at_time(
        screen, img,
        flick,
        kwargs={"base_image": img, "intensity": 5000},
        duration=2.0,
    )

    return True