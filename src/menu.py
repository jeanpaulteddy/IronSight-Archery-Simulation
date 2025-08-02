import pygame

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
BLUE = (50, 150, 255)

# Fonts
def get_font(size):
    return pygame.font.SysFont("arial", size)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)

def main_menu(screen):
    clock = pygame.time.Clock()

    while True:
        screen.fill(BLACK)

        draw_text("IronSight Archery Simulation", get_font(40), WHITE, screen, 400, 100)

        # Buttons (just visual for now)
        mx, my = pygame.mouse.get_pos()

        button_start = pygame.Rect(300, 200, 200, 50)
        button_target = pygame.Rect(300, 280, 200, 50)
        button_quit = pygame.Rect(300, 360, 200, 50)

        # Hover effect
        pygame.draw.rect(screen, BLUE if button_start.collidepoint((mx, my)) else GRAY, button_start)
        pygame.draw.rect(screen, BLUE if button_target.collidepoint((mx, my)) else GRAY, button_target)
        pygame.draw.rect(screen, BLUE if button_quit.collidepoint((mx, my)) else GRAY, button_quit)

        draw_text("Start", get_font(30), WHITE, screen, 400, 225)
        draw_text("Select Target", get_font(30), WHITE, screen, 400, 305)
        draw_text("Quit", get_font(30), WHITE, screen, 400, 385)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_start.collidepoint(event.pos):
                    return "start"
                elif button_target.collidepoint(event.pos):
                    return "select_target"
                elif button_quit.collidepoint(event.pos):
                    pygame.quit()
                    exit()

        pygame.display.flip()
        clock.tick(60)

def select_target_menu(screen):
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("arial", 28)

    # Define available targets and default selection
    options = [("40 cm", 40), ("60 cm", 60), ("80 cm", 80)]
    selected_index = 0

    while True:
        screen.fill(BLACK)

        # Title
        title = font.render("Select Target Face", True, WHITE)
        screen.blit(title, (screen.get_width() // 2 - title.get_width() // 2, 100))

        # Display options
        for i, (label, _) in enumerate(options):
            color = (255, 255, 0) if i == selected_index else GRAY
            text = font.render(label, True, color)
            screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, 200 + i * 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_index = (selected_index - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected_index = (selected_index + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    return options[selected_index]  # e.g., ("40 cm", 40)

        pygame.display.flip()
        clock.tick(60)

def confirm_exit(screen):
    font = get_font(36)
    small_font = get_font(28)
    clock = pygame.time.Clock()
    dialog_running = True

    width, height = screen.get_size()
    overlay = pygame.Surface((width, height), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))

    while dialog_running:
        screen.blit(overlay, (0, 0))

        prompt = font.render("Are you sure you want to end this session?", True, (255, 255, 255))
        yes_text = small_font.render("Yes (Y)", True, (255, 255, 255))
        no_text = small_font.render("No (N)", True, (255, 255, 255))

        screen.blit(prompt, (width // 2 - prompt.get_width() // 2, height // 2 - 60))
        screen.blit(yes_text, (width // 2 - 100, height // 2 + 10))
        screen.blit(no_text, (width // 2 + 50, height // 2 + 10))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    return True
                elif event.key == pygame.K_n or event.key == pygame.K_ESCAPE:
                    return False
            if event.type == pygame.QUIT:
                return True

        clock.tick(30)