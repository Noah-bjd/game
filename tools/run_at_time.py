from datetime import datetime, timedelta
import pygame

def run_at_time(screen, func, args=(), kwargs=None, duration=1): 
    if kwargs is None:
        kwargs = {}
    end_time = datetime.now() + timedelta(seconds=duration)
    clock = pygame.time.Clock()

    while datetime.now() < end_time:
        func(screen, *args, **kwargs)
        pygame.display.flip()
        clock.tick(60)  