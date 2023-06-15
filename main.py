import pygame
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SNAKE_SIZE = 20
FOOD_SIZE = 20
SNAKE_COLOR = (0, 255, 0)  # Green
FOOD_COLOR = (255, 0, 0)  # Red
BACKGROUND_COLOR = (0, 0, 0)  # Black

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")

    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(10)  # Controls the speed of the game, adjust as needed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()