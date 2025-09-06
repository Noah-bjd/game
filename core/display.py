import pygame
import random
from .Flicker import flicker
from effects import BlockGlitch, intense_block_glitch , DatamoshGlitch, scary_datamosh_glitch , flick

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
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:  # ⬅️ change on SPACE
                    space_pressed = not space_pressed  # toggle between images
        
        window.blit(image, (0, 0))
        if space_pressed:
            # Apply the intense block glitch effect
            intense_block_glitch(window, glitch_processor, intensity=random.randint(20, 30))
            # Apply the scary datamosh glitch effect
            scary_datamosh_glitch(window, another_glitch_processor, intensity=random.randint(20, 30))
            flick(window, intensity=random.randint(5, 15))

        pygame.display.flip()
    
    pygame.quit()