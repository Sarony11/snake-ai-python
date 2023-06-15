import pygame
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SNAKE_SIZE = 20
FOOD_SIZE = 20
SNAKE_COLOR = (0, 255, 0)  # Green
FOOD_COLOR = (255, 0, 0)  # Red
BACKGROUND_COLOR = (0, 0, 0)  # Black

snake = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]  # Snake starts at the center of the screen
direction = "RIGHT"  # Initial direction

def move_snake():
    head = snake[0]
    x, y = head

    if direction == "UP":
        y -= SNAKE_SIZE
    elif direction == "DOWN":
        y += SNAKE_SIZE
    elif direction == "LEFT":
        x -= SNAKE_SIZE
    elif direction == "RIGHT":
        x += SNAKE_SIZE

    new_head = (x, y)
    snake.insert(0, new_head)
    snake.pop()  # Remove the last segment to maintain the size of the snake

def draw_snake(screen):
    for segment in snake:
        x, y = segment
        pygame.draw.rect(screen, SNAKE_COLOR, (x, y, SNAKE_SIZE, SNAKE_SIZE))

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
        move_snake()
        draw_snake(screen)
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()