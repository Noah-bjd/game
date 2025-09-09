import pygame
import random
import time
from effects.glitch_func import BlockGlitch, DatamoshGlitch, intense_block_glitch, scary_datamosh_glitch
from effects.glitch_func import flick
from .test import test
from game import intro

def show_fullscreen(pil_image):
    """
    Display a PIL image in fullscreen mode using pygame.
    :param pil_image: A PIL Image object.
    :return: None
    """
    # Convert PIL image to pygame Surface
    mode = pil_image.mode
    size = pil_image.size
    data = pil_image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    
    # Initialize pygame
    pygame.init()
    window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    running = True
    w_width, w_height = window.get_size()
    
    # Scale the image to fullscreen
    image = pygame.transform.scale(image, (w_width, w_height))
    space_pressed = False

    # Initialize the block glitch processor
    glitch_processor = BlockGlitch(w_width, w_height)
    another_glitch_processor = DatamoshGlitch(w_width, w_height)
    
    window.blit(image, (0, 0))
    intro(window)
    window.blit(image, (0, 0))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    space_pressed = not space_pressed 
        
        if space_pressed:
            # test(window, base_image=image, intensity=1000)
            """
                create a function which will signal the scary datamosh glitch with sound few time then call the new trojan glitch 
                to lach the game in pitch black goog
            """            
            ""

            # intense_block_glitch(window, glitch_processor, intensity=random.randint(20, 60))
            # flick(window, intensity=random.randint(5, 15))

        pygame.display.flip()
    
    pygame.quit()