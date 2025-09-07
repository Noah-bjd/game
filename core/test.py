import pygame
import random
import numpy as np

def test(surface, base_image, intensity=30):
    """
    Scary Trojan-style glitch effect with mixed chaos.
    """
    width, height = surface.get_size()
    frame = base_image.copy()

    # --- 1. Screen tearing (both horizontal & vertical) ---
    for _ in range(intensity):
        block_w = random.randint(30, 200)
        block_h = random.randint(10, 120)
        x = random.randint(0, width - block_w)
        y = random.randint(0, height - block_h)
        slice_rect = pygame.Rect(x, y, block_w, block_h)
        slice_surface = frame.subsurface(slice_rect).copy()

        shift_x = random.randint(-80, 80)
        shift_y = random.randint(-40, 40)
        frame.blit(slice_surface, (x + shift_x, y + shift_y))

        # Occasionally rotate a block for chaos
        if random.random() < 0.1:
            slice_rot = pygame.transform.rotate(slice_surface, random.choice([90, 180, 270]))
            frame.blit(slice_rot, (x, y))

    # --- 2. RGB channel separation (different per channel) ---
    arr = pygame.surfarray.pixels3d(frame)
    ghost = np.zeros_like(arr)
    ghost[..., 0] = np.roll(arr[..., 0], random.randint(-20, 20), axis=1)  # Red horizontal shift
    ghost[..., 1] = np.roll(arr[..., 1], random.randint(-20, 20), axis=0)  # Green vertical shift
    ghost[..., 2] = np.roll(arr[..., 2], random.randint(-15, 15), axis=1)  # Blue horizontal shift
    del arr
    pygame.surfarray.blit_array(frame, ghost)

    # --- 3. Static fuzz clouds ---
    if random.random() < 0.5:
        noise = np.random.randint(0, 255, (width, height, 3), dtype=np.uint8)
        noise_surf = pygame.surfarray.make_surface(noise)
        noise_surf.set_alpha(random.randint(40, 120))
        frame.blit(noise_surf, (0, 0))

    # --- 4. Random inversion flash ---
    if random.random() < 0.05:
        inv = pygame.surfarray.pixels3d(frame)
        inv[:] = 255 - inv  # invert colors
        del inv

    # --- 5. Flashing color overlay (trojan vibe) ---
    if random.random() < 0.2:
        flash = pygame.Surface((width, height))
        flash.fill(random.choice([(255, 0, 0), (0, 255, 0), (0, 0, 255)]))
        flash.set_alpha(random.randint(60, 180))
        frame.blit(flash, (0, 0))

    surface.blit(frame, (0, 0))
