import pygame
import sys
import random

# ======================
# CONFIG
# ======================
#ANTES WIDTH, HEIGHT = 900, 600
WIDTH, HEIGHT = 1000, 650
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SKYSCRAPER")
clock = pygame.time.Clock()

FONT = pygame.font.SysFont("consolas", 22)
BIGFONT = pygame.font.SysFont("consolas", 32)

WHITE = (230, 230, 230)
BLACK = (10, 10, 10)
RED = (160, 40, 40)
GRAY = (120, 120, 120)

# ======================
# SANITY SYSTEM
# ======================
class SanitySystem:
    def __init__(self):
        self.value = 50
        self.state = "stable"

    def change(self, amount):
        self.value = max(0, min(100, self.value + amount))
        self.update_state()

    def destabilize(self):
        self.state = "unstable"

    def update_state(self):
        if self.value <= 25:
            self.state = "low"
        elif self.value >= 75:
            self.state = "high"
        else:
            self.state = "stable"

# ======================
# TEXT RENDER
# ======================
def draw_text(text, x, y, color=WHITE, font=FONT):
    lines = text.split("\n")
    for i, line in enumerate(lines):
        surf = font.render(line, True, color)
        screen.blit(surf, (x, y + i * 28))

# ======================
# SKY EVENT
# ======================
def sky_whisper(sanity):
    chance = {
        "stable": 0.15,
        "high": 0.05,
        "low": 0.3,
        "unstable": 0.6
    }[sanity.state]

    if random.random() < chance:
        return random.choice([
            "Você sente isso também.",
            "Nada aqui termina.",
            "Você não está sozinho.",
            "Parar também é uma escolha.",
            "Você já esteve aqui antes."
        ])
    return None

# ======================
# GAME STATE
# ======================
sanity = SanitySystem()
scene = "ROOM"
message = ""
sky_message = ""
wait_timer = 0

# ======================
# MAIN LOOP
# ======================
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    # SANITY VISUAL EFFECT
    if sanity.state == "low":
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(40)
        overlay.fill(RED)
        screen.blit(overlay, (0, 0))
    elif sanity.state == "high":
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(60)
        overlay.fill(GRAY)
        screen.blit(overlay, (0, 0))
    elif sanity.state == "unstable":
        offset = random.randint(-4, 4)
        screen.scroll(offset, 0)

    # EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # ======================
            # ROOM
            # ======================
            if scene == "ROOM":
                if event.key == pygame.K_1:
                    message = "O reflexo se move tarde demais."
                    sanity.destabilize()
                elif event.key == pygame.K_2:
                    message = "A porta não responde."
                    sanity.change(+2)
                elif event.key == pygame.K_3:
                    message = "O silêncio pesa mais do que deveria."
                    sanity.change(-3)

                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3]:
                    scene = "HALLWAY"
                    wait_timer = pygame.time.get_ticks()

            # ======================
            # HALLWAY
            # ======================
            elif scene == "HALLWAY":
                if event.key == pygame.K_1:
                    message = "A sala está vazia. Mas passos ecoam atrás."
                    sanity.change(-5)
                    sanity.destabilize()
                elif event.key == pygame.K_2:
                    message = "Você se afasta. Algo observa."
                    sanity.change(+3)

    # SKY MESSAGE
    if pygame.time.get_ticks() % 240 == 0:
        whisper = sky_whisper(sanity)
        if whisper:
            sky_message = whisper

    # ======================
    # DRAW SCENES
    # ======================
    if scene == "ROOM":
        draw_text("Você acorda em uma sala pequena.\n\n"
                  "1 - Olhar o espelho\n"
                  "2 - Examinar a porta\n"
                  "3 - Ficar parado",
                  60, 80)

    elif scene == "HALLWAY":
        draw_text("O corredor é longo demais.\n"
                  "Uma porta bate ao fundo.\n\n"
                  "1 - Abrir a porta\n"
                  "2 - Ir embora",
                  60, 80)

    draw_text(message, 60, HEIGHT - 140, RED)

    if sky_message:
        draw_text(sky_message, WIDTH//2 - 200, HEIGHT//2 + 120, GRAY, BIGFONT)

    pygame.display.flip()

pygame.quit()
sys.exit()
