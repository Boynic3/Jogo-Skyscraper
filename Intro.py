def intro():
    import os
    import pygame
    import sys
    import time


    # ======================
    # CONFIG
    # ======================
    WIDTH, HEIGHT = 1000, 650
    FPS = 30
    DURATION = 6  # duração total em segundos
    BG_COLOR = (5, 5, 5)
    TEXT_COLOR = (200, 200, 200)

    pygame.init()
    #som de fundo
    #configuracao para pegar da pasta assets
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    AUDIO_PATH = os.path.join(BASE_DIR, "assets", "skyscraper_ambient_intro.wav")
    pygame.mixer.init()
    pygame.mixer.music.load(AUDIO_PATH)
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)  # loop

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Skyscraper")
    clock = pygame.time.Clock()

    FONT = pygame.font.SysFont("consolas", 24)

    # ======================
    # ASCII TEXTOS
    # ======================
    ASCII_SKY = [
        "███████╗██╗  ██╗██╗   ██╗",
        "██╔════╝██║ ██╔╝╚██╗ ██╔╝",
        "███████╗█████╔╝  ╚████╔╝ ",
        "╚════██║██╔═██╗   ╚██╔╝  ",
        "███████║██║  ██╗   ██║   ",
        "╚══════╝╚═╝  ╚═╝   ╚═╝   ",
    ]

    ASCII_SCRAPER = [
        "███████╗ ██████╗ ██████╗  █████╗ ██████╗ ███████╗██████╗ ",
        "██╔════╝██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗",
        "███████╗██║     ╗██████╔╝███████║██████╔╝█████╗  ██████╔╝",
        "╚════██║██║     ║██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗",
        "███████║╚██████╔╝██║  ██║██║  ██║██║     ███████╗██║  ██║",
        "╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝",
    ]

    # ======================
    # POSIÇÕES (mais centralizado)
    center_x = WIDTH // 2
    base_y = HEIGHT // 2 - 175 #aqui ajusta a altura inicial
    sky_y = base_y
    scraper_y = HEIGHT + 80  # começa fora da tela

    scraper_target_y = base_y + len(ASCII_SKY) * 30 + 10
    scraper_speed = 120  # pixels por segundo

    # efeito TV antiga
    shake_timer = 0
    shake_x = 0
    shake_y = 0

    start_time = time.time()
    running = True
    show_scraper = False

    # ======================
    # MAIN LOOP
    # ======================
    while running:
        dt = clock.tick(FPS) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        elapsed = time.time() - start_time

        # efeito TV antiga (balanço irregular)
        shake_timer += dt
        if shake_timer > 0.08:
            shake_timer = 0
            shake_x = pygame.math.Vector2(-1, 1).elementwise() * 0
            shake_x = int((pygame.time.get_ticks() % 3) - 1)
            shake_y = int((pygame.time.get_ticks() % 3) - 1)

        # após 2 segundos, scraper começa a surgir
        if elapsed >= 2:
            show_scraper = True
            if scraper_y > scraper_target_y:
                scraper_y -= scraper_speed * dt

        screen.fill(BG_COLOR)

        # desenha SKY
        offset_y = sky_y
        for line in ASCII_SKY:
            surf = FONT.render(line, True, TEXT_COLOR)
            rect = surf.get_rect(centerx=center_x + shake_x)
            rect.y = offset_y + shake_y
            screen.blit(surf, rect)
            offset_y += 28

        # desenha SCRAPER surgindo embaixo
        if show_scraper:
            offset_y = scraper_y
            for line in ASCII_SCRAPER:
                surf = FONT.render(line, True, TEXT_COLOR)
                rect = surf.get_rect(centerx=center_x + shake_x)
                rect.y = offset_y + shake_y
                screen.blit(surf, rect)
                offset_y += 28

        pygame.display.flip()

        # encerra após DURATION segundos
        if elapsed >= DURATION:
            running = False

    #para o som
    pygame.mixer.music.stop()
    pygame.quit()

if __name__ == "__main__":
    intro()
