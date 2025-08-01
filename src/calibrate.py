import pygame

def run_calibration(screen):
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("arial", 24)
    big_font = pygame.font.SysFont("arial", 32)

    target_cm = 10
    box_width_px = 100
    box_height_px = 10

    while True:
        screen.fill((0, 0, 0))

        # Calculate rect
        box_rect = pygame.Rect(
            (screen.get_width() - box_width_px) // 2,
            (screen.get_height() - box_height_px) // 2,
            box_width_px,
            box_height_px
        )

        # Draw white bar
        pygame.draw.rect(screen, (255, 255, 255), box_rect)

        # Title
        title_text = big_font.render("Calibration Mode", True, (255, 255, 255))
        screen.blit(title_text, (screen.get_width() // 2 - title_text.get_width() // 2, 30))

        # Instructions
        instructions = [
            "Use ← and → arrow keys to adjust the white bar",
            "Make the bar measure exactly 10 centimeters on the wall",
            "Stand next to the foam wall with a ruler and project this screen",
            "Press Enter when done"
        ]

        for i, line in enumerate(instructions):
            text_surface = font.render(line, True, (200, 200, 200))
            screen.blit(text_surface, (screen.get_width() // 2 - text_surface.get_width() // 2, 80 + i * 30))

        # Metrics
        metric_text = font.render(f"Current width: {box_width_px}px = {box_width_px / target_cm:.2f} px/cm", True, (255, 255, 255))
        screen.blit(metric_text, (screen.get_width() // 2 - metric_text.get_width() // 2, box_rect.bottom + 30))

        # Visual 10 cm markers
        marker_y = box_rect.top - 40
        pygame.draw.line(screen, (200, 200, 200), (box_rect.left, marker_y), (box_rect.left, marker_y + 20), 2)
        pygame.draw.line(screen, (200, 200, 200), (box_rect.right, marker_y), (box_rect.right, marker_y + 20), 2)
        label = font.render("10 cm", True, (200, 200, 200))
        screen.blit(label, (screen.get_width() // 2 - label.get_width() // 2, marker_y - 10))

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    box_width_px += 5
                elif event.key == pygame.K_LEFT and box_width_px > 10:
                    box_width_px -= 5
                elif event.key == pygame.K_RETURN:
                    return box_width_px / target_cm

        pygame.display.flip()
        clock.tick(60)