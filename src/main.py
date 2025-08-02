import pygame
import sys
import os
from menu import main_menu, select_target_menu, confirm_exit
from calibrate import run_calibration
from scoring import map_physical_to_screen, score_arrow_px
from scoring import get_scaled_ring_boundaries_px



pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.NOFRAME)
pygame.display.set_caption("IronSight Archery Simulation")

pixels_per_cm = run_calibration(screen)

target_diameter_cm = 40  # Default

while True:
    choice = main_menu(screen)

    if choice == "select_target":
        _, target_diameter_cm = select_target_menu(screen)

    elif choice == "start":
        # Load target image (always use the same image regardless of selected size)
        image_filename = "Target-Face.png"
        target_path = os.path.join("assets", "images", image_filename)
        target_img = pygame.image.load(target_path).convert_alpha()
        
        # Scale to real-life size using calibrated pixels/cm
        target_size_px = int(target_diameter_cm * pixels_per_cm)
        target_img = pygame.transform.smoothscale(target_img, (target_size_px, target_size_px))
        target_rect = target_img.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

        running = True
        return_to_menu = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if confirm_exit(screen):
                        running = False
                        return_to_menu = True
                # Allow exiting fullscreen and quitting by pressing ESC
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    if confirm_exit(screen):
                        running = False
                        return_to_menu = True

            screen.fill((0, 0, 0))
            screen.blit(target_img, target_rect)

            # Draw scoring rings aligned with image
            scaled_radius_px = target_size_px // 2
            ring_radii_px = get_scaled_ring_boundaries_px(scaled_radius_px)

            for r_px in ring_radii_px:
                pygame.draw.circle(screen, (57, 255, 20), target_rect.center, r_px, 1)

            # Simulated arrow hits (in cm relative to target center)
            arrow_hits_cm = [(-1.2, 0.5), (3.4, -2.1)]

            # Draw arrow hits and scores
            font = pygame.font.SysFont("arial", 20)
            for x_cm, y_cm in arrow_hits_cm:
                x_px, y_px = map_physical_to_screen(x_cm, y_cm, pixels_per_cm, target_rect.center, target_diameter_cm)
                pygame.draw.circle(screen, (255, 0, 0), (x_px, y_px), 5)
                score = score_arrow_px(x_px, y_px, target_rect.center, scaled_radius_px)
                score_text = font.render(str(score), True, (255, 255, 255))
                screen.blit(score_text, (x_px + 10, y_px))

            pygame.display.flip()

        if return_to_menu:
            continue

    elif choice == "quit":
        break