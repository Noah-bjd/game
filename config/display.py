import pygame
from PIL import Image

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
    clock = pygame.time.Clock()
    running = True
    w_width, w_height = window.get_size()

    # Scale the image to fullscreen
    image = pygame.transform.scale(image, (w_width, w_height))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        window.fill("white")
        window.blit(image, (0, 0))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
