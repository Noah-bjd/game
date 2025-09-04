import pygame


def flicker(window: any):
    # remove image
    for i in range(5):
        window.fill("white")
        pygame.display.flip()
        window.fill("black")
        pygame.display.flip()
        window.fill("red")
        pygame.display.flip()
