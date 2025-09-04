import pygame
from .Flicker import flicker


def show_fullscreen(pil_image):
    """
    Display a PIL image in fullscreen mode using pygame.
    :param pil_image: A PIL Image object.
    :return: None
    """
    # Convert PIL ima ge to pygame Surface
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

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:  # ⬅️ change on SPACE
                    space_pressed = not space_pressed  # toggle between images

        window.fill("white")
        if space_pressed:
            # add animation isntead of flickers or reproduce window error
            flicker(window)
            screenshot = pygame.image.load("Hck.png")
            screenshot = pygame.transform.scale(screenshot, (w_width, w_height))
            window.blit(screenshot, (0, 0))
        else:
            window.blit(image, (0, 0))

        pygame.display.flip()

    pygame.quit()
