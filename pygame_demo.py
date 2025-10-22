"""pygame_demo.py

A minimal pygame demo that opens a window and shows a moving rectangle.

Controls:
- Esc or window close to exit
"""

import sys
import pygame

WIDTH, HEIGHT = 640, 480
BG = (30, 30, 30)
RECT_COLOR = (200, 60, 80)


def run():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pygame Demo")
    clock = pygame.time.Clock()

    rect = pygame.Rect(50, HEIGHT // 2 - 25, 50, 50)
    vel = 200  # pixels / second
    direction = 1

    running = True
    while running:
        dt = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        rect.x += direction * vel * dt
        if rect.right >= WIDTH:
            rect.right = WIDTH
            direction = -1
        elif rect.left <= 0:
            rect.left = 0
            direction = 1

        screen.fill(BG)
        pygame.draw.rect(screen, RECT_COLOR, rect)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    run()
