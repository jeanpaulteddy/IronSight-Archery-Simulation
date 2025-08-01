import pygame
import sys
import os
from menu import main_menu, select_target_menu
from calibrate import run_calibration

pygame.init()
screen = pygame.display.set_mode((800, 600))
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
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill((0, 0, 0))
            screen.blit(target_img, target_rect)
            pygame.display.flip()

        break

pygame.quit()
sys.exit()